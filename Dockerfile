FROM python:3.11-slim

# Instalar dependências de sistema
RUN apt-get update && \
    apt-get install -y wget gnupg2 ca-certificates fonts-liberation \
    chromium chromium-driver && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Setar variáveis de ambiente (opcional mas ajuda)
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Diretório do app
WORKDIR /app

# Copiar código para dentro do container
COPY . /app

# Instalar dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expor porta que o gunicorn vai escutar
EXPOSE 10000

# Rodar app com gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]