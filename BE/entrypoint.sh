#!/bin/bash

# Activate the virtual environment
source django_venv/bin/activate

cd ./restApi

# Run migrations
python3 manage.py migrate

# Start the Django development server
python3 manage.py runserver 0.0.0.0:8000
