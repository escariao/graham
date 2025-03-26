
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from detect_paths import detect_browser_paths
import os
import time
from bs4 import BeautifulSoup

def get_stock_data_selenium(stock_code):
    # Detecta os caminhos dos binários
    paths = detect_browser_paths()

    # Debug extra para logs no Render
    print("[CHROMIUM DETECTADO]:", paths.get("chromium"))
    print("[CHROMEDRIVER DETECTADO]:", paths.get("chromedriver"))
    print("[EXISTE CHROMIUM?]", os.path.isfile(paths.get("chromium") or ""))
    print("[EXISTE CHROMEDRIVER?]", os.path.isfile(paths.get("chromedriver") or ""))
    print("[VERIFICANDO FALLBACKS]")
    print("Existe /app/.apt/usr/bin/chromedriver ?", os.path.isfile("/app/.apt/usr/bin/chromedriver"))
    print("Existe /usr/bin/chromedriver ?", os.path.isfile("/usr/bin/chromedriver"))

    # Fallbacks
    fallback_chromium = "/app/.apt/usr/bin/chromium"
    fallback_chromedriver = "/app/.apt/usr/bin/chromedriver"

    chromium_path = paths.get("chromium") if paths.get("chromium") and os.path.isfile(paths["chromium"]) else fallback_chromium
    chromedriver_path = paths.get("chromedriver") if paths.get("chromedriver") and os.path.isfile(paths["chromedriver"]) else fallback_chromedriver

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = chromium_path

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = f"https://statusinvest.com.br/acoes/{stock_code.lower()}"
        driver.get(url)
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

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

if __name__ == "__main__":
    ticker = "mypk3"
    data = get_stock_data_selenium(ticker)
    if data:
        print("Dados extraídos via Selenium:")
        print(data)
    else:
        print("Não foi possível obter os dados via Selenium.")
