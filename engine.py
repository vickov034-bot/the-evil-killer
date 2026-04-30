import requests
import os
from config import Config

class Engine:
    @staticmethod
    def fetch_targets():
        try:
            res = requests.get(f"{Config.SB_URL}?select=*", headers=Config.HEADERS, timeout=10)
            return res.json() if res.status_code == 200 else []
        except:
            return []

    @staticmethod
    def send_action(target_id, action):
        url = f"{Config.SB_URL}?id=eq.{target_id}"
        payload = {"last_command": action}
        try:
            res = requests.patch(url, headers=Config.HEADERS, json=payload)
            return res.status_code in [200, 204]
        except:
            return False

    @staticmethod
    def save_log(data):
        if not os.path.exists('logs'): os.makedirs('logs')
        with open(Config.LOG_PATH, "a") as f:
            f.write(f"{data}\n")
