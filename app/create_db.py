############------------ IMPORTS ------------############
import sqlite3
from sqlite3 import Error


############------------ GLOBAL VARIABLE(S) ------------############
sql_create_table = """
CREATE TABLE IF NOT EXISTS books (
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL
)
"""


############------------ FUNCTION(S) ------------############
def create_books_db_and_books_table():
    connection = None

    try:
        connection = sqlite3.connect('/Users/aaronaguerrevere/Documents/projects/pyflaskapi/app/books.db')
    except Error as e:
        print(e)
    finally:
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(sql_create_table)
            except Error as e:
                print(e)
            finally:
                print("db & books table created.")
            connection.close()
        else:
            print("something went wrong.")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    create_books_db_and_books_table()