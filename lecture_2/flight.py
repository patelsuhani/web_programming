class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        # list to store the passengers
        self.passengers = []

    # method/function to add passengers
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    
# instantiate the class
flight = Flight(3)

people = ["Alice", "Bob", "Charlie", "David"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to the flight successfully.")
    else:
        print(f"No available seats for {person}.")