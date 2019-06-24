from rest_framework import serializers
from .models import DeviceTag
from fcm_django.models import FCMDevice


class DeviceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTag
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    tags = DeviceTagSerializer(many=True)

    class Meta:
        model = FCMDevice
        fields = '__all__'


class CreateDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = '__all__'
