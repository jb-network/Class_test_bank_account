from random import randint
from os import system

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name        
        
class Customer (Person):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def __str__(self):
        return (f"Account Owner: {self.first_name} {self.last_name} Account Number: {self.account_number}  Account Balance: {self.balance}")
    def Deposit(self):
        amount_deposit = input("How much would you like to deposit: ")
        self.balance += amount_deposit
        print(f" {amount_deposit} successfully added to your account")
        print(f" Your current balance is: {self.balance}")
    def Withdraw(self):
        amount_withdraw = input("How much would you like to withdraw: ")
        while True:
            if self.balance - amount_withdraw > 0:
                self.balance -= amount_withdraw
                print(f"{amount_withdraw} successfully withdran from your account" )
                print(f" Your current balance is: {self.balance}")
                break
            else:
                print(f"Your account balance is: {self.balance}, the amount you requested is {amount_withdraw} ")
                print(f"You have insufficient funds to complete this transaction")
                user_action = input("Press x to return to the main menu or press enter to try a new amount")
                if user_action == 'x':
                    break
                else:
                    continue
def create_client():
    print("Customer Create Mode")
    first_name = input("Please enter your first name: ")
    last_name = input ("Please enter your last name: ")
    initial_deposit = input ("Enter the amount of the initial deposit")
    account_number = randint(100000, 999999)
    customer = Customer(first_name, last_name, account_number, initial_deposit)
    return customer

def banking_loop():
    print("Welcome to Class test bank")
    print("Lets create a test customer object")
    customer = create_client()
    print("Customer created")
    print("Lets test the test customer object")
    print("Menu:")
    print("1 : Deposit")
    print("2 : Withdraw")
    print("3 : Exit")
    user_choice = int(input("Please choose 1, 2 or 3: "))
    while user_choice != range(1, 4):
        if user_choice == 1:
            customer.Deposit()
        elif user_choice == 2:
            customer.Withdraw()
        elif user_choice== 3:
            exit("Exit Program")
        else:
            print("Please make a valid selection")
            system("cls")



# MAIN
banking_loop()
# Currently scripting and debugging
