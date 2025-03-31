import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("BRAPI_TOKEN")

def get_stock_data(stock_code):
    url = f"https://brapi.dev/api/quote/{stock_code.upper()}?range=1d&interval=1d"
    try:
        response = requests.get(url)
        data = response.json()

        if "results" not in data or not data["results"]:
            print("Erro: 'results' ausente ou vazio na resposta da API.")
            return None

        result = data["results"][0]
        eps = result.get("eps")
        vpa = result.get("bookValue")
        current_price = result.get("regularMarketPrice")

        if eps is None or vpa is None or current_price is None:
            print("Dados incompletos recebidos:", result)
            return None

        return {
            "eps": eps,
            "vpa": vpa,
            "current_price": current_price
        }

    except Exception as e:
        print("Erro ao obter dados da brapi.dev:", e)
        return None
