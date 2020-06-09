from repository import Repository


class BookService:

    legajo_counter = 1

    def __init__(self):
        pass

    def add_book(self, book):
        book.legajo = BookService.legajo_counter
        Repository.booksList[BookService.legajo_counter] = book.__dict__
        BookService.legajo_counter += 1
        return book.legajo

    def update_book(self, book_key, updatedBook):
        try:
            if book_key == 0 or book_key > BookService.legajo_counter:
                raise KeyError
            Repository.booksList[book_key] = updatedBook.__dict__
        except KeyError:
            raise ValueError

    def assign_book(self, book_key, member_legajo):
        try:
            if book_key == 0 or book_key > BookService.legajo_counter:
                raise KeyError
            book = Repository.booksList[book_key]
            book["memberLegajo"] = member_legajo
        except KeyError:
            raise ValueError
