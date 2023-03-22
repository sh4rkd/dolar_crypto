import requests

def get_USD(apikey):
    url = "https://api.apilayer.com/exchangerates_data/convert?to=MXN&from=USD&amount=1"

    payload = {}
    headers= {
    "apikey": apikey
    }

    try:
        response = requests.request("GET", url, headers=headers, data = payload)
        status_code = response.status_code
        result = response.json()
    except Exception as e:
        print(e)
    return f"""Al dia de hoy {result['date']}
1 USD 🇺🇸 son
{result['result']} MXN 🇲🇽
"""