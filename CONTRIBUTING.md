# Linee guida per contribuire al Tesauro AI Governance

Grazie per il tuo interesse a migliorare questo tesauro bilingue (EN/IT) sulla governance dell'IA.

---

## Flusso editoriale

1. **Proposta**
 - Apri una **Issue** usando il template "Proposta di aggiornamento voce".
 - Devi includere **motivazioni** e **fonti normative/standard** a supporto.

2. **Valutazione**
 - Il **comitato editoriale** discute la proposta nell'Issue.
 - Possibili esiti: accettata, respinta, richiesta di revisione.

3. **Approvazione / Rifiuto**
 - Se la proposta è approvata, viene apseta una **Pull Request (PR)** che aggiorna il file 'tesauro.json'
 - Se respinta, l'Issue viene chiusa con una **giustificazione pubblica**.

4. **Pubblicazione**
 - Una volta fusa la PR su 'main', il sito si aggiorna automaticamente tramite GitHub Pages.
 - La giustificazione editoriale rimane visibile nella PR o nell'Issue collegata.

--- 

## Critreri di valutazione

- Coerenza terminologica EN/IT
- Allineamento a norme e standard internazionali (AI Act, ISO/IEC 22989, ecc.)
- Correttezza delle relazioni semantiche (broader / narrower / related)
- Trasparenza e tracciabilità delle fonti

--- 

## Come aprire una PR

- Aggiorna il file 'tesauro.json' con la nuova voce o la modifica approvata.
- Esegui lo script per rigenerare le pagine:
  ```bash
  python scripts/generate_docs.py
  