FROM python:3.11-slim

# Instala Chrome + ChromeDriver e dependências básicas
RUN apt-get update && \
    apt-get install -y wget gnupg2 ca-certificates fonts-liberation curl unzip chromium-driver chromium && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 10000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
