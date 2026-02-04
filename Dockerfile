FROM python:3.10-slim
MAINTAINER  Akhilesh ML
WORKDIR /app

#COPY Django .
COPY Django/requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -m pip install Pillow

#WORKDIR /app/django_app
COPY Django .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]






# FROM python:3.10-slim

# WORKDIR /app

# COPY Django/requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY Django .

# EXPOSE 8000

# CMD ["gunicorn", "manage_app.wsgi:application", "--bind", "0.0.0.0:8000"]
