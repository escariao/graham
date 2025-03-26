import requests
from bs4 import BeautifulSoup

def get_stock_data(stock_code):
    url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Erro ao acessar a página:", response.status_code)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    def extract_value(css_class):
        el = soup.find("strong", class_=css_class)
        if el:
            return float(el.text.strip().replace(",", ".").replace(" ", ""))
        return None

    # Possíveis classes (precisa ajustar conforme o HTML da página real)
    eps = extract_value("indicator-value lpa")
    vpa = extract_value("indicator-value vpa")
    price = soup.find("div", class_="price")

    if eps is None or vpa is None or price is None:
        print("Não encontrou os dados necessários.")
        return None

    current_price = float(price.text.strip().replace("R$", "").replace(",", ".").strip())

    return {
        "eps": eps,
        "vpa": vpa,
        "current_price": current_price
    }

# Teste
if __name__ == "__main__":
    print(get_stock_data("mypk3"))