from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_stock_data_selenium(stock_code):
    # Configura o Selenium para rodar sem abrir janela (headless)
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"
        driver.get(url)

        # Aguarda um tempo para o JS carregar (ajuste se necessário)
        time.sleep(3)

        # Obtém o HTML final, após o JS
        html = driver.page_source

        # Agora podemos usar BeautifulSoup normalmente
        soup = BeautifulSoup(html, "html.parser")

        # Ajuste os seletores conforme a estrutura do site
        eps_element = soup.find("span", {"data-test": "earnings-per-share"})
        vpa_element = soup.find("span", {"data-test": "book-value-per-share"})
        price_element = soup.find("span", {"data-test": "price-value"})

        if not eps_element or not vpa_element or not price_element:
            return None

        eps = float(eps_element.text.strip().replace(",", "."))
        vpa = float(vpa_element.text.strip().replace(",", "."))
        current_price = float(price_element.text.strip().replace(",", "."))

        return {"eps": eps, "vpa": vpa, "current_price": current_price}

    finally:
        driver.quit()

# Teste isolado
if __name__ == "__main__":
    ticker = "mypk3"
    data = get_stock_data_selenium(ticker)
    if data:
        print(f"EPS: {data['eps']}")
        print(f"VPA: {data['vpa']}")
        print(f"Preço: {data['current_price']}")
    else:
        print("Não foi possível obter os dados via Selenium.")
