# Use the official Python image with tag 3.8-slim
FROM python:3.8-slim

# Set environment variables to optimize Python for Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory within the container to /app/
WORKDIR /app/

# Copy the requirements.txt file to /app/
COPY requirements.txt /app/

# Upgrade pip and install project dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to /app/
COPY . /app/

# Run migrations and start the Django development server
CMD ["sh", "-c", "python ./BE/DjangoAPI/manage.py makemigrations && python ./BE/DjangoAPI/manage.py migrate && python ./BE/DjangoAPI/manage.py runserver 0.0.0.0:8000"]
