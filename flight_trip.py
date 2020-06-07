# <user story> as an airport assistant I want to be able to create a flight_trip with a specific destination

class Flight_trip:

    def __init__(self, destination, duration, origin, passenger_list=[]):
        self.destination = destination
        self.duration = duration
        self.origin = origin
        if passenger_list is None:
            passenger_list = []
        self.passenger_list = passenger_list


# create a flight trip with a specific destination

    def flight_destination(self):
        return self.destination

    # store the duration
    def flight_duration(self):
        return self.duration

    def flight_origin(self):
        return self.origin

    # create passenger_list

    def add_passenger_list(self, passenger):
        self.passenger_list.append(passenger)
        return 'passenger added'

    def get_list_of_passengers(self):
        return self.passenger_list





    #
    # def get_passenger_list(self):
    #     new_passenger_list = []
    #     for passenger in self.passenger_list:
    #         new_passenger_list.append(passenger.get_name())
    #     return new_passenger_list

