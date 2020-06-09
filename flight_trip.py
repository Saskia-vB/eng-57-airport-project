# <user story> as an airport assistant I want to be able to create a flight_trip with a specific destination

class Flight_trip:

    def __init__(self, flight_number, destination, duration, origin, passenger_list=[], passport_number_list=[]):
        # password = 'flight123'
        # password_input = input('Please enter password: ')
        # if password == password_input:
        self.flight_number = flight_number
        self.destination = destination
        self.duration = duration
        self.origin = origin
        if passenger_list is None:
            passenger_list = []
        self.passenger_list = passenger_list
        if passport_number_list is None:
            passport_number_list = []
        self.passport_number_list = passport_number_list
        # else:
        #     return 'wrong password'

# create a flight

    def get_flight_number(self):
        return self.flight_number

    def create_flight_number(self, new_flight_number):
        self.flight_number = new_flight_number
        return new_flight_number

# create a flight trip with a specific destination

    def flight_destination(self):
        return self.destination

    # store the duration
    def flight_duration(self):
        return self.duration

    def flight_origin(self):
        return self.origin

    # create passenger_list

    def get_passenger_details(self):
        return self.passenger_list, self.passport_number_list

    def add_passenger_details(self, new_passenger, new_passport_number):
        self.passenger_list.append(new_passenger)
        self.passport_number_list.append(int(new_passport_number))
        return self.passenger_list, self.passport_number_list



    # def add_passenger_list(self, passenger):
    #     self.passenger_list.append(passenger)
    #     return 'passenger added'
    #
    # def get_list_of_passengers(self):
    #     return self.passenger_list
    #
    # def add_passport_list(self, passport):
    #     self.passport_list.append(passport)
    #     return 'passport added'
    #
    # def get_passport_list(self):
    #     return self.passport_list


        






