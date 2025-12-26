from __future__ import absolute_import  

import os

from celery import Celery
from core.settings import base

# Set the default Django settings module to the development settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

app = Celery("core")

# Configure the Celery application using the development settings, CELERY_...
app.config_from_object("core.settings.development", namespace="CELERY") 

# Automatically find and load any tasks defined in the installed apps of the project
app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
