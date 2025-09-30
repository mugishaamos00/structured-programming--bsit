print("Welcome to Dinners Restaurant and Cafe!")
print("Please select from our menu below:\n")

dishes = {
    1: ("Grilled Chicken", 250),
    2: ("Veggie Burger", 180),
    3: ("Pasta Alfredo", 220),
    4: ("Beef Steak", 350),
    5: ("Caesar Salad", 150)
}

drinks = {
    1: ("Fresh Lemonade", 60),
    2: ("Iced Tea", 50),
    3: ("Coffee", 70),
    4: ("Orange Juice", 80),
    5: ("Mineral Water", 40)
}

def print_menu(menu, menu_type):
    print(f"{menu_type}:")
    for num, (item, price) in menu.items():
        print(f"  {num}. {item} - ₹{price}")
    print()

print_menu(dishes, "Dishes")
print_menu(drinks, "Drinks")

order = []
total = 0

while True:
    choice = input("Enter 'd' to order a dish, 'r' for a drink, or 'q' to finish: ").lower()
    if choice == 'q':
        break
    elif choice == 'd':
        try:
            dish_num = int(input("Enter dish number (1-5): "))
            if dish_num in dishes:
                order.append(dishes[dish_num])
                total += dishes[dish_num][1]
                print(f"Added {dishes[dish_num][0]}")
            else:
                print("Invalid dish number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == 'r':
        try:
            drink_num = int(input("Enter drink number (1-5): "))
            if drink_num in drinks:
                order.append(drinks[drink_num])
                total += drinks[drink_num][1]
                print(f"Added {drinks[drink_num][0]}")
            else:
                print("Invalid drink number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid choice.")

print("\n--- Your Bill ---")
for item, price in order:
    print(f"{item:20} ₹{price}")
print(f"\nTotal: ₹{total}")
print("Thank you for dining with us!")