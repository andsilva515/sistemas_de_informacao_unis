# 🧮 Atividade - Ciclo 4  
## Python + Banco de Dados (Flask + PostgreSQL)

Este projeto faz parte da atividade do **Ciclo 4 da disciplina de Linguagem de Programação**.  
O objetivo é criar uma aplicação **web** em Python para calcular **IMC (Índice de Massa Corporal)** e **armazenar os resultados em um banco de dados PostgreSQL**.

---

## 📁 Estrutura do Projeto

```text
imc_web/
 ├─ app.py                # Backend Flask + Conexão com PostgreSQL
 └─ templates/
     └─ index.html        # Interface web (HTML)

🛠 Tecnologias Utilizadas

Python 3

Flask (Framework Web)

Flask SQLAlchemy (ORM)

PostgreSQL (Banco de Dados)

pgAdmin (Administração do banco)

🗄 Configuração do Banco de Dados

Passos para Testar a Aplicação

Instale as dependências
Dentro da pasta do projeto, execute:

pip install flask flask_sqlalchemy psycopg2-binary


Crie o banco de dados no PostgreSQL
No pgAdmin ou pelo terminal:

CREATE DATABASE imcdb;


Configure a conexão no arquivo app.py
Ajuste a linha:

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usuario:senha@localhost/imcdb"


Execute a aplicação
Entre na pasta imc_web:

python app.py


Abra o navegador e acesse:

http://127.0.0.1:5000/


Use a interface para calcular IMC

Digite nome, altura (cm) e peso (kg)

Clique em Calcular

O resultado será salvo no banco
