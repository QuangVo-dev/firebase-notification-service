from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view, permission_classes, action, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from fcm_django.models import FCMDevice
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from fcm_django.api.rest_framework import FCMDeviceViewSet
from .models import DeviceTag
from .serializers import DeviceTagSerializer, DeviceSerializer, CreateDeviceSerializer
from rest_framework.viewsets import ModelViewSet
import json
# Create your views here.

# Create Device tag


class DeviceTagViewSet(ModelViewSet):
    queryset = DeviceTag.objects
    serializer_class = DeviceTagSerializer

# Create Device


class DeviceViewSet(FCMDeviceViewSet):
    queryset = FCMDevice.objects
    serializer_class = DeviceSerializer

    def create(self, request):
        serializer = CreateDeviceSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Send Notification
@api_view(['POST'])
@parser_classes((MultiPartParser, FormParser, ))
def SendNotification(request):
    registration_id = request.data.get('registration_id', None)
    title = request.data.get('title', None)
    body = request.data.get('body', None)
    icon = request.data.get('icon', None)
    data = request.data.get('data', None)
    tags = request.data.get('tags', None)
    path = default_storage.save(json.loads(
        json.dumps(str(icon))), ContentFile(icon.read()))

    if tags is not None:
        device_tags = DeviceTag.objects.all().filter(tags=tags)
        for tag in device_tags:
            for device in model_to_dict(tag)['devices']:
                device.send_message(title=title, body=body,
                                    icon=f'django_firebase/{path}', data=data)
        return Response({"message": "NOTIFICATION_SENT_FOR_TAG_DEVICES"}, status=status.HTTP_200_OK)

    if registration_id is None:
        return Response({"message": "REGISTRATION_ID_CANNOT_BE_EMPTY"}, status=status.HTTP_400_BAD_REQUEST)

    if title is None or body is None:
        return Response({"message": "NOTIFICATION_CONTENT_CANNOT_BE_EMPTY"}, status=status.HTTP_400_BAD_REQUEST)

    device=FCMDevice.objects.all().filter(registration_id=registration_id).first()

    try:
        device.send_message(title=title, body=body,
                            icon=f'django_firebase/{path}', data=data)
    except Exception as e:
        print(e)
        return Response({"message": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "NOTIFCATION_SENT"}, status=status.HTTP_200_OK)
