#!/usr/bin/env bash
set -euo pipefail
echo "[*] Creating virtualenv and installing backend dev deps..."
python3 -m venv .venv || true
. .venv/bin/activate
pip install -U pip
pip install -e backend/[dev]
echo "[*] Installing frontend deps..."
pushd frontend >/dev/null
npm i || true
popd >/dev/null
echo "[*] Bootstrapped. To run: 'docker compose up -d --build'"
