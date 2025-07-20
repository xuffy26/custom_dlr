# custom_dlr/urls.py

from django.urls import path
from .views import webhook_listener

urlpatterns = [
    path('chat360/webhook/', webhook_listener),
]
