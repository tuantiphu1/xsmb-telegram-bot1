import os
import asyncio
import requests
from playwright.async_api import async_playwright

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://xoso.com.vn/xsmb.html"


async def get_html():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(URL, timeout=60000)
        await page.wait_for_timeout(5000)  # chờ JS load

        html = await page.content()

        await browser.close()
        return html


def extract_db(html):
    import re

    # tìm đúng khu vực "Giải đặc biệt"
    match = re.search(
        r"Giải đặc biệt.*?(\d{5})",
        html,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1)

    return None


async def main():
    try:
        html = await get_html()

        db = extract_db(html)

        if not db:
            db = "Không lấy được"

        msg = f"""📊 XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {db}
"""

    except Exception as e:
        msg = f"❌ Lỗi: {str(e)}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )


asyncio.run(main())
