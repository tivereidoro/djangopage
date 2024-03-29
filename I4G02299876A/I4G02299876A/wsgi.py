"""
WSGI config for I4G02299876A project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see the docs
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'I4G02299876A.settings')

application = get_wsgi_application()
