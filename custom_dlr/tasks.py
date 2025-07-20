from celery import shared_task
import requests
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def fetch_and_forward_dlr_status(message_id, callback_url, bearer_token):
    try:
        time.sleep(120)  # Wait for 2 minutes before checking DLR status

        dlr_url = f"https://app.chat360.io/service/campaign/report?message_id={message_id}"
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }

        response = requests.get(dlr_url, headers=headers)
        response.raise_for_status()
        dlr_data = response.json()

        # Extract the relevant DLR info (handle missing fields as needed)
        dlr_status = dlr_data.get("status", "UNKNOWN")
        forwarded_payload = {
            "message_id": message_id,
            "dlr_status": dlr_status,
            "raw_response": dlr_data
        }

        callback_response = requests.post(callback_url, json=forwarded_payload)
        callback_response.raise_for_status()

        logger.info(f"DLR status forwarded successfully for {message_id}")
        return {"status": "success", "message": "DLR forwarded"}
    except Exception as e:
        logger.error(f"DLR forwarding failed for {message_id}: {str(e)}")
        return {"status": "error", "message": str(e)}
