import os
import asyncio
import requests
from playwright.async_api import async_playwright

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://xoso.com.vn/xsmb.html"


async def get_db():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(URL, timeout=60000)

        # chờ bảng kết quả load xong
        await page.wait_for_selector("table", timeout=15000)

        # lấy ô chứa "ĐB"
        cells = await page.locator("td").all_text_contents()

        await browser.close()

        # tìm đúng chữ ĐB
        for i in range(len(cells)):
            if "ĐB" in cells[i]:
                # số thường nằm ô kế bên
                if i + 1 < len(cells):
                    return cells[i + 1].strip()

        return None


async def main():
    try:
        db = await get_db()

        if not db:
            db = "KHÔNG LẤY ĐƯỢC"

        msg = f"""📊 XỔ SỐ MIỀN BẮC

🏆 Giải đặc biệt: {db}
"""

    except Exception as e:
        msg = f"❌ Lỗi BOT: {str(e)}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )


asyncio.run(main())
