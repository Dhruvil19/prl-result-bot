import requests
import hashlib
import os
from bs4 import BeautifulSoup

URL = "https://www.prl.res.in/prl-eng/advertisement"
STATE_FILE = "last_hash.txt"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers, timeout=20)

soup = BeautifulSoup(response.text, "html.parser")

# 🔍 ONLY advertisement section extract
ads_section = soup.get_text(strip=True)

# 🔐 Hash only meaningful content
current_hash = hashlib.sha256(ads_section.encode()).hexdigest()

# 📂 Load old hash
old_hash = None
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old_hash = f.read().strip()

# 💾 Save hash
with open(STATE_FILE, "w") as f:
    f.write(current_hash)

# 🚨 Alert only on REAL change
if old_hash and old_hash != current_hash:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "🚨 PRL Advertisement UPDATED!\n\nCheck:\nhttps://www.prl.res.in/prl-eng/advertisement"
        },
        timeout=20
    )

