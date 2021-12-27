############------------ IMPORTS ------------############
from flask import Flask
from app.books.books_blueprint import books_blueprint


############------------ FUNCTION(S) ------------############
def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_blueprint)
    return app