# Usamos imagem baseada no Debian que já tem o Chrome e o ChromeDriver
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# Diretório da aplicação
WORKDIR /app

# Copia os arquivos para o container
COPY . /app

# Instala dependências do Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Porta usada pelo gunicorn
EXPOSE 10000

# Comando para rodar a aplicação
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]