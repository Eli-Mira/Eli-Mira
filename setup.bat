@echo off
echo === Installing Eli-Mira ===
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
echo Done.
