FROM python:3.7-alpine AS builder

EXPOSE 8000
WORKDIR /app

RUN apk add --no-cache bash

RUN pip install --upgrade pip
RUN pip install django
RUN pip install psycopg2-binary

COPY restApi .

WORKDIR /app/restApi

RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["/bin/sh", "-c", "source /app/django_venv/bin/activate && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
