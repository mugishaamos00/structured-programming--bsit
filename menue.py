def show_menu():
    print("Welcome to the Simple Menu!")
    print("1. Matooke - 3000 UGX")
    print("2. Rice    - 2000 UGX")
    print("3. Chappati- 1000 UGX")

def get_order():
    prices = {"Matooke": 3000, "Rice": 2000, "Chappati": 1000}
    order = {}
    for item in prices:
        qty = input(f"How many {item} would you like? ")
        try:
            qty = int(qty)
        except ValueError:
            qty = 0
        order[item] = qty
    return order, prices

def print_receipt(order, prices):
    print("\n--- Receipt ---")
    total = 0
    for item, qty in order.items():
        if qty > 0:
            cost = qty * prices[item]
            print(f"{item}: {qty} x {prices[item]} UGX = {cost} UGX")
            total += cost
    print(f"Total: {total} UGX")
    print("Thank you for your order!")

if __name__ == "__main__":
    show_menu()
    order, prices = get_order()
    print_receipt(order, prices)