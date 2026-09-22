import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("8358575962:AAEc4tLrbOOm5Dbm1pttawejOZ0NOgnQryQ")

if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не найден в переменных окружения")

print("✅ BOT_TOKEN найден")
