import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

try:
    url = "https://www.minhngoc.net.vn/api/kqxs/mien-bac?ngay="
    res = requests.get(url, timeout=10)
    data = res.json()

    # lấy giải đặc biệt
    giai_db = data.get("data", {}).get("db") or "Không có dữ liệu"

    message = f"""📊 XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    message = f"❌ Lỗi: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
