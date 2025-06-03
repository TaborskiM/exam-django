from django.contrib import admin
from .models import AdminTheme
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule

admin.site.register(AdminTheme)

# Register your models here.
