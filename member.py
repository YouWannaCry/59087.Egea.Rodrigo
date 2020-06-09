class Member:
    def __init__(self, name='', surname='', age='', phone=''):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def legajo(self):
        return self._legajo

    @legajo.setter
    def legajo(self, value):
        self._legajo = value
