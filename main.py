import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

API = "https://raw.githubusercontent.com/dzapk/xo-so-json/main/mb.json"

try:
    r = requests.get(API, timeout=10)
    r.raise_for_status()

    data = r.json()

    # format an toàn nhiều kiểu JSON
    giai_db = (
        data.get("giai_db")
        or data.get("giaidb")
        or data.get("DB")
        or data.get("special")
        or "Không lấy được"
    )

    message = f"""📊 KẾT QUẢ XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    message = f"❌ Lỗi API: {str(e)}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
