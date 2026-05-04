import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create superuser from environment variables if it does not exist'

    def handle(self, *args, **kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(f'Superuser "{username}" created.')
        else:
            self.stdout.write(f'Superuser "{username}" already exists.')
