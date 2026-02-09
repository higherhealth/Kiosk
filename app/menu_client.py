import httpx
from app.config import MENU_API_URL, MENU_API_KEY
from app.models import Product


async def fetch_live_menu() -> list[Product]:
    headers = {"Authorization": f"Bearer {MENU_API_KEY}"}

    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(MENU_API_URL, headers=headers)
        response.raise_for_status()

    return [Product(**p) for p in response.json() if p.get("available")]
