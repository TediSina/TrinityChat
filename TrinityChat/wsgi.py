"""
WSGI config for TrinityChat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise
from .settings import STATIC_ROOT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrinityChat.settings')

application = get_wsgi_application()

application = WhiteNoise(application, root=STATIC_ROOT)
application.add_files(STATIC_ROOT, prefix="static/")

app = application
