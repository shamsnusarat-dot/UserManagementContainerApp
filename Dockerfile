# Base image
FROM python:3.11-slim

# Set work dir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Collect static (optional)
RUN python manage.py collectstatic --noinput || true

# Run server
CMD ["gunicorn", "user_management.wsgi:application", "--bind", "0.0.0.0:8000"]