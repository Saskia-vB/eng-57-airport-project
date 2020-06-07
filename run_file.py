from flight_trip import *
from passenger import *
new_flight = Flight_trip(destination='rome', duration='1:00', origin='geneva')

# new passenger
leo = Passengers(name='Lola', passport_number='')
print(leo.name, leo.set_passport_number(new_passport_number='65432'))

# user_input = str(input())

new_flight.add_passenger_list(leo)
# new_flight.get_list_of_passengers(user_input)

print(new_flight.destination, new_flight.duration, new_flight.origin, new_flight.passenger_list)


for passenger in new_flight.passenger_list:
    print(passenger.get_name())

