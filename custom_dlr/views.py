import json
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
if not scheduler.running:
    scheduler.start()

CALLBACK_URL = "http://117.206.82.68/srh-desktopwidget/chatwadlr/wabadelivery"
CHAT360_EMAIL = "partner+test@chat360.io"
CHAT360_PASSWORD = "Test@123"

@csrf_exempt
def webhook_listener(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event_type = data.get("event")
            message_id = data.get("message_id")

            if event_type == "template_message_sent" and message_id:
                run_time = datetime.now() + timedelta(minutes=2)
                scheduler.add_job(
                    func=fetch_and_forward_dlr,
                    trigger='date',
                    run_date=run_time,
                    args=[message_id]
                )
                return JsonResponse({"status": "scheduled"})
            return JsonResponse({"status": "ignored or invalid"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)
