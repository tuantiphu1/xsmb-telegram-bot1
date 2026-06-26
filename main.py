import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🎉 Xin chào! Bot đã kết nối thành công với GitHub Actions."
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.text)
