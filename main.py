from login import Login
from parkingoperation import ParkingOperation
from prettytable import PrettyTable
class ParkingApp:
    def __init__(self):
        self.parking_operation = ParkingOperation()
        self.login_system = Login(self.parking_operation)
        self.current_user = None

    def main_page(self):
        while True:
            table = PrettyTable()
            table.field_names = ["No.", "Action"]
            table.add_row(["1", "Login"])
            table.add_row(["2", "Parking Info"])
            table.add_row(["3", "Exit"])
            print("\nUser Panel Menu:")
            print(table)
            choice = input("Choose an option: ")
            if choice == "1":
                self.login_system.login_page()
            elif choice == "2":
                self.parking_operation.display_parking_lot()
            elif choice == "3":
                self.parking_operation.save_data()
                self.login_system.save_data()
                break

    def run(self):
        self.parking_operation.load_data()
        self.login_system.load_data()
        self.main_page()

if __name__ == "__main__":
    app = ParkingApp()
    app.run()
