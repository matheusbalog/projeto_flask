from flask import render_template, url_for
from projeto_flask import app
from flask_login import login_required

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("meuperfil.html", usuario = usuario)

@app.route("/login")
def login():
    return "Faça login"