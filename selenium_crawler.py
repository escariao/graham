from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def get_stock_data_selenium(stock_code):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Atualize os caminhos para os binários instalados via apt.txt
    options.binary_location = "/app/.apt/usr/bin/chromium-browser"
    service = Service("/app/.apt/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"
        driver.get(url)
        time.sleep(5)  # aguarda o JavaScript carregar

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        # Ajuste os seletores conforme o HTML renderizado
        eps_element = soup.find("span", {"class": "indicador-lpa"})
        vpa_element = soup.find("span", {"class": "indicador-vpa"})
        price_element = soup.find("span", {"class": "price-value"})

        if not (eps_element and vpa_element and price_element):
            print("Erro: Não foi possível encontrar EPS, VPA ou Preço.")
            return None
        
        eps = float(eps_element.text.strip().replace(",", "."))
        vpa = float(vpa_element.text.strip().replace(",", "."))
        current_price = float(price_element.text.strip().replace(",", "."))

        return {"eps": eps, "vpa": vpa, "current_price": current_price}

    finally:
        driver.quit()

# Teste isolado
if __name__ == "__main__":
    ticker = "mypk3"  # Altere para um ticker de teste conhecido
    data = get_stock_data_selenium(ticker)
    if data:
        print("Dados extraídos via Selenium:")
        print(data)
    else:
        print("Não foi possível obter os dados via Selenium.")
