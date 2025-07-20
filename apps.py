from django.apps import AppConfig
from django.conf import settings

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        if not settings.SCHEDULER.running:
            settings.SCHEDULER.start()
