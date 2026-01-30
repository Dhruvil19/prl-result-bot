import requests

URL = "https://www.prl.res.in/prl-eng/advertisement"
KEYWORDS = ["result", "written test result", "selection"]

BOT_TOKEN = "8410171083:AAH6ivYb2vE3nazTIjOihNuDIaJdGZIAPPc"
CHAT_ID = "2043365711"

headers = {"User-Agent": "Mozilla/5.0"}

page = requests.get(URL, headers=headers).text.lower()

for word in KEYWORDS:
    if word in page:
        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(telegram_url, data={
            "chat_id": CHAT_ID,
            "text": "🚨 PRL RESULT UPDATE FOUND!\nhttps://www.prl.res.in/prl-eng/advertisement"
        })
        break
