INTENT_TAG_MAP = {
    "relax": ["calming"],
    "uplifting": ["uplifting"],
    "best_seller": []
}


def intent_match(product, intent: str) -> bool:
    required = INTENT_TAG_MAP.get(intent, [])
    return all(tag in product.tags for tag in required)
