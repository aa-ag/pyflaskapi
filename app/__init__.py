############------------ IMPORTS ------------############
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


############------------ GLOBAL VARIABLE(S) ------------############
db = SQLAlchemy()

############------------ FUNCTION(S) ------------############
def create_app():
    from app.books.books_blueprint import books_blueprint
    # create a flask app
    app = Flask(__name__)
    # create/config sqlite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    # set track modifications to False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # extend the books_blueprint object 
    # to consume encapsulated functionality
    app.register_blueprint(books_blueprint)
    # initialize database
    db.init_app(app)
    return app