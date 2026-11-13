#!/usr/bin/env python3
"""Lista o que a voz pt-BR pode ler mal depois do mapa de pronúncia: palavras que existem
no dicionário inglês e não no português, e tokens com maiúscula no meio (DevOps, IaaS).
Uso: python testes/checar_pronuncia.py [arquivos .md]   (sem argumentos: roteiro/ e perguntas/)"""
import glob, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pronuncia import para_fala
def dic(p): return {l.strip().lower() for l in open(p, encoding="utf-8", errors="ignore")}
EN, PT = dic("/usr/share/dict/american-english"), dic("/usr/share/dict/brazilian")
arqs = sys.argv[1:] or sorted(glob.glob("roteiro/*.md") + glob.glob("perguntas/*.md"))
achados = collections.defaultdict(set)
for a in arqs:
    md = open(a, encoding="utf-8").read()
    if "## Narração" in md:
        md = md.split("## Narração")[1].split("\n## ")[0]
    else:  # perguntas: só o que é falado
        md = "\n".join(l for l in md.splitlines() if re.match(r"^(P|R|E):", l) or not l.startswith(("#", "tipo:", "dominio:", "topicos:")))
    fala = para_fala(md)
    for w in re.findall(r"[A-Za-zÀ-ÿ][\wÀ-ÿ'/-]*", fala):
        lw = w.lower()
        if re.search(r"[a-z][A-Z]|[A-Z]{2}[a-z]", w) or (lw in EN and lw not in PT and len(lw) > 2):
            achados[w].add(os.path.basename(a)[:3])
for w in sorted(achados, key=str.lower):
    print(f"{w:30} {' '.join(sorted(achados[w]))}")
