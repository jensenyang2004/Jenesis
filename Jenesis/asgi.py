"""
<<<<<<< HEAD
ASGI config for jenesis project.
=======
ASGI config for Jenesis project.
>>>>>>> origin/main

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jenesis.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jenesis.settings')
>>>>>>> origin/main

application = get_asgi_application()
