from random import randint
from os import system

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Customer (Person):
    def __init__(self, first_name, last_name, account_number, balance):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance
    
    def __str__(self):
        return (f"Account Owner: {self.first_name} {self.last_name} Account Number: {self.account_number}  Account Balance: ${self.balance}")

    def Deposit(self):
        amount_deposit = int(input("How much would you like to deposit: "))
        self.balance += amount_deposit
        print(f" ${amount_deposit} successfully added to your account")
        print(f" Your current balance is: ${self.balance}")
        input("Press Enter to return to the main menu")

    def Withdraw(self):
        while True:
            amount_withdraw = int(input("How much would you like to withdraw: "))

            if self.balance - amount_withdraw > 0:
                self.balance -= amount_withdraw
                print(f"${amount_withdraw} successfully withdrawn from your account" )
                print(f" Your current balance is: ${self.balance}")
                input("Press Enter to return to the main menu")
                break
            else:
                print(f"Your account balance is: ${self.balance}, the amount you requested is ${amount_withdraw} ")
                print(f"You have insufficient funds to complete this transaction")
                user_action = input("Press 'x' to return to the main menu or press 'Enter' to try a new amount: ")
                if user_action == 'x':
                    break
                else:
                    system("cls")
# MAIN
def create_client():
    print("Customer Create Mode")
    first_name = input("Please enter your first name: ")
    last_name = input ("Please enter your last name: ")
    initial_deposit = int(input ("Enter the amount of the initial deposit: "))
    account_number = randint(100000, 999999)
    customer = Customer(first_name, last_name, account_number, initial_deposit)
    system("cls")
    return customer

def banking_loop():
    user_choice = 0
    print("Welcome to Class test bank")
    print("Lets create a test customer object")
    customer = create_client()
    print("Customer created")
    print("Lets test the test customer object")
    while user_choice != 3:
        print(customer)
        print("Menu:")
        print("1 : Deposit")
        print("2 : Withdraw")
        print("3 : Exit")
        user_choice = int(input("Please choose 1, 2 or 3: "))
        if user_choice == 1:
            customer.Deposit()
            system("cls")
        elif user_choice == 2:
            customer.Withdraw()
            system("cls")
        elif user_choice== 3:
            exit("Exit Program")
        else:
            print("Please make a valid selection")
            print("Press Enter to return try again")
            system("cls")
            
banking_loop()
