# LAB - Class 01

Project: snakes-cafe
Author: Niles Thompson
Links and Resources
[github repo](https://github.com/Niles086/snakes-cafe)
back-end server url (when applicable)
front-end application (when applicable)
Setup
.env requirements (where applicable)
i.e.

PORT - Port Number
DATABASE_URL - URL to the running Postgres instance/db
How to initialize/run your application (where applicable)
e.g. python main.py
How to use your library (where applicable)
Tests
How do you run tests? Just ran the program 
Any tests of note?
Describe any tests that you did not complete, skipped, etc

## code explination

print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type 'quit' **") 
print("**************************************")
## These lines print a welcome message and instructions for the user. It creates a visual separator using asterisks to enhance the display.


categories = ["Appetizers", "Entrees", "Desserts", "Drinks"]
menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}
## Here, two variables categories and menu are defined. categories contains the names of different menu categories, and menu is a dictionary where each category is associated with a list of items.


print("***********************************")
print("** What would you like to order? **")
print("***********************************")
## This section prints a prompt for the user to start entering their order.


order = {}
## Initializes an empty dictionary order to keep track of the user's orders and their counts.


            while True:
                print("\n")
                for category in categories:
                    print(f"{category}\n{'-' * len(category)}")
                    for item in menu[category]:
                        print(item)
                print("\n")
## This part of the code displays the menu to the user. It uses nested loops to iterate over categories and items in each category, printing them in a structured manner.


                user_input = input("> ").capitalize()

                if user_input == "Quit":
                    break

                if user_input not in order:
                    order[user_input] = 1
                else:
                    order[user_input] += 1

                print(f"** {order[user_input]} order{'s' if order[user_input] > 1 else ''} of {user_input} has been added to your meal. **")

## This section takes user input, converts it to title case using capitalize(), and checks if the user wants to quit. If the user input is not in the order dictionary, it adds the item with a count of 1; otherwise, it increments the count. It then prints an acknowledgment of the order.


            print("Your order:")
            for item, count in order.items():
                print(f"{count} order{'s' if count > 1 else ''} of {item}")

## Finally, this part of the code prints the user's final order, iterating over the order dictionary and displaying the count and name of each item.