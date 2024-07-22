import os
import json


class Book:
    """
    Represents a book with attributes such as book ID, title, author, year of publication, and status.

    Attributes:
        book_id (int): Unique identifier for the book.
        title (str): Title of the book.
        author (str): Author of the book.
        year (int): Year of publication.
        status (bool): Status of the book (True for in stock, False for issued). Default is True.
    """
    def __init__(self, book_id, title, author, year, status=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return (f"Id: {self.book_id}, "
                f"title: {self.title}, "
                f"author: {self.author}, "
                f"year: {self.year}, "
                f"status: {self.status}")


class Library:
    """
    Manages a collection of Book instances, including loading from and saving to a JSON file.

    Attributes:
        library_file (str): Path to the JSON file that stores the library data. Default is 'library.json'.
        books (list): List of Book instances in the library.
    """
    def __init__(self, library_file='library.json'):
        self.library_file = library_file
        self.books = self.load_books()

    def load_books(self):
        """
        Loads books from the JSON file.

        Return:
            list: List of Book instances.
        """
        if os.path.exists(self.library_file):
            with open(self.library_file, 'r', encoding='utf-8') as file:
                return [Book(**book) for book in json.load(file)]
        return []

    def save_books(self):
        """
        Saves the current list of books to the JSON file.
        """
        with open(self.library_file, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def generate_book_id(self):
        """
        Generates a new unique book ID.

        Return:
            int: New unique book ID.
        """
        return max((book.book_id for book in self.books), default=0) + 1

    def add_book(self, title, author, year):
        """
        Adds a new book to the library.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            year (int): Year of publication.
        """
        book_id = self.generate_book_id()
        new_book = Book(book_id=book_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()

        print(f'New book added. Id: {book_id}\n')

    def delete_book(self, book_id):
        """
        Deletes a book from the library by its ID.

        Args:
            book_id (int): Unique identifier of the book to be deleted.
        """
        book_to_delete = next((book for book in self.books if book.book_id == book_id), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books()
            print(f'Book with Id {book_id} deleted\n')
        else:
            print(f'Book with Id {book_id} not found\n')

    def find_books(self, **kwargs):
        """
        Finds books that match the given criteria.

        Args:
            **kwargs: Key-value pairs of attributes to match.

        Return:
            list: List of matching Book instances.
        """
        all_books = self.books
        for key, value in kwargs.items():
            all_books = [book for book in all_books if getattr(book, key, None) == value]
        return all_books

    def get_all_books(self):
        """
        Retrieves all books in the library.

        Return:
            list: List of Book instances.
        """
        return self.books

    def change_book_status(self, book_id, new_status):
        """
        Changes the status of a book.

        Args:
            book_id (int): Unique identifier of the book.
            new_status (bool): New status of the book.
        """
        current_book = next((book for book in self.books if book.book_id == book_id), None)
        if current_book:
            current_book.status = new_status
            self.save_books()
            if new_status is True:
                status_text = 'in stock'
            else:
                status_text = 'has been issued'

            print(f'Book with Id {book_id} changed status to "{status_text}"\n')
        else:
            print(f'Book with Id {book_id} not found\n')
