############------------ IMPORTS ------------############
from flask import Flask
from app.books.books_blueprint import books_blueprint
from flask_sqlalchemy import SQLAlchemy


############------------ GLOBAL VARIABLE(S) ------------############
db = SQLAlchemy()

############------------ FUNCTION(S) ------------############
def create_app():
    # create a flask app
    app = Flask(__name__)
    # create/config sqlite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://books.db'
    # extend the books_blueprint object 
    # to consume encapsulated functionality
    app.register_blueprint(books_blueprint)
    return app