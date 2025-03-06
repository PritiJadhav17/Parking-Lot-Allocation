import pickle 
from prettytable import PrettyTable
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Login:
    def __init__(self, parking_operation):
        self.users = {
            "admin": User("admin", "admin123", "admin"),
            "user": User("user", "user123", "user")
        }
        self.current_user = None
        self.parking_operation = parking_operation

    def save_data(self):
        with open('users.pkl', 'wb') as file:
            pickle.dump(self.users, file)

    def load_data(self):
        try:
            with open('users.pkl', 'rb') as file:
                self.users = pickle.load(file)
        except FileNotFoundError:
            pass

    def register_user(self, username, password, role):
        """Register a new user."""
        if username in self.users:
            return "Username already exists." 
        else:
            self.users[username] = User(username, password, role)
            self.save_data()
            return f"User {username} registered successfully as {role}."


    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            return f"Welcome, {self.current_user.role} {username}!"
        else:
            return "Invalid username or password"

    def logout(self):
        self.current_user = None
        return "Logged out successfully"

    def login_page(self):
        """Show login page or registration page.""" 
        while True:
            print("\nLogin Page")
            choice = input("Do you have an account? (y/n): ").strip().lower()
            if choice == 'y':
                username = input("Username: ")
                password = input("Password: ")
                print(self.login(username, password))
                if self.current_user:
                    self.redirect_user_based_on_role()
                break
            elif choice == 'n':
                username = input("Choose a username: ")
                password = input("Choose a password: ")
                role = input("Enter role (admin/user): ").strip().lower()
                print(self.register_user(username, password, role))
                break
            else:
                print("Invalid choice. Please enter 'y' for Yes or 'n' for No.")

    def redirect_user_based_on_role(self):
        """Redirect user to their respective page after login."""
        if self.current_user.role == "admin":
            self.admin_page()
        elif self.current_user.role == "user":
            self.user_page()
      
    def admin_page(self):
        while True:
            table = PrettyTable()
            table.field_names = ["No.", "Action"]
            table.add_row(["1", "Display Parking Lot"])
            table.add_row(["2", "Remove Car"])
            table.add_row(["3", "Adjust Hourly Rate"])
            table.add_row(["4", "View Registered Users"])
            table.add_row(["5", "Logout"])
            print("\nUser Panel Menu:")
            print(table)
            choice = input("Choose an option: ")
            if choice == "1":
                self.parking_operation.display_parking_lot()
            elif choice == "2":
                car_number = input("Enter car number to remove: ")
                print(self.parking_operation.remove_car(car_number))
            elif choice == "3":
                new_rate = input("Enter new hourly rate: ")
                self.parking_operation.set_hourly_rate(float(new_rate))
                print(f"Hourly rate updated to (₹){new_rate}/hour")
            elif choice == "4":
                self.display_registered_users()  # Display all users
            elif choice == "5":
                print(self.logout())
                break

    def user_page(self):
        while True:
            table = PrettyTable()
            table.field_names = ["No.", "Action"]
            table.add_row(["1", "Park Car"])
            table.add_row(["2", "Remove Car"])
            table.add_row(["3", "Display Parking Lot"])
            table.add_row(["4", "Logout"])
            print("\nUser Panel Menu:")
            print(table)
            choice = input("Choose an option: ")
            if choice == "1":
                car_number = input("Enter car number: ")
                print(self.parking_operation.park_car(car_number))
            elif choice == "2":
                car_number = input("Enter car number: ")
                print(self.parking_operation.remove_car(car_number))
            elif choice == "3":
                self.parking_operation.display_parking_lot()
            elif choice == "4":
                print(self.logout())
                break

    def display_registered_users(self):
        """Displays all registered users with their roles (Admins only)."""
        if self.current_user and self.current_user.role == "admin":  
            table = PrettyTable()
            table.field_names = ["Username", "Role"]
        
            for username, user in self.users.items():
                table.add_row([username, user.role])

            print("\nRegistered Users:")
            print(table)
        else:
            print("Access denied! Only admins can view registered users.")
        