#!/bin/bash
set -e
echo "=== Installing Eli-Mira ==="
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "Done."
