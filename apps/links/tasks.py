from celery import shared_task
from django.db import models


@shared_task
def increment_click_count(short_code):
    from .models import Link
    Link.objects.filter(short_code=short_code).update(click_count=models.F('click_count') + 1)