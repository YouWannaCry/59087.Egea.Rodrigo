import unittest
from parameterized import parameterized
from member import Member
from memberService import MemberService
from repository import Repository


class TestMember(unittest.TestCase):

    # *************************
    # ****** Member ***********
    # *************************
    def test_constructor_vacio(self):
        member = Member()
        self.assertDictEqual(member.__dict__, {'_name': '',
                                               '_surname': '',
                                               '_age': '',
                                               '_phone': ''})

    def test_uso_property(self):
        member = Member()
        member.name = 'Santiago'
        member.surname = 'Fernandez'
        member.age = 24
        member.phone = 2615956565
        self.assertDictEqual(member.__dict__, {'_name': 'SANTIAGO',
                                               '_surname': 'FERNANDEZ',
                                               '_age': 24,
                                               '_phone': 2615956565})

    def test_constructor_con_valores_iniciales(self):
        member = Member("Pedro", "Pico", 30, 2615956565)
        self.assertDictEqual(member.__dict__, {'_name': 'PEDRO',
                                               '_surname': 'PICO',
                                               '_age': 30,
                                               '_phone': 2615956565})

    # *************************
    # *****ServicesMember *****
    # *************************
    @parameterized.expand([
        ("Claudio", "Pico", 30, 2615956565),
        ("Juanx", "Bautista", 15, 2615656545),
    ])
    # Agregar un member
    def test_add_member(self, name, surname, age, phone):
        member = Member(name, surname, age, phone)
        memberKey = MemberService().add_member(member)
        self.assertDictEqual(Repository.membersList[memberKey],
                             member.__dict__)

    @parameterized.expand([
        (1, "Juan", "Bautista", 25, 2615656545),
    ])
    # Modificar un member
    def test_update_member(self, legajo, name, surname, age, phone):
        member = Member(name, surname, age, phone)
        MemberService().update_member(legajo, member)
        self.assertDictEqual(Repository.membersList[legajo],
                             member.__dict__)

    @parameterized.expand([
        (2222, "Claudio", "Pico", 20, 2615111122),
        (3333, "Juan", "Bautista", 25, 2615656545),
    ])
    # Verificar la exeption al modificar un member con un legajo que no existe
    def test_update_member_value_error(self, legajo, name, surname, age,
                                       phone):
        member = Member(name, surname, age, phone)
        with self.assertRaises(ValueError):
            MemberService().update_member(legajo, member)

    # Eliminar un member
    def test_delete_member(self):
        MemberService().delete_member(0)
        self.assertEqual(Repository.membersList.get(0), None)

    # Verificar la exeption al modificar un member con un legajo que no existe
    def test_delete_member_value_error_legajo(self):
        with self.assertRaises(ValueError):
            MemberService().delete_member(222)


if __name__ == '__main__':
    unittest.main()
