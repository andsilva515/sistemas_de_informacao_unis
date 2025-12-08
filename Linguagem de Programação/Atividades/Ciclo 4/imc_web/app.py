from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# =================== CONFIGURAÇÃO DO BANCO ===================
# Exemplo de conexão com PostgreSQL (ajuste os dados!):
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://imcuser:senha123@localhost/imcdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =================== MODEL ===================
class PacienteIMC(db.Model):
    __tablename__ = "pacientes_imc"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    endereco = db.Column(db.String(255))
    altura_cm = db.Column(db.Float, nullable=False)
    peso_kg = db.Column(db.Float, nullable=False)
    imc = db.Column(db.Float, nullable=False)
    classificacao = db.Column(db.String(50), nullable=False)
    data_calculo = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PacienteIMC {self.nome} - IMC {self.imc}>"

# Cria as tabelas no banco (apenas na primeira execução)
with app.app_context():
    db.create_all()

# =================== FUNÇÃO DE CÁLCULO ===================
def calcular_imc(altura_cm, peso_kg):
    altura_m = altura_cm / 100
    imc = peso_kg / (altura_m ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return imc, classificacao

# =================== ROTAS ===================
@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = None

    if request.method == "POST":
        nome = request.form.get("nome")
        endereco = request.form.get("endereco")
        altura_str = request.form.get("altura")
        peso_str = request.form.get("peso")

        try:
            altura_cm = float(altura_str.replace(",", "."))
            peso_kg = float(peso_str.replace(",", "."))

            imc, classificacao = calcular_imc(altura_cm, peso_kg)

            registro = PacienteIMC(
                nome=nome,
                endereco=endereco,
                altura_cm=altura_cm,
                peso_kg=peso_kg,
                imc=imc,
                classificacao=classificacao,
            )
            db.session.add(registro)
            db.session.commit()

            mensagem = f"IMC de {nome}: {imc:.2f} ({classificacao}) salvo no banco."

        except ValueError:
            mensagem = "Erro: altura e peso devem ser números."

    # Busca últimos registros para mostrar na tela
    registros = (
        PacienteIMC.query.order_by(PacienteIMC.data_calculo.desc())
        .limit(10)
        .all()
    )

    return render_template("index.html", registros=registros, mensagem=mensagem)


@app.route("/historico")
def historico():
    registros = PacienteIMC.query.order_by(PacienteIMC.data_calculo.desc()).all()
    return render_template("index.html", registros=registros)

# =================== MAIN ===================
if __name__ == "__main__":
    app.run(debug=True)
