#!/bin/bash
cd /home/rashadstack/Desktop/elevate/backend
source venv/bin/activate

# Load environment variables from .env.backend
set -a
source ../.env.backend
set +a

# Start Django server
python manage.py runserver 0.0.0.0:8000
