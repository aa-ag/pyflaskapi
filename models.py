############------------ IMPORTS ------------############
from app import db


############------------ CLASS(ES) ------------############
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def serialized(self):
        json = {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }

        return json