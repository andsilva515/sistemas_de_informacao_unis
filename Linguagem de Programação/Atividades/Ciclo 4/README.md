# Atividade - Ciclo 4 - Python + Banco de Dados

Workspace atividade ciclo 4 - Linguagem de Programação

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

