############------------ IMPORTS ------------############
from flask import Flask

from app import books


############------------ FUNCTION(S) ------------############
def create_app():
    from app.books.books_blueprint import books_blueprint
    app = Flask(__name__)
    app.register_blueprint(books_blueprint)