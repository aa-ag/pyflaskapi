############------------ IMPORTS ------------############
from flask import Flask, jsonify


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
@app.route("/")
def home():
    return "Update the url ^"


@app.route("/books", methods=["GET"])
def get_books():
    serialized = {"books": books}
    return jsonify(serialized)


@app.route("/books/<int:uid>", methods=["GET"])



############------------ DRIVER CODE ------------############
