#!/bin/bash
set -e


echo "────────────────────────────────────────"
echo " Django startup"
echo "────────────────────────────────────────"

echo "[1/3] Running migrations..."
python manage.py migrate --noinput

echo "[2/3] Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "[3/3] Starting Gunicorn with Uvicorn workers..."
exec gunicorn raw_website.asgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --worker-class uvicorn.workers.UvicornWorker \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -