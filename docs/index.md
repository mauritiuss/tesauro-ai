.venv/
site/

python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs
python scripts/generate_docs.py
clear
