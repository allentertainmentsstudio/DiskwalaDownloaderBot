import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "34446649"))
API_HASH = os.getenv("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8735534617:AAFNBedzWsDRcsiw6GXBq7QAHbqJSJiDw0w")

ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "7892805795").split()))
DOWNLOAD_DIR = "downloads"
