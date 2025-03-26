# Imagem base com Python
FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y chromium chromium-driver && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Define variáveis de ambiente do Chrome
ENV CHROMIUM_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver

# Define diretório da aplicação
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta
EXPOSE 10000

# Comando para rodar a app com gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]