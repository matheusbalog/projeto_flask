from projeto_flask import database, app
from projeto_flask.models import Usuario, Foto

with app.app_context():
    database.create_all()