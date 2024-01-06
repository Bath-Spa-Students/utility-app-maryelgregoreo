# importing a table from rich

from rich.console import Console
from rich.table import Table

# variables 

console = Console()
balance = 0
new_balance = 0

# printing the  title 

print("""

░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ▀█▀ ░█▄─░█ ░█▀▀█  ░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ░█▀▀▀ 
─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█─ ░█░█░█ ░█─▄▄  ░█░█░█ ░█▄▄█ ░█─── ░█▀▀█ ░█─ ░█░█░█ ░█▀▀▀ 
──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█  ░█──░█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄
      """)

# the vending machine menu

vendo_machine = {
    'Drinks': {
        'D1': {'name': 'Coke Zero', 'price': 3.00, 'stocks': 9},
        'D2': {'name': 'Iced Tea', 'price': 3.50, 'stocks': 10},
        'D3': {'name': 'Mountain Dew', 'price': 3.00, 'stocks': 8},
        'D4': {'name': 'Capri Sun', 'price': 2.50, 'stocks': 7},
        'D5': {'name': 'Chocolate Milk', 'price': 2.50, 'stocks': 5}
    },
    'Chips': {
        'C1': {'name': 'Doritos', 'price': 3.50, 'stocks': 8},
        'C2': {'name': 'Lays', 'price': 3.50, 'stocks': 9},
        'C3': {'name': 'Spicy Cheetos', 'price': 4.00, 'stocks': 4},
        'C4': {'name': 'Salad Chips', 'price': 3.00, 'stocks': 6},
        'C5': {'name': 'Pringles', 'price': 3.50, 'stocks': 7}
    },
    'Snacks': {
        'S1': {'name': 'Cupcake', 'price': 5.00, 'stocks': 7},
        'S2': {'name': 'Chocolate Chip Cookies', 'price': 4.50, 'stocks': 8},
        'S3': {'name': 'Skyflakes', 'price': 2.50, 'stocks': 6},
        'S4': {'name': 'Cheez-it', 'price': 3.00, 'stocks': 9},
        'S5': {'name': 'Hello Panda', 'price': 4.50, 'stocks': 6}
    }
}

# inserting the menu into a table

# creating the table
def vendo_table(data):
    table = Table()
    table.add_column("Category", style="white")
    table.add_column("Number", style="blue")
    table.add_column("Item", style="magenta")
    table.add_column("Price", style="red")
    table.add_column("Stocks", style="green")

# inserting the items into the table
    for category, items in data.items():
        for key, item in items.items():
            table.add_row(category, key, item['name'], str(item['price']), str(item['stocks']))

    return table


# defining return_change function: allows the user to receive their change after the transaction

def return_change(change):
    if change > 0:
        console.print(f"Returning change AED {change:.2f}")
        return change
    return 0
    

# defining buy function: allows the user to purchase items 

def buy(category, item_number, name, money):
    item = vendo_machine[category][item_number]

    # using if statement to decrease the balance and stock after the purchase
    if money >= item['price'] and item['stocks'] > 0:
        item['stocks'] -= 1
        change = money - item['price']
        console.print(f'Dispensed... {item[name]}!')
        display_stock(item_number)
        # returning the change
        return return_change(change), change
    
    # elif statement to give the option to add more money if the user has insufficient balance
    elif money < item['price']:
        choice = input("Insufficient funds. Do you want to add more money (YES/NO)? ").upper()
        if choice == 'YES':
            money_added = add_money(0)
            if money_added is not None:
                return buy(category, item_number, name, money + money_added)
            else:
                console.print("Transaction canceled due to insufficient funds.")
                return None, 0
        else:
            console.print ("Transaction canceled due to insufficient funds.")
            return None, 0
            
    elif item['stocks'] <= 0:
        console.print("Out of stock!")
        return None, 0
    
    else:
        console.print("Invalid.")
        return None, 0


# defining add_money function: allows the user to add money to the balance
        
def add_money(balance):
    while True:
        try:
            amount = input("Insert money! (q to quit): ")
            if amount.lower() == 'q':
                console.print("Transaction cancelled. Have a nice day!")
                return None

# it prevents users to insert a negative or invalid amount
            amount = float(amount)
            if amount < 0:
                console.print("Please enter a positive amount.")
                continue

            balance += amount
            console.print(f"Added AED {amount:.2f}!")
            return balance

        except ValueError:
            console.print("Invalid input. Please enter a valid amount or 'q' to quit.")


# defining the continue_shopping function: allows the user to continue buying items

def continue_shopping():

    # using while loop to ask the question
    while True:
        choice = input("Do you want to buy more items (YES/NO)? ").upper()
        if choice == 'YES':
            using_vendo_machine()
            break
        elif choice == 'NO':
            console.print("Thank you for using our vending machine! Have a nice day!")
            break
        else:
            console.print("Invalid choice. Please enter YES or NO.")
    

# # defining the using_vendo_machine function: allows the user to choose the item they want to buy

def using_vendo_machine():
    global balance

    # while loop to ask the question on what item to buy
    while True:
        category = input("Enter what you'd like to purchase! (drinks/chips/snacks): ").capitalize()
        item_number = input(f"Enter {category} item number: ").upper()

        # if statements to update the balance after returning the change
        if category in vendo_machine and item_number in vendo_machine[category]:
            returned_change, remaining_balance = buy (category, item_number, 'name', balance)
            if returned_change is not None and remaining_balance > 0:
                balance = remaining_balance
                continue_shopping()
                break
    
        # if statements when the balance is 0 or insufficient
            else:
                console.print("Insufficient funds. Cannot proceed further.")
                break
        else:
            console.print("Invalid category or item number. Please try again.")


# defining the display_stock function: allows the users to see how many stocks the item has left after purchasing

def display_stock(item_number):
    for category in vendo_machine.values():
        for item_key, item_value in category.items():
            if item_key == item_number:
                console.print(f"Remaining stocks for {item_value['name']} is {item_value['stocks']}")

# messages

console.print("Hello!")
console.print("Available items:")
console.print(vendo_table(vendo_machine))

# flow of the program

balance = add_money(balance)
if balance is not None and balance > 0:
    using_vendo_machine()