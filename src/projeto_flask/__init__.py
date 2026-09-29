from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app.cofig["SQL_DATABASE_URI"] = "sqlite: ///comunidade.db"



app = Flask(__name__)
from projeto_flask import routes
