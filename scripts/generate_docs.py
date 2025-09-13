import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TERMS_DIR = DOCS / "terms"
TERMS_DIR.mkdir(parents=True, exist_ok=True)

data_path = ROOT / "tesauro.json"
if not data_path.exists():
    print("❌ File tesauro.json non trovato nella root del progetto.")
    sys.exit(1)

# Carica i dati
data = json.loads(data_path.read_text(encoding="utf-8"))
terms = data.get("terms", [])

# Mappa ID → oggetto per collegamenti interni
by_id = {t.get("id", "").strip(): t for t in terms if t.get("id")}

def link_to(tid: str) -> str:
    tid = (tid or "").strip()
    if tid and tid in by_id:
        return f"[{tid}](./{tid}.md)"
    return tid or "—"

# Costruisci l'indice
index_lines = [
    "# Indice dei termini",
    "",
    "| ID | Inglese | Italiano |",
    "|---|---|---|",
]

for t in terms:
    tid = (t.get("id") or "").strip()
    en = (t.get("english") or "").strip()
    it = (t.get("italian") or "").strip()
    defn = t.get("definition", {}) or {}
    defn_en = defn.get("en", "") or ""
    defn_it = defn.get("it", "") or ""
    sources = t.get("sources", []) or []
    rel = t.get("relations", {}) or {}
    broader = [link_to(x) for x in (rel.get("broader") or [])]
    narrower = [link_to(x) for x in (rel.get("narrower") or [])]
    related = [link_to(x) for x in (rel.get("related") or [])]
    variants = t.get("variants", []) or []

    # Riga nell'indice
    index_lines.append(f"| [{tid}](./{tid}.md) | {en} | {it} |")

    # Sezione fonti (senza usare * condizionale)
    fonti_lines = [f"- {s}" for s in sources] if sources else ["_Nessuna fonte indicata._"]

    page_lines = [
        f"# {en} / {it} ({tid})",
        "",
        "## Definizioni",
    ]
    if defn_it:
        page_lines.append(f"**IT**: {defn_it}")
    if defn_en:
        page_lines.append(f"**EN**: {defn_en}")

    page_lines += [
        "",
        "## Fonti",
        *fonti_lines,
        "",
        "## Relazioni semantiche",
        f"- **Più ampio (broader)**: {', '.join(broader) if broader else '—'}",
        f"- **Più specifico (narrower)**: {', '.join(narrower) if narrower else '—'}",
        f"- **Correlati (related)**: {', '.join(related) if related else '—'}",
        "",
        "## Varianti",
        f"{', '.join(variants) if variants else '—'}",
        "",
        "[↩ Torna all’indice](./index.md)",
    ]

    (TERMS_DIR / f"{tid}.md").write_text("\n".join(page_lines), encoding="utf-8")

# Scrivi l'indice
(TERMS_DIR / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
print("✅ Generazione completata in docs/terms/")