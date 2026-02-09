BANNED_PHRASES = [
    "treat",
    "cure",
    "medical",
    "anxiety",
    "pain",
    "dosage"
]


def enforce_compliance(text: str):
    for word in BANNED_PHRASES:
        if word in text.lower():
            raise ValueError("Compliance violation")
