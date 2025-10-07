# Part A

#The break statement exits the loop entirely when a certain condition is met.
#e.g

for i in range (1, 6):
    if i == 5:
        break     # Stop the loop when i is 5
    print(i)


#The continue statement skips the current iteration and moves to the next
# iteration of the loop when a certain condition is met
#e.g

for i in range(1, 6):
    if i == 3:
        continue  # Skip when i is 3
    print(i)    

#Par B

def sum_if_integers(a, b, c, d):
    if all(isinstance(x, int) for x in [a, b, c, d]):
        return a + b + c + d
    else:
        return False

#PART C

clients = []
total_profit = 0

for i in range(5):
    print(f"\nEnter data for client {i+1}:")
    name = input("Client name: ")
    loan_amount = float(input("Loan amount: "))
    duration = int(input("Duration in days: "))
    interest = 0.005 * loan_amount * duration
    amount_payable = loan_amount + interest
    clients.append((name, amount_payable, interest))
    total_profit += interest

print("\nAmount payable for each client:")
for client in clients:
    print(f"{client[0]}: Amount Payable = {client[1]:.2f}, Profit = {client[2]:.2f}")

print(f"\nTotal profit from all clients: {total_profit:.2f}")