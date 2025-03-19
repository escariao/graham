import subprocess
import os

def detect_browser_paths():
    """
    Tenta detectar os caminhos dos binários do Chromium (ou chromium‑browser) e chromedriver.
    Retorna um dicionário com as chaves "chromium" e "chromedriver" se encontrados, ou None caso não.
    """
    paths = {}
    
    # Tenta encontrar o binário do Chromium usando diferentes comandos
    chromium_cmds = ["which chromium-browser", "which chromium"]
    for cmd in chromium_cmds:
        try:
            output = subprocess.check_output(cmd, shell=True).decode().strip()
            if output:
                paths["chromium"] = output
                break
        except Exception:
            continue
    else:
        paths["chromium"] = None

    # Tenta encontrar o chromedriver
    try:
        output = subprocess.check_output("which chromedriver", shell=True).decode().strip()
        paths["chromedriver"] = output if output else None
    except Exception:
        paths["chromedriver"] = None

    return paths

if __name__ == "__main__":
    detected = detect_browser_paths()
    print("Caminhos detectados:")
    print(f"Chromium: {detected.get('chromium')}")
    print(f"ChromeDriver: {detected.get('chromedriver')}")
    
    # Opcional: definir essas variáveis de ambiente para uso posterior
    if detected.get("chromium"):
        os.environ["CHROMIUM_BINARY"] = detected.get("chromium")
    if detected.get("chromedriver"):
        os.environ["CHROMEDRIVER_PATH"] = detected.get("chromedriver")
