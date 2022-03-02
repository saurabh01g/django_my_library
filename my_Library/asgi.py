"""
ASGI config for my_Library project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
print("In asgi.py")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_Library.settings')

application = get_asgi_application()
