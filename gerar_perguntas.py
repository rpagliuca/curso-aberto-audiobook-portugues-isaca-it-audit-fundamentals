#!/usr/bin/env python3
"""Gera os capítulos de perguntas e respostas (estilo Pimsleur) a partir de perguntas/pNN-*.md.

Formato-fonte (o mesmo do curso da ISO 27001): cabeçalho com tipo/dominio/topicos, blocos
"## Abertura", "## Perguntas" e "## Encerramento"; cada item é "### id" seguido de P:, R: e E:
(explicação, opcional); "### = id" repete um item anterior (revisão espaçada).

Silêncio depois da pergunta, dimensionado pela resposta esperada:
    pausa = tempo_para_lembrar + FATOR_FALA × duração da resposta falada, limitada a [MIN, MAX]
Saída: docs/pNN-*.mp3 e docs/pNN-*.cues.json (duração e marcas de tempo; o gerar_site.py lê).
Uso: python gerar_perguntas.py [p01 p02 ...]   (sem argumentos: todos)
"""
import asyncio
import json
import os
import re
import subprocess
import sys

from pronuncia import para_fala

TAXA = 24000  # o mesmo do gerar_audio.py; tts é importado em gerar(), para o gerar_site.py usar parse() sem edge-tts

RAIZ = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(RAIZ, "perguntas")
SAIDA = os.path.join(RAIZ, "docs")

PENSAR_NOVA, PENSAR_REVISAO = 4.0, 2.5
FATOR_FALA = 1.4
PAUSA_MIN, PAUSA_MAX = 5.5, 10.0
GAP_POS_RESPOSTA = 0.5
GAP_ENTRE_ITENS = 1.6
CAUDA_TTS = 0.75  # silêncio que o próprio edge-tts deixa no fim de cada trecho


def parse(caminho: str) -> dict:
    ch = {"meta": {}, "abertura": "", "encerramento": "", "itens": []}
    sec, item, por_id = None, None, {}
    for bruta in open(caminho, encoding="utf-8"):
        linha = bruta.rstrip("\n")
        if linha.startswith("# "):
            ch["titulo"] = linha[2:].strip()
            continue
        m = re.match(r"^(tipo|dominio|topicos):\s*(.+)$", linha)
        if m and sec is None:
            ch["meta"][m.group(1)] = m.group(2).strip()
            continue
        if linha.startswith("## "):
            sec, item = linha[3:].strip().lower(), None
            continue
        m = re.match(r"^### (=)?\s*(\S+)", linha)
        if m:
            if m.group(1):
                if m.group(2) not in por_id:
                    raise SystemExit(f"{caminho}: revisão de id inexistente: {m.group(2)}")
                item = None
                ch["itens"].append({"revisao": True, **{k: por_id[m.group(2)][k] for k in ("id", "P", "R")}})
            else:
                item = {"id": m.group(2), "revisao": False, "P": "", "R": "", "E": ""}
                por_id[item["id"]] = item
                ch["itens"].append(item)
            continue
        if sec in ("abertura", "encerramento"):
            ch[sec] = (ch[sec] + " " + linha.strip()).strip()
            continue
        if item is not None and linha.strip():
            m = re.match(r"^([PRE]):\s*(.*)$", linha)
            if m:
                item[m.group(1)] = m.group(2).strip()
                item["_cur"] = m.group(1)
            elif "_cur" in item:
                item[item["_cur"]] += " " + linha.strip()
    for it in ch["itens"]:
        it.pop("_cur", None)
        if not it["P"] or not it["R"]:
            raise SystemExit(f"{caminho}: item {it['id']} sem P ou R")
    return ch


def silencio(s: float) -> bytes:
    return b"\x00\x00" * int(max(0.0, s) * TAXA)


def dur(pcm) -> float:
    return len(pcm) / 2 / TAXA


async def gerar(caminho: str) -> None:
    from gerar_audio import tts
    ch = parse(caminho)
    slug = os.path.splitext(os.path.basename(caminho))[0]
    textos = [ch["abertura"], ch["encerramento"]]
    for it in ch["itens"]:
        textos += [it["P"], it["R"], it.get("E", "")]
    unicos = [t for t in dict.fromkeys(textos) if t]
    sem = asyncio.Semaphore(4)

    async def um(t):
        async with sem:
            return await tts(para_fala(t))

    audio = dict(zip(unicos, await asyncio.gather(*[um(t) for t in unicos])))

    out, cues = bytearray(), []
    if ch["abertura"]:
        out += audio[ch["abertura"]] + silencio(1.0)
    for it in ch["itens"]:
        r = audio[it["R"]]
        pausa = (PENSAR_REVISAO if it["revisao"] else PENSAR_NOVA) + FATOR_FALA * max(0.5, dur(r) - CAUDA_TTS)
        pausa = min(PAUSA_MAX, max(PAUSA_MIN, pausa))
        cue = {"id": it["id"], "revisao": it["revisao"], "t_pergunta": round(dur(out), 2)}
        out += audio[it["P"]]
        cue["pausa"] = round(pausa, 1)
        out += silencio(pausa - CAUDA_TTS)
        cue["t_resposta"] = round(dur(out), 2)
        out += r
        if it.get("E"):
            out += silencio(GAP_POS_RESPOSTA) + audio[it["E"]]
        out += silencio(GAP_ENTRE_ITENS)
        cues.append(cue)
    if ch["encerramento"]:
        out += audio[ch["encerramento"]]

    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ac", "1", "-ar", str(TAXA), "-i", "-",
         "-codec:a", "libmp3lame", "-b:a", "48k", "-metadata", f"title={ch['titulo']}",
         os.path.join(SAIDA, slug + ".mp3")],
        input=bytes(out), check=True,
    )
    total = dur(out)
    json.dump({"slug": slug, "duracao": round(total, 1), "cues": cues},
              open(os.path.join(SAIDA, slug + ".cues.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    novas = sum(1 for i in ch["itens"] if not i["revisao"])
    print(f"{slug}: {total/60:.1f} min, {novas} perguntas + {len(ch['itens']) - novas} revisões")


async def main(filtro: list[str]) -> None:
    arqs = sorted(f for f in os.listdir(FONTE) if re.match(r"p\d+.*\.md$", f))
    for f in arqs:
        if not filtro or f.split("-")[0] in filtro:
            await gerar(os.path.join(FONTE, f))


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
