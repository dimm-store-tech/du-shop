#!/usr/bin/env bash
# exit on error
set -o errexit
/opt/render/project/src/.venv/bin/python3.10 -m pip install pywin32

# poetry install
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate