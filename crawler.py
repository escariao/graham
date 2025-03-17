import requests
from bs4 import BeautifulSoup

def get_stock_data(stock_code):
    """
    Passo 1: Vamos apenas verificar se o HTML contém
    ou não as informações necessárias (EPS, VPA, preço).
    Neste momento, não extrairemos nada; só imprimimos
    para depurar.
    """
    url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.93 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"[DEBUG] Status code: {response.status_code}")

        if response.status_code != 200:
            print(f"[DEBUG] Erro ao acessar {url}")
            return None

        # Montamos o objeto BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # **Aqui imprimimos TODO o HTML** para analisar
        # (em produção, isso pode ser enorme e não é ideal,
        # mas serve para depuração).
        print("\n[DEBUG] HTML completo:")
        print(soup.prettify())

        # Por ora, não faremos a extração. Vamos retornar None
        # para que o app.py mostre "Erro ao obter dados".
        return None

    except Exception as e:
        print(f"[DEBUG] Erro ao extrair os dados: {e}")
        return None

# Teste isolado
if __name__ == "__main__":
    # Escolha um ticker para testar
    ticker = "mypk3"
    print(f"==> Testando com a ação: {ticker}")
    data = get_stock_data(ticker)
    print(f"==> Retorno da função: {data}")
