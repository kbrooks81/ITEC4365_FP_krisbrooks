"""
ASGI config for ITEC4365_FP_krisbrooks project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITEC4365_FP_krisbrooks.settings')

application = get_asgi_application()
