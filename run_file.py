from flight_trip import *
from passenger import *

# create a instance
new_flight = Flight_trip(destination='rome', duration='1:00', origin='geneva')

# new passenger to passenger file
new_passenger = Passengers(name='', passport_number='')
input_name = input('enter name: ')
input_passport_number = input('enter passport input: ')
new_passenger.create_name(input_name)
new_passenger.set_passport_number(input_passport_number)
print(new_passenger.get_name(), new_passenger.get_passport_number())


# add passenger as an object
# new_flight.add_passenger_list(leo)

# add a passenger to the new_flight
user_input = input('add passenger: ')
new_flight.add_passenger_list(user_input)
print(new_flight.destination, new_flight.duration, new_flight.origin, new_flight.passenger_list)

user_input = input('add passenger: ')
new_flight.add_passenger_list(user_input)

# add a passport number to the new_flight
flight_passport = input('add passport: ')
new_flight.add_passenger_list(flight_passport)
print(new_flight.get_passport_list())
# get the list of passengers
print(new_flight.get_list_of_passengers())

#



# for passenger in new_flight.passenger_list:
#     print(passenger.get_name())

