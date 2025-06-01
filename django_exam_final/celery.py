import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_exam_final.settings')

app = Celery('django_exam_final')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Additional configuration
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    timezone='UTC',
    accept_content=['json'],
    task_serializer='json'
)

# Auto-discover tasks
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')