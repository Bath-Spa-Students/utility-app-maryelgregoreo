# importing a table from rich

from rich.console import Console
from rich.table import Table

# variables 

console = Console()
balance = 0

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

# inserting the menu into the table

# creating the table
def create_combined_table(data):
    table = Table()
    table.add_column ("Category", style = "white")
    table.add_column ("Number", style = "blue")
    table.add_column ("Item", style = "magenta")
    table.add_column ("Price", style = "red")
    table.add_column ("Stocks", style = "green")

# inserting the items into the table
    for category, items in data.items():
        for key, item in items.items():
            table.add_row (category, key, item ['name'], str(item['price']), str(item['stocks']))

    return table

console.print(create_combined_table(vendo_machine))


# defining buy function: allows the user to purchase items 

def buy (category, item_number,name, money):
    item = vendo_machine [category][item_number]

# if statements when buying an item and the message after
    if money >= item ['price'] and item ['stocks'] > 0:
        item['stocks'] -= 1
        change = money - item ['price']
        console.print (f'Purchased: {item[name]}. Your remaining balance is {change:.2f}')
    elif money < item ['price']:
        console.print ("Insufficient funds")
    elif item['stocks'] <= 0:
        console.print ("Out of stock!")
    else:
        console.print("Invalid.")

# defining add_money function: allows the user to add money to the balance

def add_money(balance):
    while True:
        amount = input("Insert money! (q to quit):")
        if amount.lower() == 'q':
            break 

# allows user to add money when the balance is insufficient
        amount = float(amount)
        if amount < 0:
            console.print ("Your remaining balance is 0, insert money! (enter q to quit)")
            continue

        balance += amount
        console.print (f'Added AED{amount:.2f}. Your current balance is AED {balance:.2f}!')
        
print ("Thank you for using, have a nice day!")

console.print(create_combined_table(vendo_machine))

# definfing the function using_vendo_machine: allows the user to choose the item they want to buy

def using_vendo_machine():

# while loop to ask the question on what item to buy
    while True:
        category = input ("Enter what you'd like to purchase! (drinks/chips/snacks):")
        item_number = input ("Enter item number:")
        if category in vendo_machine and item_number in vendo_machine[category]:
            break
    console.print ("Invalid! Please try again.")
    
    return buy (category, item_number, 'name', balance)

# user's balance
balance = add_money (balance)




