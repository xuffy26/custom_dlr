import requests

# Constant config values
CALLBACK_URL = "https://testtemple34teupdateevent.requestcatcher.com/"
CHAT360_EMAIL = "partner+test@chat360.io"
CHAT360_PASSWORD = "Test@123"

def get_fresh_token():
    try:
        login_url = "https://app.chat360.io/api/auth/login"
        credentials = {
            "email": CHAT360_EMAIL,
            "password": CHAT360_PASSWORD
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(login_url, json=credentials, headers=headers)
        response.raise_for_status()
        return response.json().get("access")
    except Exception as e:
        print(f"[AUTH ERROR] {e}")
        return None

def fetch_and_forward_dlr(message_id):
    try:
        token = get_fresh_token()
        if not token:
            print(f"[ERROR] Token fetch failed for {message_id}")
            return

        headers = {"Authorization": f"Bearer {token}"}
        dlr_url = f"https://app.chat360.io/service/campaign/report?message_id={message_id}"
        dlr_response = requests.get(dlr_url, headers=headers)
        dlr_data = dlr_response.json()

        payload = {
            "event": "template_dlr_status",
            "message_id": message_id,
            "status": dlr_data.get("status", "unknown"),
            "reason": dlr_data.get("reason", "N/A")
        }

        res = requests.post(CALLBACK_URL, json=payload)
        print(f"[INFO] DLR pushed: {message_id}, status: {payload['status']}")
    except Exception as e:
        print(f"[ERROR] DLR fetch/push failed for {message_id}: {e}")
