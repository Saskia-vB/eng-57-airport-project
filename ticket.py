from flight_trip import *


class Tickets(Flight_trip):
    def __init__(self,destination, duration, origin, name, price):
        super().__init__()
        self.name = name
        self.price = price
