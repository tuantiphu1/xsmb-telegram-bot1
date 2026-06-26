import os
import requests
import re
from playwright.sync_api import sync_playwright

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://xoso.com.vn/xsmb.html"


def get_html():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, timeout=60000)
        page.wait_for_timeout(5000)
        html = page.content()
        browser.close()
        return html


def extract_db(html):
    """
    CHỈ LẤY ĐÚNG DÒNG 'ĐB' KHÔNG LẤY NHẦM SỐ KHÁC
    """
    lines = html.split("\n")

    for line in lines:
        # chuẩn hóa text
        clean = re.sub(r"<.*?>", " ", line)
        clean = re.sub(r"\s+", " ", clean).strip()

        # chỉ bắt dòng có ĐB
        if "ĐB" in clean:
            match = re.search(r"ĐB.*?(\d{5})", clean)
            if match:
                return match.group(1)

    return None


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})


def main():
    try:
        html = get_html()

        db = extract_db(html)

        if not db:
            db = "KHÔNG LẤY ĐƯỢC"

        msg = f"""📊 XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {db}
"""

    except Exception as e:
        msg = f"❌ Lỗi BOT: {str(e)}"

    send_telegram(msg)


if __name__ == "__main__":
    main()
