import pickle
import time
from prettytable import PrettyTable
class ParkingOperation:
    def __init__(self):
        self.total_spots = 10
        self.occupied_spots = 0
        self.parking_spots = [None] * self.total_spots
        self.parking_times = [None] * self.total_spots
        self.hourly_rate = 10  # rate per hour

    def add_parking_spot(self):
        """Add one more parking spot."""
        self.total_spots += 1
        self.parking_spots.append(None)
        self.parking_times.append(None)
        print(f"New parking spot added. Total spots: {self.total_spots}")
    
    def save_data(self):
        with open('parking_operation.pkl', 'wb') as file:
            pickle.dump((self.parking_spots, self.parking_times, self.hourly_rate), file)

    def load_data(self):
        try:
            with open('parking_operation.pkl', 'rb') as file:
                self.parking_spots, self.parking_times, self.hourly_rate = pickle.load(file)
                self.occupied_spots = sum(1 for spot in self.parking_spots if spot is not None)
        except FileNotFoundError:
            pass

    def park_car(self, car_number):
        if self.occupied_spots < self.total_spots:
            for i in range(self.total_spots):
                if self.parking_spots[i] is None:
                    self.parking_spots[i] = car_number
                    self.parking_times[i] = time.time()
                    self.occupied_spots += 1
                    return f"Car {car_number} parked at spot {i+1}"
        else:
            return "Parking lot is full"

    def remove_car(self, car_number):
        for i in range(self.total_spots):
            if self.parking_spots[i] == car_number:
                parked_time = time.time() - self.parking_times[i]
                hours_parked = parked_time / 3600
                fee = hours_parked * self.hourly_rate
                self.parking_spots[i] = None
                self.parking_times[i] = None
                self.occupied_spots -= 1
                return f"Car {car_number} left spot {i+1}. Fee: ₹{fee:.2f}"
        return "Car not found in the parking lot"
    
    def display_parking_lot(self):
        print("\nParking Lot Status:")
        table = PrettyTable()
        table.field_names = ["Spots No.", "Car Number", "Parked Time (hrs)"]

        for i in range(self.total_spots):
            car_number = self.parking_spots[i] if self.parking_spots[i] else "Empty"
            if car_number != "Empty":
                parked_time = time.time() - self.parking_times[i]
                hours_parked = parked_time / 3600
                table.add_row([i+1, car_number, f"{hours_parked:.2f}"])
            else:
                table.add_row([i+1, car_number, "N/A"])

        print(table)

    def set_hourly_rate(self, rate):
        self.hourly_rate = rate

        