import unittest
from parameterized import parameterized
from book import Book
from bookService import BookService
from repository import Repository
from member import Member
from memberService import MemberService


class TestBook(unittest.TestCase):

    # *************************
    # ****** Book *************
    # *************************
    def test_constructor_vacio(self):
        book = Book()
        self.assertDictEqual(book.__dict__, {'_name': '',
                                             '_authorName': '',
                                             '_memberLegajo': ''})

    def test_uso_property(self):
        book = Book()
        book.name = 'Don Quijote de la Mancha'
        book.authorName = 'Miguel de Cervantes'
        book.memberLegajo = ''
        self.assertDictEqual(book.__dict__,
                             {'_name': 'DON QUIJOTE DE LA MANCHA',
                              '_authorName': 'MIGUEL DE CERVANTES',
                              '_memberLegajo': ''})

    def test_constructor_con_valores_iniciales(self):
        book = Book("El alquimista", "Paulo Coelho", '')
        self.assertDictEqual(book.__dict__,  {'_authorName': 'PAULO COELHO',
                                              '_memberLegajo': '',
                                              '_name': 'EL ALQUIMISTA'})

    # *************************
    # ****** ServicesBook *****
    # *************************
    @parameterized.expand([
        ("El código Da Vinci", "Dan Brown", ''),
        ("Viaje al centro de la Tierra", "Julio Verne", ''),
    ])
    # Agregar un book
    def test_add_book(self, name, authorName, memberLegajo):
        book = Book(name, authorName, memberLegajo)
        bookKey = BookService().add_book(book)
        self.assertDictEqual(Repository.booksList[bookKey], book.__dict__)

    @parameterized.expand([
        ("La vuelta al mundo en 80 días", "Julio Verne", ''),
    ])
    # Modificar un book
    def test_update_book(self, name, authorName, memberLegajo):
        # Creamos book
        book = Book(name, authorName, memberLegajo)
        bookKey = BookService().add_book(book)
        # Modificamos book
        book_update = Book(name + '_udate', authorName
                                + '_udate', memberLegajo)
        BookService().update_book(bookKey, book_update)
        self.assertDictEqual(Repository.booksList[bookKey], book_update
                             .__dict__)

    @parameterized.expand([
        (2222, "Claudio", "Pico", ''),
        (3333, "Juan", "Bautista", ''),
    ])
    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_update_book_value_error(self, id_book, name, authorName,
                                     memberLegajo):
        book = Book(name, authorName, memberLegajo)
        with self.assertRaises(ValueError):
            BookService().update_book(id_book, book)

    # Verificar exeption al modificar un book con un id de book que no existe
    def test_assign_book(self):
        book = Book('Cuentos varios de Charles Dickens', 'Charles Dickens', '')
        book_id = BookService().add_book(book)
        member = Member("Daniel", "Quinteros", 35, 2615956565)
        member_legajo = MemberService().add_member(member)
        BookService().assign_book(book_id, member_legajo)

    # Verificar exeption al modificar book con un id de book que no existe
    def test_assign_book_value_error_for_book(self):
        with self.assertRaises(ValueError):
            BookService().assign_book(2222, 0)().delete_book(222)

    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_assign_book_value_error_for_member(self):
        with self.assertRaises(ValueError):
            BookService().assign_book(0, 222)().delete_book(222)


if __name__ == '__main__':
    unittest.main()
