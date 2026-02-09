import os

MENU_API_URL = os.getenv("MENU_API_URL")
MENU_API_KEY = os.getenv("MENU_API_KEY")

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
MAX_RESPONSE_SENTENCES = 3
