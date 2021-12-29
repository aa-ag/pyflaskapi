############------------ IMPORTS ------------############
from flask import Flask, Blueprint, json, jsonify, request
from app import db
from models import Book

############------------ GLOBAL VARIABLE(S) ------------############
books_blueprint = Blueprint("books_blueprint", __name__, url_prefix="/books")


############------------ ENDPOINT(S) ------------############
### GET #####################################################
@books_blueprint.route("", methods=["GET"])
def get_books():
    books_store = Book.query.all()
    serialized_books = [book.serialized() for book in books_store]
    serialized = {"books": serialized_books}
    return jsonify(serialized)


@books_blueprint.route("<int:uid>", methods=["GET"])
def get_book(uid):
    requested_book = Book.query.get(uid)
    return jsonify(requested_book.serialized())


### POST ####################################################
@books_blueprint.route("", methods=["POST"])
def post_book():
    request_json = request.get_json()

    try:
        book_title = request_json["title"]
    except KeyError:
        return "Please provide a title", 400

    try:
        book_author = request_json["author"]
    except KeyError:
        return "Please provide an author", 400

    books_store = Book.query.all()
    titles = [book.serialized()["title"] for book in books_store]

    if book_title in titles:
        return "Title already exists", 400
    else:
        new_book = Book(
                        title=book_title,
                        author=book_author
                    )

        db.session.add(new_book)
        db.session.commit()

        return jsonify(new_book.serialized())

### PUT #####################################################
@books_blueprint.route("<int:uid>", methods=["PUT"])
def put_book(uid):
    # find book in db by id
    requested_book = Book.query.get(uid)

    # have json object from input
    request_json = request.get_json()

    try:
        book_title = request_json["title"]
    except KeyError:
        return "Please provide a title", 400

    try:
        book_author = request_json["author"]
    except KeyError:
        return "Please provide an author", 400

    # update book found by id
    requested_book.title = book_title
    requested_book.author = book_author

    # add changes to session and save them to the db
    db.session.add(requested_book)
    db.session.commit()

    # show updated version of the book
    return jsonify(requested_book.serialized())