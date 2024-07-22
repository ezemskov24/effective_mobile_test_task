import unittest
import os

from app.models import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """
        Creates a test library and adds some books for testing.
        """
        self.library = Library(library_file='test_library.json')
        self.library.add_book('Test book 1', 'Test author 1', 2021)
        self.library.add_book('Test book 2', 'Test author 2', 2022)
        self.library.add_book('Test book 3', 'Test author 3', 2023)

    def tearDown(self):
        """
        Removes the test library file after each test.
        """
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')

    def test_add_book(self):
        """
        Test adding a new book to the library.
        """
        self.library.add_book('Test book 4', 'Test author 4', 2004)
        book = self.library.find_books(title='Test book 4')[0]
        self.assertEqual(book.title, 'Test book 4')
        self.assertEqual(book.author, 'Test author 4')
        self.assertEqual(book.year, 2024)
        self.assertEqual(book.status, True)

    def test_delete_book(self):
        """
        Test deleting a book from the library.
        """
        book = self.library.find_books(title='Test book 1')[0]
        self.library.delete_book(book.book_id)
        books = self.library.find_books(title='Test book 1')
        self.assertEqual(len(books), 0)

    def test_find_books(self):
        """
        Test finding books in the library by a given attribute.
        """
        books = self.library.find_books(author='Test author 2')
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'Test book 2')

    def test_get_all_books(self):
        """
        Test retrieving all books from the library.
        """
        books = self.library.get_all_books()
        self.assertEqual(len(books), 3)

    def test_change_status(self):
        """
        Test changing the status of a book
        """
        book = self.library.find_books(title='Test book 3')[0]
        self.library.change_book_status(book.book_id, False)
        book = self.library.find_books(title='Test book 3')[0]
        self.assertEqual(book.status, False)


if __name__ == '__main__':
    unittest.main()
