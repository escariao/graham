import requests
from bs4 import BeautifulSoup

def get_stock_data(stock_code):
    """
    Busca os dados de uma ação no StatusInvest.
    
    Parâmetros:
        stock_code (str): Código da ação (por exemplo, 'PETR4').
    
    Retorna:
        dict: Dicionário com os valores extraídos: 'eps', 'vpa' e 'current_price'.
              Retorna None se ocorrer algum erro ou se os seletores não forem encontrados.
    """
    url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"
    
    # Define um User-Agent para evitar bloqueio por parte do site
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Status code: {response.status_code}")  # Para debug

        if response.status_code != 200:
            print(f"Erro ao acessar {url}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Ajuste os seletores de acordo com o HTML real do StatusInvest
        eps_element = soup.find("span", {"data-test": "earnings-per-share"})
        vpa_element = soup.find("span", {"data-test": "book-value-per-share"})
        price_element = soup.find("span", {"data-test": "price-value"})

        # Converte o texto para float, substituindo vírgulas por pontos
        eps = float(eps_element.text.strip().replace(",", ".")) if eps_element else None
        vpa = float(vpa_element.text.strip().replace(",", ".")) if vpa_element else None
        current_price = float(price_element.text.strip().replace(",", ".")) if price_element else None

        # Se algum dos campos for None, retornamos None
        if eps is None or vpa is None or current_price is None:
            return None

        return {
            "eps": eps,
            "vpa": vpa,
            "current_price": current_price
        }

    except Exception as e:
        print(f"Erro ao extrair os dados: {e}")
        return None

# Exemplo de uso:
if __name__ == "__main__":
    stock_code = "PETR4"  # Você pode testar com qualquer código de ação
    data = get_stock_data(stock_code)
    if data:
        print(f"Dados da ação {stock_code}:")
        print(f"EPS (LPA): {data['eps']}")
        print(f"VPA: {data['vpa']}")
        print(f"Preço Atual: {data['current_price']}")
    else:
        print("Não foi possível obter os dados.")
