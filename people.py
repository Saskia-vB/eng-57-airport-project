
class People:
    def __init__(self, name, tax_number):
        self.name = name
        self.__tax_number = tax_number

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
        return new_name

    def get_tax_number(self):
        return self.__tax_number

    def set_tax_number(self, new_tax_number):
        self.__tax_number = new_tax_number
        return new_tax_number


