import requests
import hashlib
import os

URL = "https://www.prl.res.in/prl-eng/advertisement"
STATE_FILE = "last_hash.txt"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers, timeout=20)
content = response.text

# 🔐 Create hash of page content
current_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

# 📂 Load previous hash
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old_hash = f.read().strip()
else:
    old_hash = None

# 🔁 Save current hash for next run
with open(STATE_FILE, "w") as f:
    f.write(current_hash)

# 🚨 Notify ONLY if page actually changed
if old_hash and current_hash != old_hash:
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(
        telegram_url,
        data={
            "chat_id": CHAT_ID,
            "text": "🚨 PRL WEBSITE UPDATED!\n\nCheck now:\nhttps://www.prl.res.in/prl-eng/advertisement"
        },
        timeout=20
    )
