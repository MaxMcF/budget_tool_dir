#!/bin/bash

set -e

cd /src

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn budget_tool.wsgi:application -w 3 -b :8000
