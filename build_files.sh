#!/bin/sh
set -eu

PYTHON_BIN="${PYTHON_BIN:-python3.12}"
VENV_DIR="${VENV_DIR:-.vercel_build_venv}"

"$PYTHON_BIN" -m venv "$VENV_DIR"
. "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py tailwind install
python manage.py migrate --noinput
python manage.py tailwind build
python manage.py collectstatic --noinput
