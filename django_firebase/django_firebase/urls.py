"""django_firebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceViewSet
from firebase_notificiation.views import SendNotification
from django.conf.urls.static import static
from firebase_notificiation.views import DeviceTagViewSet, DeviceViewSet
from . import settings

router = DefaultRouter(trailing_slash=False)
router.register('devices', FCMDeviceViewSet)
router.register('test-devices', DeviceViewSet)
router.register('device-tags', DeviceTagViewSet)

urlpatterns = []
urlpatterns += router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/send-notification', SendNotification),
    path('firebase', TemplateView.as_view(
        template_name='index.html'), name='firebase'),
    path('firebase-messaging-sw.js', (TemplateView.as_view(template_name="firebase-messaging-sw.js",
                                                           content_type='application/javascript', )), name='firebase-messaging-sw.js')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
