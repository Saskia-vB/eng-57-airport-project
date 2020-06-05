# <user story> as an airport assistant I want to be able to create a flight_trip with a specific destination

class Flight_trip:

    def __init__(self, destination, duration, origin, passenger_list=None):
        self.destination = destination
        self.duration = duration
        self.origin = origin
        self.passenger_list = passenger_list
        if passenger_list is None:
            passenger_list = []

# create a flight trip with a specific destination

    def flight_destination(self):
        return self.destination

    # store the duration
    def flight_duration(self):
        return self.duration

    def flight_origin(self):
        return self.origin

    # create passenger_list
    def flight_passenger_list(self):
        return self.flight_passenger_list