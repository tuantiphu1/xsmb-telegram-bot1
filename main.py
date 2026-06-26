import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

API_URL = "https://xoso-api.vercel.app/api/mb"

res = requests.get(API_URL, timeout=10)
data = res.json()

print(data)  # để debug nếu cần

# 👉 cố gắng lấy giải đặc biệt
try:
    giai_db = data["data"]["special"]
except:
    try:
        giai_db = data["results"]["DB"][0]
    except:
        giai_db = "Không lấy được"

message = f"""📊 KẾT QUẢ XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
