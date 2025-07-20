import requests
import json
import logging

logger = logging.getLogger(__name__)

def fetch_dlr_status(message_id, bearer_token):
    """
    Pull DLR status from Chat360 Campaign Report API using the message ID.
    """
    url = f"https://app.chat360.io/service/campaign/report?message_id={message_id}"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching DLR status: {e}")
        return {"error": str(e)}

def send_to_callback(callback_url, payload):
    """
    Send the final DLR log to the client's callback URL.
    """
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(callback_url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending to callback: {e}")
        return {"error": str(e)}
