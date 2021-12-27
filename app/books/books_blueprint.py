############------------ IMPORTS ------------############
from flask import Blueprint


############------------ GLOBAL VARIABLE(S) ------------############
books_blueprint = Blueprint("books_blueprint", __name__, url_prefix="/books")