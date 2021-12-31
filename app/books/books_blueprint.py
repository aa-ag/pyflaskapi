############------------ IMPORTS ------------############
from flask import Flask, Blueprint, json, jsonify, request
from app import db
from models import Book
from pprint import pprint


############------------ GLOBAL VARIABLE(S) ------------############
books_blueprint = Blueprint("books_blueprint", __name__, url_prefix="/books")


############------------ ENDPOINT(S) ------------############
### GET #####################################################
@books_blueprint.route("", methods=["GET"])
def get_books():
    books_store = Book.query.all()
    serialized_books = [book.serialized() for book in books_store]
    if len(serialized_books):
        serialized = {"books": serialized_books}
        return jsonify(serialized)
    return "no books here ;)"


@books_blueprint.route("<int:uid>", methods=["GET"])
def get_book(uid):
    requested_book = Book.query.get(uid)
    if requested_book:
        return jsonify(requested_book.serialized())
    return "could not find that book"


### POST ####################################################
@books_blueprint.route("", methods=["POST"])
def create_book():
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


@books_blueprint.route("/create_many", methods=["POST"])
def create_many_books():
    request_json = request.get_json()
    books = request_json["books"]
    count = 0
    books_store = Book.query.all()
    titles = [book.serialized()["title"] for book in books_store]
    already_exists = list()
    
    for book in books:
        try:
            book_title = book["title"]
        except KeyError:
            return "Please provide a title", 400

        try:
            book_author = book["author"]
        except KeyError:
            return "Please provide an author", 400

        if book_title in titles:
            already_exists.append(book_title)
            continue
        else:
            new_book = Book(
                            title=book_title,
                            author=book_author
                        )

            db.session.add(new_book)
            db.session.commit()
            count += 1

    if already_exists:
        return f"Title(s) {already_exists} already exists: created {count} books"
    return f"{count} books created"


### PUT #####################################################
@books_blueprint.route("update/<int:uid>", methods=["PUT"])
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

    books_store = Book.query.all()
    titles = [book.serialized()["title"] for book in books_store]

    if book_title in titles:
        return "Title already exists", 400
    else:
        # update book found by id
        requested_book.title = book_title
        requested_book.author = book_author

        # add changes to session and save them to the db
        db.session.add(requested_book)
        db.session.commit()

        # show updated version of the book
        return jsonify(requested_book.serialized())


### DELETE ##################################################
@books_blueprint.route("delete/<int:uid>", methods=["DELETE"])
def delete_book(uid):
    # find book in db by id
    requested_book = Book.query.get(uid)

    # have json object from input
    request_json = request.get_json()

    if request_json:
        # add changes to session and save them to the db
        db.session.delete(requested_book)
        db.session.commit()

        # show updated version of the book
        return jsonify(requested_book.serialized())
    return "couldn't find that book..."


@books_blueprint.route("purge", methods=["DELETE"])
def purge_books():
    all_books = Book.query.all()

    if len(all_books):
        for book in all_books:
            db.session.delete(book)
            db.session.commit()
        return "all books have been purged"
    return "no books left to purge"