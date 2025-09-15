# Changelog

Tutte le modifiche rilevanti al tesauro sono documentate in questo file.
Il versionamento segue lo schema **MAJOR.MINOR.PATCH**:

- **MAJOR**: modifiche strutturali o incompatibili (es. cambio formato sorgente).
- **MINOR**: nuove voci, nuove funzionalità editoriali.
- **PATCH**: correzioni minori o aggiornamenti a voci esistenti.

## [0.4.0] - 2025-09-13
### Aggiunto
- Nuova voce AI005 "Risk-based approach / Approccio basato sul rischio"
- Fonti: AI Act, NIST AI RMF, ISO/IEC 23894
- Relazioni semantiche: broader → AI001, related → AI002

## [0.3.0] - 2025-09-13
### Aggiunto
- Nuova voce AI004 "Generative AI / IA generativa" con definizione bilingue
- Fonti NIST e ISO/IEC
- Relazioni semantiche con AI001 (broader)

## [0.2.0] - 2025-09-13
### Aggiunto
- Nuova voce AI003 "Agentic AI / IA agentica" con definizione bilingue
- Fonti normative e accademiche di riferimento
- Relazioni semantiche con AI001 (broader)

## [0.1.0] - 2025-09-12
### Aggiunto
- Prima versione del tesauro online
- File sorgente `tesauro.json` con le voci AI001 e AI002
- Script `generate_docs.py` per generare le pagine
- Configurazione MkDocs e pubblicazione su GitHub Pages