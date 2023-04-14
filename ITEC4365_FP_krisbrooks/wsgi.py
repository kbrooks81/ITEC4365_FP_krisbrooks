"""
WSGI config for ITEC4365_FP_krisbrooks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITEC4365_FP_krisbrooks.settings')

application = get_wsgi_application()
