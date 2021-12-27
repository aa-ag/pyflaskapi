############------------ IMPORTS ------------############
from flask import Flask, Blueprint, jsonify, request


############------------ GLOBAL VARIABLE(S) ------------############
books_blueprint = Blueprint("books_blueprint", __name__, url_prefix="/books")

books_store = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "Author 1"
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Author 2"
    },
    {
        "id": 3,
        "title": "Book 3",
        "author": "Author 3"
    }
]


############------------ ENDPOINT(S) ------------############
### GET #####################################################
@books_blueprint.route("", methods=["GET"])
def get_books():
    serialized = {"books": books_store}
    return jsonify(serialized)


@books_blueprint.route("<int:uid>", methods=["GET"])
def get_book(uid):
    requested_book = next(book for book in books_store if book["id"] == uid)
    return jsonify(requested_book)


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

    new_book = {
        "id": books_store[-1]["id"] + 1,
        "title": book_title,
        "author": book_author,
    }

    books_store.append(new_book)

    serialized = {
        "books": books_store
    }

    return jsonify(serialized)