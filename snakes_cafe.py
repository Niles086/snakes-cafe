print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type 'quit' **") 
print("**************************************")

categories = ["Appetizers", "Entrees", "Desserts", "Drinks"]
menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

order = {}
while True:
    print("\n")
    for category in categories:
        print(f"{category}\n{'-' * len(category)}")
        for item in menu[category]:
            print(item)
    print("\n")

    user_input = input("> ").capitalize()

    if user_input == "Quit":
        break

    if user_input not in order:
        order[user_input] = 1
    else:
        order[user_input] += 1

    print(f"** {order[user_input]} order{'s' if order[user_input] > 1 else ''} of {user_input} has been added to your meal. **")

print("Your order:")
for item, count in order.items():
    print(f"{count} order{'s' if count > 1 else ''} of {item}")
