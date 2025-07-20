from django.urls import path
from .views import TriggerDLRStatusCheck

urlpatterns = [
    path("trigger-dlr/", TriggerDLRStatusCheck.as_view(), name="trigger_dlr_status_check"),
]
