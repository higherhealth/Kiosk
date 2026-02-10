import csv
from app.models import Product

MENU_CSV_PATH = "menu.csv"

async def fetch_live_menu() -> list[Product]:
    products = []

    with open(MENU_CSV_PATH, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["available"].lower() != "true":
                continue

            products.append(
                Product(
                    product_id=row["product_id"],
                    name=row["name"],
                    category=row["category"],
                    price=float(row["price"]),
                    available=True,
                    tags=[t.strip() for t in row["tags"].split(",")],
                    margin_score=float(row["margin_score"]),
                )
            )

    return products
