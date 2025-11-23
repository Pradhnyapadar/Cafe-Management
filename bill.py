#Cafe and Menu Python Project
# -------------------------------

# Menu stored as a dictionary
menu = {
    "Coffee": 50,
    "Tea": 30,
    "Cold Coffee": 80,
    "Sandwich": 120,
    "momos": 150,
"Pasta": 180,
    "French Fries": 90
}

# Function to display the menu
def display_menu():
    print("\n------ Welcome to Python Cafe ------")
    print("----------- MENU -----------")
    for item, price in menu.items():
        print(f"{item:15} : ₹{price}")
    print("------------------------------------\n")
#Function to take order
def take_order():
    order_list = []
    total = 0
    
    while True:
        item = input("Enter an item to order (or type 'done' to finish): ")

        if item.lower() == "done":
            break

        if item in menu:
            quantity = int(input("Enter quantity for {item}: "))
    
            cost = menu[item] * quantity
            order_list.append((item, quantity, cost))
            total += cost
   
        else:
            print("Item not in menu. Please try again.")
    
    return order_list, total

# Function to print receipt
def print_receipt(order_list, total):
    print("\n----------- BILL RECEIPT -----------")
    for item, qty, cost in order_list:
        print(f"{item:15} x {qty} = ₹{cost}")
    print("------------------------------------")
    print(f"Total Amount         = ₹{total}")
    print("Thank you for visiting Python Café!")
    print("------------------------------------\n")

# Main program
display_menu()
orders, total_amount = take_order()
print_receipt(orders, total_amount)

