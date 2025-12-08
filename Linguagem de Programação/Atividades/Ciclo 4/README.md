# Atividade - Ciclo 4 - Python + Banco de Dados

Este projeto faz parte da atividade do **Ciclo 4 da disciplina de Linguagem de Programação**. 

O objetivo é criar uma aplicação **web** em Python para calcular **IMC (Índice de Massa Corporal)** e **armazenar os resultados em um banco de dados PostgreSQL**.

---

## Estrutura do Projeto

```text
imc_web/
 ├─ app.py
 └─ templates/
     └─ index.html
```

## Dependências

```bash
pip install flask flask_sqlalchemy psycopg2-binary
```

## Criar o banco no PostgreSQL

No psql (ou pgAdmin), crie o banco:

```bash
CREATE DATABASE imcdb;
```

E um usuário (se ainda não tiver):
```bash
CREATE USER imcuser WITH PASSWORD 'senha123';
GRANT ALL PRIVILEGES ON DATABASE imcdb TO imcuser;
```

## Rodando a aplicação

Dentro da pasta imc_web:

```bash
python app.py
```
Depois acesse no navegador:

```bash
http://127.0.0.1:5000
```
## Observações
- A aplicação cria automaticamente a tabela no banco ao iniciar.
- Os cálculos realizados ficam registrados e podem ser listados na interface.
