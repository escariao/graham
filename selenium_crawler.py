from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

def get_stock_data_selenium(stock_code):
    # Configura o Selenium para rodar sem interface (headless)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Em muitos casos, o Selenium localiza o chromium e o chromedriver
    # sozinho. Se precisar, informe explicitamente:
    options.binary_location = "/usr/bin/chromium"
    
    # O parâmetro executable_path pode ser necessário para o ChromeDriver:
    driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")

    try:
        url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"
        driver.get(url)

        # Aguarde alguns segundos para o JS carregar (ou use WebDriverWait)
        time.sleep(5)

        # Captura o HTML final
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Ajuste os seletores conforme o HTML renderizado
        # Estes são exemplos ilustrativos:
        eps_element = soup.find("span", {"class": "indicador-lpa"})
        vpa_element = soup.find("span", {"class": "indicador-vpa"})
        price_element = soup.find("span", {"class": "price-value"})

        if not eps_element or not vpa_element or not price_element:
            print("Erro: Não foi possível encontrar EPS, VPA ou Preço.")
            return None

        eps = float(eps_element.text.strip().replace(",", "."))
        vpa = float(vpa_element.text.strip().replace(",", "."))
        current_price = float(price_element.text.strip().replace(",", "."))

        return {
            "eps": eps,
            "vpa": vpa,
            "current_price": current_price
        }
    finally:
        driver.quit()

# Teste local (opcional)
if __name__ == "__main__":
    data = get_stock_data_selenium("mypk3")
    print("Retorno:", data)
