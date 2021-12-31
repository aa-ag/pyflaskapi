############------------ IMPORTS ------------############
import unittest
from models import Book


############------------ FUNCTION(S) ------------############
class BookTest(unittest.TestCase):
    def creating_book(self):
        test_book_title = 'Test Title'
        test_book_author = 'Test Author'
        test_book = Book(test_book_title, test_book_author)
        self.assertEqual(test_book.title, test_book_title)
