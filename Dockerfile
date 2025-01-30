FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies

RUN apt-get update && apt-get install -y \
    libpq-dev gcc zlib1g-dev libjpeg-dev libffi-dev libkrb5-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy the Django project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "--error-logfile", "-", "patient_emr.wsgi:application"]
