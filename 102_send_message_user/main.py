import requests
import os
TOKEN = os.environ.get("TELEGRAM_BOT_API_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")
message = "An user tried to reach you."
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message
