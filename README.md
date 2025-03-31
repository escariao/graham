Análise de Ações com Número de Graham
=====================================

Aplicação web simples que permite analisar ações da bolsa brasileira usando a fórmula do Número de Graham,
com dados atualizados via brapi.dev (https://brapi.dev).

📘 O que é o Número de Graham?
------------------------------
Benjamin Graham, mentor de Warren Buffett, propôs a seguinte fórmula:

  Número de Graham = √(22.5 × EPS × VPA)

- EPS = Lucro por Ação
- VPA = Valor Patrimonial por Ação

🚀 Funcionalidades
------------------
- Consulta de ações por código (ex: PETR4, VALE3)
- Cálculo automático do Número de Graham
- Classificação: subvalorizada, sobrevalorizada ou avaliada corretamente
- Dados em tempo real via brapi.dev
- Totalmente compatível com Render.com

📂 Estrutura do projeto
-----------------------
.
|-- app.py              -> Lógica principal Flask
|-- brapi_crawler.py    -> Comunicação com a API brapi.dev
|-- requirements.txt    -> Dependências
|-- .env                -> Token da API (NÃO subir ao GitHub)
|-- templates/
    |-- index.html      -> Interface HTML

⚙️ Como rodar localmente
------------------------
1. Clone o repositório:
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo

2. Crie o arquivo `.env` com sua chave:
   BRAPI_TOKEN=sua_chave_aqui

3. Instale as dependências:
   pip install -r requirements.txt

4. Rode a aplicação:
   python app.py

🌐 Deploy no Render
-------------------
- Start command: gunicorn app:app
- Environment Variable: BRAPI_TOKEN=sua_chave
- Acesso: https://nome-do-projeto.onrender.com

📄 Licença
----------
MIT — Sinta-se livre para usar e modificar.

✨ Créditos
----------
Desenvolvido por Andrey Escarião  
Online em https://graham-j01n.onrender.com
