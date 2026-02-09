from app.models import Product

CATEGORY_UPSELL_MAP = {
    "Flower": ["Accessories"],
    "Vape": ["Batteries"],
    "Edible": ["Low Dose"]
}


def choose_upsells(menu: list[Product], primary: Product) -> list[Product]:
    upsells = [
        p for p in menu
        if p.category in CATEGORY_UPSELL_MAP.get(primary.category, [])
    ]

    return sorted(upsells, key=lambda p: p.margin_score, reverse=True)[:2]
