import os
import requests
import xml.etree.ElementTree as ET

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://xskt.com.vn/rss-feed/mien-bac.rss"

try:
    res = requests.get(URL, timeout=10)
    res.raise_for_status()

    root = ET.fromstring(res.content)

    # RSS structure: channel -> item đầu tiên = kết quả mới nhất
    item = root.find(".//item")

    title = item.find("title").text if item is not None else "Không có dữ liệu"

    message = f"""📊 KẾT QUẢ XỔ SỐ MIỀN BẮC

🏆 {title}
"""

except Exception as e:
    message = f"❌ Lỗi RSS: {str(e)}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
