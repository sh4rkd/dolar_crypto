from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_EXCHANGE
from usd_api import get_USD
from usd_script import send_whatsapp

try:
    usd_message = get_USD(API_KEY_EXCHANGE)
    message = send_whatsapp(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,usd_message)
    print(f"message sent successfully {message}")
except Exception as e:
    print(e)