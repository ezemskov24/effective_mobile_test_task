from models import Book, Library


def main():
    library = Library()

    while True:
        try:
            answer = int(input('Choose a command by number:\n'
                               '1: Add a book\n'
                               '2: Delete a book\n'
                               '3: Find a book\n'
                               '4: Get all books\n'
                               '5: Change book status\n'
                               '6: Exit\n'
                               'Command: '))
            if answer == 1:
                title = input('Enter the book title: ')
                author = input('Enter the author of the book: ')
                year = input('Enter the year the book was written: ')
                library.add_book(title=title, author=author, year=year)

            elif answer == 2:
                book_id = int(input('Enter the ID of the book you want to delete: '))
                library.delete_book(book_id=book_id)

            elif answer == 3:
                field = input("Search by (title/author/year): ")
                value = input(f"Enter {field}: ")
                found_books = library.find_books(**{field: value})
                if found_books:
                    for book in found_books:
                        print(book)
                else:
                    print('No books yet\n')

            elif answer == 4:
                books = library.get_all_books()

                if books:
                    for book in books:
                        print(book)
                else:
                    print('No books yet\n')

            elif answer == 5:
                book_id = int(input('Enter the ID of the book you want to change status: '))
                print('1: Book in stock\n'
                      '2: The book has been issued')
                users_status = int(input('Please, choose the book status(1 / 2): '))
                if users_status == 1:
                    book_status = True
                elif users_status == 2:
                    book_status = False
                else:
                    print('Incorrect input. Please try again\n')
                library.change_book_status(book_id=book_id, new_status=book_status)

            elif answer == 6:
                print('Have a good day')
                break

            else:
                print('Your answer was wrong. Please choose an answer from the suggested ones\n')

        except Exception:
            print('Incorrect input. Please try again\n')


if __name__ == '__main__':
    main()
