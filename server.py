############------------ IMPORTS ------------############
from flask import Flask


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
def hello_world():
    return "<p>Hello World</p>"

############------------ DRIVER CODE ------------############
