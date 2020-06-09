from flight_trip import *
from passenger import *


# create a instance for flight_trip
new_flight = Flight_trip(destination='rome', duration='1:00', origin='geneva')

# print(new_flight.destination, new_flight.duration, new_flight.origin)


# new passenger for passenger file
new_passenger = Passengers(f_name='', passport_number='')


# continuously ask for input
while True:
    # input for a new passenger
    input_name = input('enter name for new passenger: ')
    input_passport_number = input('enter passport number for new passenger: ')
    new_passenger.create_name(input_name)
    new_passenger.set_passport_number(input_passport_number)
    print(new_passenger.get_name(), new_passenger.get_passport_number())


    # add passenger as an object
    # new_flight.add_passenger_list(new_passenger)
    # print(new_passenger)

    # add a passenger to the new_flight
    user_input = input('add passenger to flight: ')
    new_flight.add_passenger_list(user_input)
    print(new_flight.destination, new_flight.duration, new_flight.origin, new_flight.passenger_list)

    # add a second passenger to the new_flight
    user_input2 = input('add passenger to flight: ')
    new_flight.add_passenger_list(user_input2)
    print(new_flight.passenger_list)


    # add a passport number to the new_flight
    flight_passport = input('add passport number to flight: ')
    new_flight.add_passport_list(flight_passport)
    print(new_flight.passport_list)

    # add a second passport number to new_flight
    flight_passport2 = input('add passport number to flight: ')
    new_flight.add_passport_list(flight_passport2)
    print(new_flight.passport_list)


    # get the list of passengers
    print(new_flight.get_list_of_passengers())

    # get list of passengers and passport numbers for flight
    print(new_flight.passenger_list, new_flight.passport_list)

    # create a dictionary
    dictionary = dict(zip(new_flight.passenger_list, new_flight.passport_list))
    print(dictionary)

    # change plane to flight_trip
    for flight in flight_trip:
        new_flight
# for passenger in new_flight.passenger_list:
#     print(passenger.get_name())


