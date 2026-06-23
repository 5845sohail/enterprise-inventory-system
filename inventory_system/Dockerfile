
FROM python:3.11-slim

# environment variables to optimize Python inside a container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# directory inside the container's virtual filesystem
WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your local Django project code into the container
COPY . /app/


EXPOSE 8000