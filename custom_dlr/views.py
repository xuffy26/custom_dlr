from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from custom_dlr.tasks import fetch_and_send_dlr

class CustomDLRWebhook(APIView):
    """
    Receives the initial webhook with message_id and callback_url,
    and delegates processing to the async task.
    """

    def post(self, request):
        try:
            message_id = request.data.get("message_id")
            callback_url = request.data.get("callback_url")
            bearer_token = request.data.get("bearer_token")

            if not all([message_id, callback_url, bearer_token]):
                return Response({
                    "status": False,
                    "message": "Missing required parameters: message_id, callback_url, bearer_token"
                }, status=status.HTTP_400_BAD_REQUEST)

            # Trigger Celery task
            fetch_and_send_dlr.delay(message_id, bearer_token, callback_url)

            return Response({
                "status": True,
                "message": "DLR task accepted for processing"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": False,
                "message": f"Error occurred: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
