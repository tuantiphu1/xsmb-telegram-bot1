import os
import requests
import re

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def extract_db(html):
    patterns = [
        r"Giải đặc biệt[^0-9]{0,50}(\d{5})",
        r"ĐB[^0-9]{0,50}(\d{5})",
        r"DB[^0-9]{0,50}(\d{5})",
    ]

    for p in patterns:
        m = re.search(p, html, re.IGNORECASE)
        if m:
            return m.group(1)

    return None

try:
    url = "https://xoso.com.vn/xsmb.html"

    html = requests.get(url, timeout=10).text

    giai_db = extract_db(html)

    if not giai_db:
        giai_db = "Không lấy được"

    msg = f"""📊 XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    msg = f"❌ Lỗi: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": msg}
)
