import requests
import os

URL = "https://www.prl.res.in/prl-eng/advertisement"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    r = requests.get(URL, headers=headers, timeout=30)
    r.raise_for_status()
    page = r.text.lower()
except Exception as e:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": f"❌ PRL site access error:\n{e}"}
    )
    exit()

KEYWORDS = [
    "result",
    "written test",
    "technical assistant",
    "advt",
    "notification",
]

if any(word in page for word in KEYWORDS):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "🚨 PRL UPDATE POSSIBLE!\nCheck website:\nhttps://www.prl.res.in/prl-eng/advertisement"
        }
    )
else:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "✅ PRL checked — no update yet"
        }
    )
