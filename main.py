import os
import re
import asyncio
from playwright.async_api import async_playwright
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://xoso.com.vn/xsmb.html"


async def get_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(URL, timeout=60000)
        content = await page.content()

        await browser.close()
        return content


def extract_special(html):
    patterns = [
        r"Giải đặc biệt.*?(\d{5})",
        r"ĐB.*?(\d{5})",
        r"special.*?(\d{5})"
    ]

    for p in patterns:
        m = re.search(p, html, re.IGNORECASE)
        if m:
            return m.group(1)

    return None


async def main():
    try:
        html = await get_data()
        db = extract_special(html)

        if not db:
            db = "Không lấy được"

        msg = f"""📊 XỔ SỐ MIỀN BẮC PRO BOT

🏆 Giải đặc biệt: {db}
"""

    except Exception as e:
        msg = f"❌ Lỗi PRO BOT: {str(e)}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )


asyncio.run(main())
