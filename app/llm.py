import os
from openai import OpenAI
from app.compliance import enforce_compliance
from app.models import Product
from app.config import MODEL_NAME, MAX_RESPONSE_SENTENCES

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are a cannabis retail kiosk assistant. "
    "Do not give medical advice. "
    "Use friendly, non-medical language."
)


def explain(primary: Product, upsells: list[Product]) -> str:
    prompt = (
        f"Product: {primary.name}\n"
        f"Category: {primary.category}\n"
        f"Tags: {', '.join(primary.tags)}\n"
        f"Upsells: {', '.join(u.name for u in upsells)}\n"
        "Explain briefly why this is a good choice."
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    text = response.choices[0].message.content.strip()
    text = ". ".join(text.split(". ")[:MAX_RESPONSE_SENTENCES])

    enforce_compliance(text)
    return text
