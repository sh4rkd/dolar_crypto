from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_EXCHANGE
from usd_api import get_USD
from usd_script import send_whatsapp
from crypto_api import get_crypto

try:
    usd_message = get_USD(API_KEY_EXCHANGE)
    usd_message += "\n"+get_crypto()
    message = send_whatsapp(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,usd_message)
    print(f"message sent successfully {message}")
except Exception as e:
    print(e)