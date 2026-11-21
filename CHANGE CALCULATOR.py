item_name = input("Enter item_name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = quantity * price
print(f"{item_name}, total is k{total:.2f}")
amount_due = float(f"{total:.2f}")
amount_paid = float(input("Enter amount_paid: "))
change = (amount_paid) - (amount_due)