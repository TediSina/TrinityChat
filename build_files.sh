#!/bin/sh
set -eu

PYTHON_BIN="${PYTHON_BIN:-python3.12}"
VENV_DIR="${VENV_DIR:-.vercel_build_venv}"

"$PYTHON_BIN" -m venv "$VENV_DIR"
. "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py tailwind install

if [ "${RUN_MIGRATIONS:-0}" = "1" ]; then
    python manage.py migrate --noinput
else
    echo "Skipping database migrations during Vercel build. Set RUN_MIGRATIONS=1 to run them explicitly."
fi

python manage.py tailwind build
python manage.py collectstatic --noinput
