
class Aircraft:
    def __init__(self, aircraft_number):
        self.aircraft_number = aircraft_number
        # self.capacity = capacity

    def get_aircraft_number(self):
        return self.__aircraft_number

    def create_aircraft_number(self, new_aircraft_number):
        self.__aircraft_number = new_aircraft_number
        return new_aircraft_number