#!/usr/bin/env python3
"""Gera docs/index.html a partir de site/template.html, do plano abaixo e dos roteiros.

Seção com roteiro e MP3 vira card completo (player, resumo, quiz, transcrição);
seção ainda sem áudio aparece como card "em produção". Também gera os cards de perguntas e
respostas (perguntas/ + docs/*.cues.json), docs/simulado.html (simulado/simulado.md) e
docs/leitura.html (guia/guia-de-leitura.md). Uso: python gerar_site.py
"""
import html
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(RAIZ, "docs")
REPO = "https://github.com/rpagliuca/curso-aberto-audiobook-portugues-isaca-it-audit-fundamentals"

# (número, slug, título, domínio da prova, tópicos)
PLANO = [
    (1, "s01", "A função de auditoria, controles e riscos",
     "Audit Function 5% · Controls, Risk and Audit 8%",
     "A prova · fases da auditoria · carta de auditoria · independência · três linhas · normas da ISACA e ITAF · tipos de controle · risco de auditoria"),
    (2, "s02", "Executar a auditoria I: planejamento baseado em risco",
     "Performing an Audit 35%", "Universo de auditoria · avaliação de riscos · objetivos e escopo · programa de auditoria"),
    (3, "s03", "Executar a auditoria II: evidência, testes e amostragem",
     "Performing an Audit 35%", "Tipos de evidência · testes de controle e substantivos · amostragem estatística e não estatística"),
    (4, "s04", "Executar a auditoria III: análise de dados e papéis de trabalho",
     "Performing an Audit 35%", "Técnicas de auditoria assistidas por computador · auditoria contínua · papéis de trabalho · fraude"),
    (5, "s05", "Executar a auditoria IV: achados, relatório e acompanhamento",
     "Performing an Audit 35%", "Achados · estrutura do relatório · comunicação · acompanhamento · qualidade da auditoria"),
    (6, "s06", "Ambiente de TI I: infraestrutura, redes e sistemas operacionais",
     "IT Environment and Components 25%", "Hardware · redes · sistemas operacionais · virtualização"),
    (7, "s07", "Ambiente de TI II: aplicações, bancos de dados e desenvolvimento",
     "IT Environment and Components 25%", "Aplicações · bancos de dados · ciclo de desenvolvimento · interfaces"),
    (8, "s08", "Ambiente de TI III: operações, serviços e nuvem",
     "IT Environment and Components 25%", "Operações de TI · gestão de serviços · continuidade · nuvem"),
    (9, "s09", "Temas específicos de auditoria",
     "Specific Audit Subjects 15%", "Acesso lógico · gestão de mudanças · terceiros · incidentes · segurança"),
    (10, "s10", "Tecnologias novas",
     "Overview of Newer Technologies 12%", "Inteligência artificial · DevOps · Internet das Coisas · blockchain"),
]


def blocos(md: str) -> dict:
    partes, atual = {}, None
    for linha in md.splitlines():
        m = re.match(r"^## (.+)$", linha)
        if m:
            atual = m.group(1).strip()
            partes[atual] = []
        elif atual:
            partes[atual].append(linha)
    return {k: "\n".join(v).strip() for k, v in partes.items()}


def inline(t: str) -> str:
    t = html.escape(t)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def quiz(texto: str) -> list:
    qs = []
    for bloco in re.split(r"^### ", texto, flags=re.M)[1:]:
        linhas = bloco.strip().splitlines()
        q = {"q": linhas[0].strip(), "opts": [], "a": 0, "exp": ""}
        for l in linhas[1:]:
            m = re.match(r"^- \[( |x)\] (.+)$", l.strip())
            if m:
                if m.group(1) == "x":
                    q["a"] = len(q["opts"])
                q["opts"].append(m.group(2))
            elif l.startswith(">"):
                q["exp"] += inline(l[1:].strip())
        qs.append(q)
    return qs


def duracao(mp3: str) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp3],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


def mmss(s: float) -> str:
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def card(n, slug, titulo, dominio, topicos, quizzes) -> tuple[str, float]:
    roteiros = [f for f in os.listdir(os.path.join(RAIZ, "roteiro")) if f.startswith(slug + "-")]
    mp3 = os.path.join(DOCS, roteiros[0].replace(".md", ".mp3")) if roteiros else None
    cab = f'''  <div class="card-header">
    <div class="ep-num">{n}</div>
    <div class="card-meta">
      <h2>{html.escape(titulo)}</h2>
      <div class="topics">{html.escape(topicos)}</div>
    </div>
    <div class="duration">{{dur}}</div>
  </div>'''
    if not mp3 or not os.path.exists(mp3):
        return (f'<div class="card pendente" id="card-{n}">\n{cab.replace("{dur}", "em produção")}\n'
                f'  <div class="tags"><span class="tag slate">{html.escape(dominio)}</span></div>\n</div>\n', 0.0)
    md = open(os.path.join(RAIZ, "roteiro", roteiros[0]), encoding="utf-8").read()
    b = blocos(md)
    d = duracao(mp3)
    quizzes[str(n)] = quiz(b.get("Quiz", ""))
    resumo = "".join(f"<li>{inline(l[2:])}</li>" for l in b.get("Resumo", "").splitlines() if l.startswith("- "))
    paragrafos = [p.strip() for p in re.split(r"\n\s*\n", b["Narração"]) if p.strip()]
    transcr = "".join(f"<p>{inline(p)}</p>" for p in paragrafos)
    nq = len(quizzes[str(n)])
    corpo = f'''<div class="card" id="card-{n}">
{cab.replace("{dur}", mmss(d))}
  <div class="player" data-ep="{n}" data-label="Seção {n}" data-src="{os.path.basename(mp3)}">
    <button class="pp" aria-label="Tocar ou pausar a seção {n}">▶</button>
    <input class="seek" type="range" min="0" max="1000" value="0" step="1" aria-label="Posição na seção {n}">
    <span class="time">0:00</span>
  </div>
  <div class="skip-row">
    <button class="btn-skip" onclick="skip('audio-{n}',-30)">−30s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',-10)">−10s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',+10)">+10s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',+30)">+30s</button>
  </div>
  <div class="tags"><span class="tag">{html.escape(dominio)}</span><span class="tag amber">3 fixações no áudio</span></div>
  <div class="actions">
    <button class="btn-toggle" onclick="togglePanel('resumo-{n}',this)">📋 Resumo</button>
    <button class="btn-toggle" onclick="togglePanel('quiz-{n}',this)">🧠 Quiz · {nq}</button>
    <button class="btn-toggle" onclick="togglePanel('transcricao-{n}',this)">📄 Transcrição</button>
  </div>
  <div class="panel" id="resumo-{n}"><div class="panel-inner"><div class="resumo-title">Pontos da seção</div><ul class="resumo-list">{resumo}</ul></div></div>
  <div class="panel" id="quiz-{n}"><div class="panel-inner"><div id="quiz-{n}-body"></div></div></div>
  <div class="panel" id="transcricao-{n}"><div class="panel-inner transcricao">{transcr}</div></div>
</div>
'''
    return corpo, d


def cards_perguntas() -> tuple[str, float, int]:
    from gerar_perguntas import parse
    e, cards, total, n_perg = html.escape, [], 0.0, 0
    pasta = os.path.join(RAIZ, "perguntas")
    for f in sorted(x for x in os.listdir(pasta) if re.match(r"p\d+.*\.md$", x)):
        slug = f[:-3]
        cj = os.path.join(DOCS, slug + ".cues.json")
        if not os.path.exists(cj):
            continue
        ch = parse(os.path.join(pasta, f))
        d = json.load(open(cj, encoding="utf-8"))["duracao"]
        num = int(re.match(r"p(\d+)", slug).group(1))
        n = 100 + num
        novas = sum(1 for i in ch["itens"] if not i["revisao"])
        rev = len(ch["itens"]) - novas
        vistos, lis = set(), []
        for it in ch["itens"]:
            if it["id"] in vistos:
                continue
            vistos.add(it["id"])
            lis.append(f'<li><details><summary>{e(it["P"])}</summary><p><strong>{e(it["R"])}</strong> {e(it.get("E", ""))}</p></details></li>')
        m = ch["meta"]
        titulo = re.sub(r"^P\d+\s*[—-]\s*", "", ch["titulo"])
        classe = "purple" if m.get("tipo") == "misto" else ""
        cards.append(f'''<div class="card" id="card-{n}">
  <div class="card-header">
    <div class="ep-num qa">P{num}</div>
    <div class="card-meta">
      <h2>{e(titulo)}</h2>
      <div class="topics">{e(m.get("topicos", ""))}</div>
    </div>
    <div class="duration">{mmss(d)}</div>
  </div>
  <div class="player" data-ep="{n}" data-label="P{num}" data-src="{slug}.mp3">
    <button class="pp" aria-label="Tocar ou pausar P{num}">▶</button>
    <input class="seek" type="range" min="0" max="1000" value="0" step="1" aria-label="Posição em P{num}">
    <span class="time">0:00</span>
  </div>
  <div class="skip-row">
    <button class="btn-skip" onclick="skip('audio-{n}',-30)">−30s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',-5)">−5s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',+5)">+5s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',+30)">+30s</button>
  </div>
  <div class="tags">
    <span class="tag {classe}">{e(m.get("dominio", ""))}</span>
    <span class="tag green">{novas} perguntas</span>
    <span class="tag amber">{rev} revisões espaçadas</span>
  </div>
  <div class="actions">
    <button class="btn-toggle" onclick="togglePanel('resumo-{n}',this)">📄 Transcrição: perguntas e respostas</button>
  </div>
  <div class="panel" id="resumo-{n}"><div class="panel-inner"><div class="resumo-title">Toque na pergunta para ver a resposta</div><ul class="resumo-list qa-list">{"".join(lis)}</ul></div></div>
</div>
''')
        total += d
        n_perg += novas
    return "".join(cards), total, n_perg


def simulado() -> int:
    fonte = os.path.join(RAIZ, "simulado", "simulado.md")
    if not os.path.exists(fonte):
        return 0
    dominios, qs = {}, []
    for bloco in re.split(r"^## ", open(fonte, encoding="utf-8").read(), flags=re.M)[1:]:
        cab, _, resto = bloco.partition("\n")
        cod, _, nome = cab.strip().partition(" ")
        dominios[cod] = nome
        for q in quiz(resto):
            qs.append({"d": cod, "q": q["q"], "o": q["opts"], "a": q["a"], "e": html.unescape(re.sub(r"<[^>]+>", "", q["exp"]))})
    js = "const D=" + json.dumps(dominios, ensure_ascii=False) + ";\nconst Q=" + json.dumps(qs, ensure_ascii=False, indent=0) + ";"
    tpl = open(os.path.join(RAIZ, "site", "simulado-template.html"), encoding="utf-8").read()
    open(os.path.join(DOCS, "simulado.html"), "w", encoding="utf-8").write(tpl.replace("/*SIMULADO*/", js))
    return len(qs)


def md_simples(texto: str) -> str:
    """Markdown mínimo do guia: #, ##, ###, parágrafos, listas "- " e tabelas "| a | b |"."""
    out, lista, tabela = [], False, []
    def fecha():
        nonlocal lista, tabela
        if lista:
            out.append("</ul>"); lista = False
        if tabela:
            linhas = [l for l in tabela if not re.match(r"^\|[\s:|-]+\|$", l)]
            cel = lambda l: [c.strip() for c in l.strip("|").split("|")]
            h = "".join(f"<th>{inline(c)}</th>" for c in cel(linhas[0]))
            corpo = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cel(l)) + "</tr>" for l in linhas[1:])
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{corpo}</tbody></table>"); tabela = []
    for l in texto.splitlines():
        if l.startswith("|"):
            if lista: out.append("</ul>"); lista = False
            tabela.append(l); continue
        if l.startswith("- "):
            if tabela: fecha()
            if not lista: out.append("<ul>"); lista = True
            out.append(f"<li>{inline(l[2:])}</li>"); continue
        fecha()
        m = re.match(r"^(#{1,3}) (.+)$", l)
        if m:
            k = len(m.group(1)); out.append(f"<h{k}>{inline(m.group(2))}</h{k}>")
        elif l.strip():
            out.append(f"<p>{inline(l)}</p>")
    fecha()
    return "\n".join(out)


def leitura() -> bool:
    fonte = os.path.join(RAIZ, "guia", "guia-de-leitura.md")
    if not os.path.exists(fonte):
        return False
    tpl = open(os.path.join(RAIZ, "site", "leitura-template.html"), encoding="utf-8").read()
    open(os.path.join(DOCS, "leitura.html"), "w", encoding="utf-8").write(
        tpl.replace("<!--CORPO-->", md_simples(open(fonte, encoding="utf-8").read())))
    return True


def main() -> None:
    quizzes, cards, total, prontas = {}, [], 0.0, 0
    for item in PLANO:
        c, d = card(*item, quizzes)
        cards.append(c)
        total += d
        prontas += d > 0
    qa, total_qa, n_perg = cards_perguntas()
    n_sim = simulado()
    tem_leitura = leitura()
    extra = ""
    if n_sim:
        extra += '<a class="link-extra" href="simulado.html">🎯 Simulado diagnóstico · {} questões →</a>'.format(n_sim)
    if tem_leitura:
        extra += '<a class="link-extra" href="leitura.html">📖 Guia de leitura →</a>'
    corpo = f'''<header>
  <h1>ISACA IT Audit Fundamentals</h1>
  <p>Curso aberto em áudio, em português · para ouvir no carro, na caminhada, na academia</p>
  <div class="badges">
    <span class="badge">{prontas} de {len(PLANO)} seções · {mmss(total)}</span>
    <span class="badge">{n_perg} perguntas em áudio · {mmss(total_qa)}</span>
    <span class="badge green">Quiz e resumo por seção</span>
    <span class="badge green">Simulado com nota por domínio</span>
  </div>
  <div class="extras">{extra}</div>
</header>

<p class="carhint">🚗 No carro ou no fone: ⏮ volta 10 s · ⏭ avança 10 s · atravessa as seções como faixa única</p>

<div class="section-head"><h2>Conteúdo</h2><p>Uma seção de até 10 minutos para cada 10% da prova. Executar a auditoria (35%) ocupa quatro seções; ambiente de TI (25%), três.</p></div>
{"".join(cards)}
<div class="section-head"><h2>Perguntas e respostas</h2><p>Capítulos de ~8 minutos no formato pergunta → silêncio para você responder em voz alta → resposta. Algumas perguntas voltam mais adiante, de propósito.</p></div>
{qa}
<div class="section-head"><h2>Simulado diagnóstico</h2><p>20 questões nos pesos da prova, com nota por domínio e revisão das erradas. <a href="simulado.html" style="color:#60a5fa">Fazer o simulado →</a></p></div>

<footer>Curso aberto de estudo · <a href="{REPO}" style="color:#475569">código-fonte e roteiros no GitHub</a><br>Material independente, sem vínculo com a ISACA. IT Audit Fundamentals é marca da ISACA.</footer>

<div id="nowbar">
  <div class="nb-title" id="nb-title">Toque em ▶ para começar</div>
  <div class="nb-btns">
    <button onclick="prevEpisode()" aria-label="Seção anterior">⏮</button>
    <button onclick="seekBy(-10)" aria-label="Voltar 10 segundos">−10</button>
    <button class="main" id="nb-pp" onclick="toggle()" aria-label="Tocar ou pausar">▶</button>
    <button onclick="seekBy(10)" aria-label="Avançar 10 segundos">+10</button>
    <button onclick="nextEpisode()" aria-label="Próxima seção">⏭</button>
  </div>
</div>'''
    tpl = open(os.path.join(RAIZ, "site", "template.html"), encoding="utf-8").read()
    out = tpl.replace("<!--CORPO-->", corpo).replace("/*QUIZZES*/", json.dumps(quizzes, ensure_ascii=False))
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(out)
    print(f"docs/index.html: {prontas} seções ({mmss(total)}), {n_perg} perguntas ({mmss(total_qa)}), simulado com {n_sim} questões, leitura={tem_leitura}")


if __name__ == "__main__":
    main()
