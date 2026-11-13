#!/usr/bin/env python3
"""Gera o MP3 de cada seção a partir de roteiro/sNN-*.md (bloco "## Narração").

Cada parágrafo vira um trecho de TTS (edge-tts, cache por hash em .tts-cache/),
decodificado para PCM; entre parágrafos entra um silêncio curto; um único encode
no fim. Uso: python gerar_audio.py [s01 s02 ...]   (sem argumentos: todas)
"""
import asyncio
import hashlib
import json
import os
import re
import subprocess
import sys

import edge_tts

from pronuncia import para_fala

VOZ = "pt-BR-AntonioNeural"
RATE = "+10%"
TAXA = 24000
PAUSA_PARAGRAFO = 0.7  # segundos

RAIZ = os.path.dirname(os.path.abspath(__file__))
ROTEIRO = os.path.join(RAIZ, "roteiro")
SAIDA = os.path.join(RAIZ, "docs")
CACHE = os.path.join(RAIZ, ".tts-cache")


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


def paragrafos(texto: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", texto) if p.strip()]


async def tts(texto: str) -> bytes:
    chave = hashlib.sha256(f"{VOZ}|{RATE}|{texto}".encode()).hexdigest()
    caminho = os.path.join(CACHE, chave + ".mp3")
    if not os.path.exists(caminho):
        os.makedirs(CACHE, exist_ok=True)
        # o serviço falha de forma intermitente (NoAudioReceived para o mesmo texto que
        # funciona segundos depois): tentar de novo com espera crescente
        for tentativa in range(8):
            try:
                await edge_tts.Communicate(texto, VOZ, rate=RATE).save(caminho + ".tmp")
                os.replace(caminho + ".tmp", caminho)
                break
            except Exception as erro:
                if tentativa == 7:
                    raise
                print(f"  tentativa {tentativa + 1} falhou ({type(erro).__name__}), nova em {2 ** tentativa} s")
                await asyncio.sleep(2 ** tentativa)
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", caminho, "-f", "s16le", "-ac", "1", "-ar", str(TAXA), "-"],
        check=True, capture_output=True,
    ).stdout
    return pcm


async def gerar(arquivo: str) -> dict:
    nome = os.path.splitext(os.path.basename(arquivo))[0]
    md = open(arquivo, encoding="utf-8").read()
    titulo = re.search(r"^# (.+)$", md, re.M).group(1).strip()
    narracao = blocos(md)["Narração"]
    silencio = b"\x00\x00" * int(TAXA * PAUSA_PARAGRAFO)
    pcm = bytearray()
    for p in paragrafos(narracao):
        pcm += await tts(para_fala(p)) + silencio
    destino = os.path.join(SAIDA, nome + ".mp3")
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ac", "1", "-ar", str(TAXA), "-i", "-",
         "-codec:a", "libmp3lame", "-b:a", "48k", "-metadata", f"title={titulo}", destino],
        input=bytes(pcm), check=True,
    )
    duracao = len(pcm) / 2 / TAXA
    print(f"{nome}: {duracao/60:.1f} min, {len(narracao.split())} palavras")
    return {"arquivo": nome + ".mp3", "titulo": titulo, "duracao": round(duracao, 1)}


async def main(filtro: list[str]) -> None:
    arquivos = sorted(
        os.path.join(ROTEIRO, f) for f in os.listdir(ROTEIRO)
        if f.endswith(".md") and (not filtro or f.split("-")[0] in filtro)
    )
    os.makedirs(SAIDA, exist_ok=True)
    for a in arquivos:
        await gerar(a)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
