from flight_trip import *
from passenger import *
new_flight = Flight_trip(destination='rome', duration='1:00', origin='geneva', passenger_list='hi')

user_input = input()
new_flight.get_passenger_list(user_input)
print(new_flight.destination, new_flight.duration, new_flight.origin, new_flight.get_passenger_list())
#
# new_passenger = Passengers(name='Lola', passport_number='')
# print(new_passenger.name, new_passenger.set_passport_number(new_passport_number='65432'))