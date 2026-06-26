import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

API_URL = "https://xoso-api.vercel.app/api/mb"

try:
    res = requests.get(API_URL, timeout=10)

    print("STATUS:", res.status_code)
    print("TEXT:", res.text[:300])  # 👈 xem raw data

    # ❌ nếu rỗng → báo lỗi ngay
    if not res.text.strip():
        raise Exception("API trả về rỗng")

    data = res.json()

    giai_db = (
        data.get("giaiDB")
        or data.get("giaidb")
        or data.get("special")
        or data.get("data", {}).get("special")
        if isinstance(data.get("data"), dict)
        else None
    )

    if not giai_db:
        giai_db = "Không lấy được"

    message = f"""📊 KẾT QUẢ XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    message = f"❌ Lỗi API XSMB: {str(e)}"

# gửi telegram dù đúng hay lỗi
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
