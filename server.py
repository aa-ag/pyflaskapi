############------------ IMPORTS ------------############
from flask import Flask, jsonify, request


############------------ GLOBAL VARIABLE(S) ------------############
app = Flask(__name__)

books = [
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

############------------ FUNCTION(S) ------------############
### HOME ####################################################
@app.route("/")
def home():
    return "Update the url ^"


### GET #####################################################
@app.route("/books", methods=["GET"])
def get_books():
    serialized = {"books": books}
    return jsonify(serialized)


@app.route("/books/<int:uid>", methods=["GET"])
def get_book(uid):
    requested_book = next(book for book in books if book["id"] == uid)
    return jsonify(requested_book)


### POST ####################################################
@app.route("/books", methods=["POST"])
def post_book():
    request_json = request.get_json()

    book_title = request_json["title"]
    book_author = request_json["author"]

    new_book = {
        "id": books[-1]["id"] + 1,
        "title": book_title,
        "author": book_author,
    }

    books.append(new_book)

    serialized = {
        "books": books
    }

    return jsonify(serialized)