from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework import status
from fcm_django.models import FCMDevice
# Create your views here.

@api_view(['POST'])
def SendNotification(request):
    device_id = request.data.get('device_id', None)
    registration_id = request.data.get('registration_id', None)
    if registration_id is None:
        return Response({"message": "REGISTRATION_ID_CANNOT_BE_EMPTY"}, status=status.HTTP_400_BAD_REQUEST)
    device = FCMDevice.objects.all().filter(registration_id=registration_id).first()
    try:
        device.send_message(title="Django", body="Python/Django server", data={"status": "WORKING FINE AF"})
    except Exception as e:
        print (e)
        return Response({"message": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({"message": "NOTIFCATION_SENT"}, status=status.HTTP_200_OK)