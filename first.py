menu = {
    "pizza": 40,
    "pasta": 80,
    "burger": 90,
    "coffee": 50,  
    "tea": 20
}

print("Welcome to our PYTHON restaurant")
print("pizza : RS 40\npasta : RS 80\nburger : RS 90\ncoffee : RS 50\ntea : RS 20\n") 

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1.lower() in menu:  
    order_total += menu[item_1.lower()]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Order item {item_1} is not available yet")  

while True: 
    another_order = input("Do you want to order another item? (Yes/No) ")
    if another_order.lower() == "yes": 
        item_2 = input("Enter the name of the next item = ")
        if item_2.lower() in menu:  
            order_total += menu[item_2.lower()]
            print(f"Item {item_2} has been added to order")
        else:
            print(f"Ordered item {item_2} is not available!")

        print(f"The total amount of items to pay is {order_total}")

    elif another_order.lower() == "no": 
        print(f"Your final bill is {order_total}")
        break 
    else:
        print("Invalid input. Please enter Yes or No.") 