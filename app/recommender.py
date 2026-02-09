from app.rules import intent_match
from app.models import Product


def choose_primary(menu: list[Product], intent: str, budget: float) -> Product:
    candidates = [
        p for p in menu
        if p.price <= budget and intent_match(p, intent)
    ]

    if not candidates:
        candidates = [p for p in menu if p.price <= budget]

    return sorted(candidates, key=lambda p: p.margin_score, reverse=True)[0]
