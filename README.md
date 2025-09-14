# Tesauro AI Governance

Questo repository contiene un **tesauro bilingue (EN/IT) sulla governance dell’intelligenza artificiale**, progettato come risorsa digitale strutturata per promuovere omogeneità terminologica e trasparenza editoriale.

---

## Obiettivi
- Fornire un vocabolario controllato e aggiornabile sulla governance dell’IA.
- Mettere in dialogo prospettive normative, tecniche e filosofiche.
- Supportare policy maker, ricercatori ed esperti con uno strumento aperto e tracciabile.

---

## Struttura del progetto
- `tesauro.json` → formato sorgente con voci bilingui, definizioni, fonti e relazioni semantiche.
- `scripts/generate_docs.py` → script Python per generare automaticamente le pagine Markdown.
- `docs/` → documentazione pubblicata tramite [MkDocs](https://www.mkdocs.org/).
- `.github/` → workflow e template per Issues e Pull Request.
- `CHANGELOG.md` → storico delle modifiche (versionamento semantico).
- `CONTRIBUTING.md` → linee guida per chi vuole contribuire.

---

## Consultazione online
Il tesauro è pubblicato come sito statico su **GitHub Pages**:  
[https://mauritiuss.github.io/tesauro-ai/](https://mauritiuss.github.io/tesauro-ai/)

---

## Come contribuire
1. Apri una **Issue** con il template “Proposta di aggiornamento voce”.
2. Fornisci definizioni EN/IT, motivazione e fonti normative/standard.
3. Attendi la valutazione del comitato editoriale.
4. Se approvata, una Pull Request aggiornerà `tesauro.json` e rigenererà la documentazione.

Maggiori dettagli: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Storico versioni
Le modifiche sono tracciate nel file [CHANGELOG.md](CHANGELOG.md).  
Esempio:
- **0.3.0 (2025-09-14)** → aggiunta voce *Generative AI / IA generativa*
- **0.2.0 (2025-09-13)** → aggiunta voce *Agentic AI / IA agentica*
- **0.1.0 (2025-09-12)** → prima versione online

---

## Requisiti tecnici
- [Python 3](https://www.python.org/)  
- [MkDocs](https://www.mkdocs.org/)  

Setup rapido:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs
python scripts/generate_docs.py
mkdocs serve