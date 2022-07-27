from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innyara.settings')

app = Celery('innyara')
# app.conf.update(timezone = "Spain/Madrid")
# app.conf.broker_url = 'redis://localhost:6379/0'
# app.conf.broker_transport_options = { 'master_name': "cluster1" }

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'**********Request: {self.request!r}')
    
# @app.task
# def hello():
#     print( '***********hello world')
#     return "***************"