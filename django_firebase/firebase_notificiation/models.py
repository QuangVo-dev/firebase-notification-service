from django.db import models
from fcm_django.models import FCMDevice
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class DeviceTag(models.Model):
    tags = models.CharField(max_length=255)
    devices = models.ManyToManyField(FCMDevice, related_name='tags')