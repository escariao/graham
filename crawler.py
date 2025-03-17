import requests
from bs4 import BeautifulSoup

def get_stock_data(stock_code):
    """
    Busca os dados de uma ação no StatusInvest.
    
    Parâmetros:
        stock_code (str): Código da ação (por exemplo, 'PETR4').
    
    Retorna:
        dict: Dicionário com os valores extraídos: 'eps', 'vpa' e 'current_price'.
              Retorna None se ocorrer algum erro.
    """
    url = f"https://statusinvest.com.br/acao/{stock_code.lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Erro ao acessar {url}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    
    try:
        # Esses seletores são apenas exemplificativos.
        # Será necessário analisar o HTML da página para ajustar os seletores corretamente.
        
        # Exemplo para extrair o EPS (LPA)
        eps_element = soup.find("span", {"data-test": "earnings-per-share"})
        eps = float(eps_element.text.strip().replace(",", ".")) if eps_element else None
        
        # Exemplo para extrair o VPA
        vpa_element = soup.find("span", {"data-test": "book-value-per-share"})
        vpa = float(vpa_element.text.strip().replace(",", ".")) if vpa_element else None
        
        # Exemplo para extrair o preço atual da ação
        price_element = soup.find("span", {"data-test": "price-value"})
        current_price = float(price_element.text.strip().replace(",", ".")) if price_element else None
        
        return {"eps": eps, "vpa": vpa, "current_price": current_price}
    
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
