from flask import render_template, url_for
from projeto_flask import app


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("meuperfil.html", usuario = usuario)

@app.route("/login")
def login():
    return "Faça login"