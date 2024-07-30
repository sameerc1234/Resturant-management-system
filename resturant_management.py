class Restaurant:
    def __init__(self):
        self.menu = {
            "Pasta": 150,
            "Burger": 70,
            "Pizza": 140,
            "Salad": 100,
            "Soda": 65
        }
        self.order = []

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: Rs {price:.2f}")

    def take_order(self):
        print("\nEnter the name of the item you want to order. Type 'done' to finish.\n")
        while True:
            choice = input("Item: ").title()
            if choice == "Done":
                break
            elif choice in self.menu:
                self.order.append(choice)
                print(f"{choice} added to order.")
            else:
                print("Item not on menu. Please try again.")

    def calculate_bill(self):
        total = sum(self.menu[item] for item in self.order)
        return total

    def display_bill(self):
        if not self.order:
            print("No items ordered.")
            return
        
        print("\nYour Order:")
        for item in self.order:
            print(f"{item}: Rs{self.menu[item]:.2f}")

        total = self.calculate_bill()
        print(f"Total Bill: Rs{total:.2f}\n")


def main():
    restaurant = Restaurant()
    while True:
        print("Welcome to the Restaurant Management System!")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Bill")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            restaurant.display_menu()
        elif choice == '2':
            restaurant.take_order()
        elif choice == '3':
            restaurant.display_bill()
        elif choice == '4':
            print("Thank you for using the Restaurant Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()