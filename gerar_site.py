#!/usr/bin/env python3
"""Gera docs/index.html a partir de site/template.html, do plano abaixo e dos roteiros.

Seção com roteiro e MP3 vira card completo (player, resumo, quiz, transcrição);
seção ainda sem áudio aparece como card "em produção". Uso: python gerar_site.py
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


def main() -> None:
    quizzes, cards, total, prontas = {}, [], 0.0, 0
    for item in PLANO:
        c, d = card(*item, quizzes)
        cards.append(c)
        total += d
        prontas += d > 0
    corpo = f'''<header>
  <h1>ISACA IT Audit Fundamentals</h1>
  <p>Curso aberto em áudio, em português · para ouvir no carro, na caminhada, na academia</p>
  <div class="badges">
    <span class="badge">{prontas} de {len(PLANO)} seções · {mmss(total)}</span>
    <span class="badge green">Quiz e resumo por seção</span>
    <span class="badge green">Transcrição completa</span>
  </div>
</header>

<p class="carhint">🚗 No carro ou no fone: ⏮ volta 10 s · ⏭ avança 10 s · atravessa as seções como faixa única</p>

<div class="section-head"><h2>Conteúdo</h2><p>Uma seção de até 10 minutos para cada 10% da prova. Executar a auditoria (35%) ocupa quatro seções; ambiente de TI (25%), três.</p></div>
{"".join(cards)}
<div class="section-head"><h2>Perguntas e respostas</h2><p>Em produção: cerca de 1 hora em capítulos de ~8 minutos, no formato pergunta → silêncio para você responder → resposta.</p></div>
<div class="section-head"><h2>Simulado diagnóstico</h2><p>Em produção: 20 questões de múltipla escolha com nota por domínio.</p></div>

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
    print(f"docs/index.html: {prontas} seções com áudio, {mmss(total)}")


if __name__ == "__main__":
    main()
