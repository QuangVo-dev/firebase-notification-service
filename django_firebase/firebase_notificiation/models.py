from django.db import models
from fcm_django.models import FCMDevice
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class DeviceModel(FCMDevice):
    tags = ArrayField(base_field=models.CharField(max_length=255))
    