############------------ IMPORTS ------------############
from flask import Flask
from app.books.books_blueprint import books_blueprint
from flask_sqlalchemy import SQLAlchemy


############------------ FUNCTION(S) ------------############
def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_blueprint)
    return app