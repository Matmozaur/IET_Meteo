from __future__ import absolute_import, unicode_literals

from celery import Celery

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meteoAnalysis.settings')

app = Celery('meteoApp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-hour': {
        'task': 'meteoApp.tasks.download_data',
        'schedule': 3600.0,
        'args': ()
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()
