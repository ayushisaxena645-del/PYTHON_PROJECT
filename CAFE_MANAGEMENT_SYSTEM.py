#Define the menu of restaurant
MENU = {
    'Pizza': 40,
    'Pasta': 30,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}


print("Welcome to the PYTHON CAFE!")
print("Here is the MENU")
print("----------------------------")
print("Pizza: Rs40\nPasta: Rs30\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the first item you want to order: ")
if item_1 in MENU:
    order_total += MENU[item_1] #0 + 50 = 50
    print(f"Youe item {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available in the menu.")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("Enter the second item you want to order: ")
    if item_2 in MENU:
        order_total += MENU[item_2] #50 + 70 = 120
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available in the menu.")
        
print(f"Your total order amount is: Rs{order_total}")
payment_method = input("Enter your payment method (cash/card): ")
if payment_method.lower() == 'cash':
    print("Please pay the amount in cash at the counter.")
elif payment_method.lower() == 'card':
    print("Please insert your card at the counter.")
print("Thank you for visiting PYTHON CAFE! Enjoy your meal!")
print("Please visit again!")