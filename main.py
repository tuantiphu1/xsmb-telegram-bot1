import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

API = "https://www.minhngoc.net.vn/api/kqxs/mien-bac?ngay="

try:
    r = requests.get(API, timeout=10)
    data = r.json()

    # cấu trúc thực tế của Minh Ngọc
    giai_db = None

    if isinstance(data, dict):
        giai_db = (
            data.get("data", {}).get("db")
            or data.get("db")
            or data.get("giai_db")
        )

    if not giai_db:
        giai_db = "Không lấy được"

    msg = f"""📊 XỔ SỐ MIỀN BẮC PRO FINAL

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    msg = f"❌ Lỗi: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": msg}
)
