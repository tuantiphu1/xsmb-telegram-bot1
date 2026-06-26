import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

API_URL = "https://xoso-api.vercel.app/api/mb"

try:
    res = requests.get(API_URL, timeout=10)
    data = res.json()
    print("API RESPONSE:", data)

    # 👉 thử nhiều kiểu lấy dữ liệu
    giai_db = None

    if isinstance(data, dict):
        giai_db = (
            data.get("giaiDB")
            or data.get("giaidb")
            or data.get("special")
            or (data.get("data", {}) if isinstance(data.get("data"), dict) else {}).get("special")
        )

    if not giai_db:
        giai_db = "Không lấy được giải ĐB"

    message = f"""📊 KẾT QUẢ XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

except Exception as e:
    # 👉 quan trọng: không cho bot chết
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": f"❌ Bot lỗi: {str(e)}"
    })

    raise
