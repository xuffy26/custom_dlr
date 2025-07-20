import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custom_dlr.settings')

app = Celery('custom_dlr')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
