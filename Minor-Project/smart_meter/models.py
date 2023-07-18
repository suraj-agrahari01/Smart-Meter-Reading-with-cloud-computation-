from django.db import models
from django.urls import clear_script_prefix

# Create your models here.
class Notification(models.Model):
    user_notice = models.CharField(max_length=100)