class Passengers:

    def __init__(self, name, passport_number):
        self.name = name
        self.__passport_number = passport_number

    def name(self):
        return self.name

    def get_passport_number(self):
        return self.__passport_number

    def set_passport_number(self, new_passport_number):
        self.__passport_number = new_passport_number
        return new_passport_number

