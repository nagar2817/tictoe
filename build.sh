#!/usr/bin/env bash
# exit on error
set -o errexit

# Ensure the directory for static files exists
mkdir -p /opt/render/project/src/staticfiles

# Activate the virtual environment
source /opt/render/project/src/.venv/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate