import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://www.minhngoc.net.vn/xo-so-truc-tiep/mien-bac.html"

try:
    r = requests.get(URL, timeout=10, headers={
        "User-Agent": "Mozilla/5.0"
    })

    text = r.text

    # debug an toàn
    print(text[:500])

    # fallback cực đơn giản: tìm số 5 chữ
    import re
    matches = re.findall(r"\b\d{5}\b", text)

    giai_db = matches[0] if matches else "Không lấy được"

    msg = f"""📊 XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {giai_db}
"""

except Exception as e:
    msg = f"❌ Lỗi: {str(e)}"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": msg}
)
