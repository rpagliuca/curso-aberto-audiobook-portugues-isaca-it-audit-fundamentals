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
    (r"\bInternet of Things\b", "ínternet óv tíngs"),
    (r"\bhuman in the loop\b", "riúman ín dâ lúp"),
    (r"\binfrastructure as code\b", "infra-ístrâkchur éz côud"),
    (r"\bartificial intelligence\b", "artifíchal intélidjens"),
    (r"\bgenerative AI\b", "djênerativ êi-ái"),
    (r"\btest data\b", "tést dêita"),
    (r"\btraining data\b", "trêining dêita"),
    (r"\bbig data\b", "bíg dêita"),
    (r"\bdata(?= (analytics|owner|dictionary|classification)\b)", "dêita"),
    (r"\bCI/CD\b", "C.I. C.D."),
    (r"\bCAATs\b", "C.A.A.T.S."),
    (r"\bbackups\b", "bêcápis"),
    (r"\blog\b", "lógue"),
    (r"\bISACA\b", "Izaca"),  # Rafael 2026-11-13: palavra corrida, não soletrada
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

# Palavras soltas em inglês (aplicadas depois das frases, das mais longas para as mais curtas;
# o limite não aceita hífen colado, para "risk" não pegar dentro de "risk-based").
PALAVRAS = {
    "abrupt": "abrâpt", "cause": "cóz", "time": "táim", "range": "rêindj", "substantive": "sâbstantiv", "acceptance": "akséptans", "access": "ákses", "accountability": "acáuntabíliti",
    "administrator": "administrêitor", "agile": "édjáil", "agreement": "agríment", "analysis": "anális",
    "analytics": "análitiks", "and": "ênd", "application": "aplicâichon", "approach": "apróutch",
    "area": "éria", "assessment": "assésment", "asset": "ásset", "assurance": "achúrans",
    "attribute": "átribiut", "audit": "audíti", "auditing": "audíting", "authentication": "autêntiquêichon",
    "authorization": "autorizêichon", "automation": "automêichon", "awareness": "auérness",
    "balancer": "bálancer", "baseline": "bêiss-láin", "batch": "bétch", "bias": "báias",
    "blockchain": "blóc-tchêin", "business": "bízness", "capacity": "capássiti", "change": "tchêindj",
    "changes": "tchêindjis", "changeover": "tchêindj-ôuver", "check": "tchék", "checklist": "tchék-lísti",
    "classification": "classificâichon", "closing": "clôusing", "cloud": "cláud", "code": "côud",
    "cold": "côuld", "community": "comiúniti", "compliance": "complaiâns",
    "computer-assisted": "compiúter-assísted", "computing": "compiúting", "condition": "condíchon",
    "confidence": "cônfidens", "configuration": "configuirêichon", "consensus": "consênsus",
    "containers": "contêiners", "continuity": "continúiti", "continuous": "contíniuos",
    "contracts": "cóntrakts", "control": "contrôul", "controls": "contrôuls", "creep": "críp",
    "criteria": "craitíria", "cycle": "sáicol", "database": "dêita-bêis", "datacenter": "dêita-cênter",
    "delivery": "delíveri", "demilitarized": "dimílitarráizd", "development": "devélopment",
    "devops": "dév-óps", "devsecops": "dév-séc-óps", "dictionary": "díkchonéri", "digit": "dídjit",
    "diligence": "díligens", "disaster": "dizáster", "discovery": "discâveri", "distributed": "distríbiuted",
    "documentation": "documentêichon", "drift": "drífti", "due": "diú", "duties": "diútis",
    "effect": "iféct", "emergency": "imêrdjenci", "end-user": "ênd-iúzer", "enterprise": "ênterpráiz",
    "entry": "êntri", "error": "érror", "evidence": "évidens", "exercise": "éxercáiz", "exit": "éguizit",
    "expected": "expéctid", "explainability": "explêinabíliti", "facility": "fassíliti",
    "finding": "fáinding", "firewall": "fáier-uól", "flags": "flégs", "foreign": "fórein",
    "forensic": "forênsic", "framework": "frêim-uôrk", "full": "fúl", "generalized": "djêneraláizd",
    "hardening": "rárdening", "hash": "réch", "hooks": "rúks", "hot": "rót", "hybrid": "ráibrid",
    "hypervisor": "ráiper-váizor", "iaas": "iás", "identification": "aidentificâichon", "impact": "ímpact",
    "incident": "íncident", "input": "ínput", "inquiry": "inkuáiri", "inspection": "inspékchon",
    "integrated": "íntegreited", "integration": "integrêichon", "integrity": "intégriti",
    "interruption": "interrâpchon", "inventory": "ínventóri", "job": "djób", "joiners": "djóiners",
    "judgmental": "djâdjmental", "key": "kí", "keys": "kís", "kick-off": "kík-óf", "learning": "lêrning",
    "least": "líst", "leavers": "lívers", "ledger": "lédjer", "level": "lével", "life": "láif",
    "limit": "límit", "linux": "línux", "load": "lôud", "logical": "lódjical", "machine": "machín",
    "machines": "machíns", "management": "mánadjment", "meeting": "míting", "mirrored": "mírrord",
    "model": "módel", "monitoring": "mônitoring", "movers": "múvers", "multi-factor": "mâlti-fáctor",
    "network": "nét-uôrk", "nonstatistical": "nón-estatístical", "normalization": "normalizêichon",
    "notebooks": "nôut-búks", "objective": "obdjéctiv", "observation": "obzervêichon",
    "operating": "óperêiting", "owner": "ôuner", "paas": "pás", "papers": "pêipers", "parallel": "páralel",
    "parties": "pártis", "patch": "pétch", "phased": "fêizd", "phishing": "fíchin", "pilot": "páilot",
    "plan": "plén", "point": "póint", "population": "populêichon",
    "post-implementation": "pôust-implementêichon", "precision": "pricíjon", "primary": "práimari",
    "private": "práivet", "privacy": "práivaci", "privilege": "prívilédj", "privileged": "prívilédjd",
    "problem": "próblem", "process": "prôcess", "professional": "proféchonal", "program": "prôugram",
    "programming": "prôugraming", "public": "pâblic", "quality": "kuáliti", "rate": "rêit",
    "reasonableness": "rízonabolness", "reciprocal": "ricíprocal", "recovery": "ricâveri", "red": "réd",
    "referential": "referênchal", "regression": "rigréchon", "release": "rilís",
    "reperformance": "ri-perfórmans", "resource": "rissórss", "response": "rispóns",
    "responsibility": "rispônsabíliti", "review": "riviú", "right": "ráit", "risk": "rísk",
    "risk-based": "rísk-bêist", "robotic": "robótic", "router": "ráuter", "run-to-run": "rân-tu-rân",
    "saas": "sás", "sample": "sémpol", "sampling": "sémpling", "scheduling": "skédjuling",
    "scope": "iscôup", "security": "sequiúriti", "segmentation": "segmentêichon",
    "segregation": "segreguêichon", "self-assessment": "sélf-assésment", "service": "sêrvis",
    "shared": "chérd", "simulation": "simulêichon", "site": "sáiti", "skepticism": "isképtissizem",
    "smart": "ismárt", "snapshot": "isnép-chót", "statistical": "estatístical",
    "stop-or-go": "istóp-ór-gôu", "stratified": "istrátifáid", "switch": "suítch", "system": "sístem",
    "tabletop": "têibol-tóp", "techniques": "tekníks", "test": "tést", "testing": "tésting",
    "third": "têrd", "third-party": "têrd-párti", "token": "tôuken", "tolerable": "tólerabol",
    "totals": "tôutals", "training": "trêining", "trust": "trâst", "unit": "iúnit",
    "universe": "iúnivers", "user": "iúzer", "utility": "iutíliti", "variable": "vérriabol",
    "walkthrough": "uók-trú", "warm": "uórm", "waterfall": "uóter-fól", "wide": "uáid",
    "windows": "uíndous", "wireless": "uáier-léss", "work": "uôrk", "zone": "zôun",
}
FONETICA += [(r"(?<![\w-])" + re.escape(p) + r"(?![\w-])", PALAVRAS[p])
             for p in sorted(PALAVRAS, key=len, reverse=True)]


def para_fala(texto: str) -> str:
    for padrao, troca in FONETICA:
        texto = re.sub(padrao, troca, texto, flags=re.IGNORECASE)
    def soletrar(m):
        s = m.group(0)
        return s if ROMANOS.match(s) else ".".join(s) + "."
    texto = re.sub(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}\b", soletrar, texto)
    return re.sub(r"(?<=[A-Z])\.\.", ".", texto)
