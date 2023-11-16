#!/bin/bash
echo "Create migrations"
python BE/DjangoAPI/manage.py makemigrations

echo "Apply migrations"
python BE/DjangoAPI/manage.py migrate

echo "Run server"
python BE/DjangoAPI/manage.py runserver 0.0.0.0:8000