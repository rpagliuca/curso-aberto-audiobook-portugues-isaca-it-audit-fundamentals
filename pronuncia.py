"""Mapa de pronúncia para a voz pt-BR do edge-tts.

O edge-tts não aceita <lang> nem <break> em SSML, então termos em inglês e siglas
são reescritos como o leitor brasileiro os falaria. Ordem importa: frases mais
longas antes das palavras soltas.
"""
import re

# Regra do Rafael (2026-11-13): toda sigla vai com pontos (TI → T.I.), sem exceção.
# Qualquer palavra de 2+ letras maiúsculas que sobrar depois do mapa fonético é soletrada.
# Algarismos romanos (II, III, IV...) ficam de fora.
ROMANOS = re.compile(r"^[IVXLC]+$")

# Termos em inglês reescritos foneticamente (case-insensitive).
FONETICA = [
    (r"\bIT Audit Fundamentals\b", "ái-tí audíti fândamêntous"),
    (r"\bIT general controls\b", "ái-tí djênerau contrôuls"),
    (r"\btools and techniques\b", "túls ênd tekníks"),
    (r"\breasonable assurance\b", "rízonabol achúrans"),
    (r"\bengagement letter\b", "enguêidjmant léter"),
    (r"\bapplication controls\b", "aplicâichon contrôuls"),
    (r"\boverlapping controls\b", "ôuver-léping contrôuls"),
    (r"\bcompensating control\b", "cômpenseiting contrôul"),
    (r"\bcontrol objective\b", "contrôul obdjéctiv"),
    (r"\binternal control\b", "intérnal contrôul"),
    (r"\bdetection risk\b", "ditékchon rísk"),
    (r"\binherent risk\b", "inírent rísk"),
    (r"\bcontrol risk\b", "contrôul rísk"),
    (r"\baudit charter\b", "audíti chárter"),
    (r"\baudit risk\b", "audíti rísk"),
    (r"\bmateriality\b", "matiriáliti"),
    (r"\bperformance\b", "perfórmans"),
    (r"\bguidelines\b", "gáid-láins"),
    (r"\bstandards\b", "istândards"),
    (r"\bfieldwork\b", "fíld-uôrk"),
    (r"\breporting\b", "ripórting"),
    (r"\bfollow-up\b", "fólou-âp"),
    (r"\bplanning\b", "plâning"),
    (r"\bpreventive\b", "privêntiv"),
    (r"\bdetective\b", "ditéctiv"),
    (r"\bcorrective\b", "corréctiv"),
    (r"\bdeterrent\b", "ditérrent"),
    (r"\bbackup\b", "bêcápi"),
    (r"\blogs\b", "lógues"),
]


def para_fala(texto: str) -> str:
    for padrao, troca in FONETICA:
        texto = re.sub(padrao, troca, texto, flags=re.IGNORECASE)
    def soletrar(m):
        s = m.group(0)
        return s if ROMANOS.match(s) else ".".join(s) + "."
    texto = re.sub(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}\b", soletrar, texto)
    return re.sub(r"(?<=[A-Z])\.\.", ".", texto)
