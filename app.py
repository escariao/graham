import math
import subprocess
from flask import Flask, render_template, request
from requests_crawler import get_stock_data

app = Flask(__name__)

# Chamada de debug: remova essa linha após confirmar os caminhos no ambiente do Render.

def calculate_graham_number(eps, vpa):
    return math.sqrt(22.5 * eps * vpa)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    data_source = None

    if request.method == "POST":
        stock_code = request.form.get("stock_code", "").strip()
        if not stock_code:
            error = "Informe o código da ação."
        else:
            stock_data = get_stock_data(stock_code)
            if not stock_data:
                error = "Erro ao obter dados da ação. Verifique o código e tente novamente."
            else:
                eps = stock_data["eps"]
                vpa = stock_data["vpa"]
                current_price = stock_data["current_price"]
                graham_number = calculate_graham_number(eps, vpa)

                if current_price < graham_number:
                    status = "subvalorizada"
                elif current_price > graham_number:
                    status = "sobrevalorizada"
                else:
                    status = "avaliada corretamente"

                result = {
                    "graham_number": round(graham_number, 2),
                    "current_price": current_price,
                    "status": status,
                    "eps": eps,
                    "vpa": vpa
                }
                data_source = "StatusInvest (requests)"

    return render_template("index.html", result=result, error=error, data_source=data_source)

if __name__ == "__main__":
    app.run(debug=True)
