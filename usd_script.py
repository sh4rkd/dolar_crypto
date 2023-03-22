from twilio.rest import Client

def send_whatsapp(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,usd_message):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            from_=f'whatsapp:{PHONE_NUMBER}',
            body=usd_message,
            to='whatsapp:+5213111285778'
        )
    return message.sid