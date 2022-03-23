"""
WSGI config for eHualien project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import django
from django.core.wsgi import get_wsgi_application

sys.path.append("C:\\herokuenv\\eHualien")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eHualien.settings')

application = get_wsgi_application()
django.setup()
