# Base image
FROM python:3.11-slim

# Set work dir
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=user_management.settings

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Collect static
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Run server
CMD ["gunicorn", "user_management.wsgi:application", "--bind", "0.0.0.0:8000"]