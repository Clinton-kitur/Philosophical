"""
WSGI config for motive project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'motive.settings')

application = get_wsgi_application()
web: gunicorn motive.wsgi:application --log-file -
create_superuser: python manage.py createsuperuser
