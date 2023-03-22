import requests

def get_crypto():
    try:
        response = requests.get(f"https://criptoya.com/api/bitso/btc/mxn/0.1").json()
        return f"""Bitcoin 🪙
compra: {response["ask"]}
venta: {response["bid"]}"""
    except Exception as e:
        print(e)