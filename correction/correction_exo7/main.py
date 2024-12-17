from src.Order import Order
from src.User import User
from src.Product import Product
from src.Invoice import Invoice
import sys
from datetime import datetime

User.load()
Product.load()
Invoice.load()
Order.load()

def save():
    print("Saving...")
    Order.save()
    User.save()
    Product.save()
    Invoice.save()

def exit():
    save()
    print("Exiting...")
    sys.exit(0) # to kill the program

def help():
    print("Available commands:")
    for command, details in commands.items():
        print(f"{command}: {details['help']}")

commands = {
    "save": {"func": save, "help": "Save all changes to CSV files"},
    "exit": {"func": exit, "help": "Exit the program"},
    "help": {"func": help, "help": "Show this help message"},
    "create_order": {"func": Order.command_create_orders, "help": "Create a new order"},
    "create_user": {"func": User.command_create_user, "help": "Create a new user"},
    "create_product": {"func": Product.command_create_product, "help": "Create a new product"},
}

while True:
    print("-"*20)
    command = input("Enter a command: ")
    if command in commands:
        try:
            commands[command]['func']()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid command")