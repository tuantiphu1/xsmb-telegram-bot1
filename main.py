import os
import requests
import re

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

try:
    # web xổ số có cấu trúc ổn hơn mấy API random
    url = "https://xoso.com.vn/xsmb.html"
    res = requests.get(url, timeout=10)
    html = res.text

    # tìm số 5 chữ gần chữ "ĐB" hoặc "đặc biệt"
    patterns = [
        r"ĐB.*?(\d{5})",
        r"đặc biệt.*?(\d{5})",
        r"Giải đặc biệt.*?(\d{5})"
    ]

    giai_db = None

    for p in patterns:
        match = re.search(p, html, re.IGNORECASE)
        if match:
            giai_db = match.group(1)
            break

    if not giai_db:
        giai_db = "Không tìm thấy"

    message = f"""📊 XỔ SỐ MIỀN BẮC TEST

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    message = f"❌ Lỗi: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
