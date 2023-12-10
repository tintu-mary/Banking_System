from random import *
class Account:

    def __init__(self):
        self.customer={}
#create a customer bank account
    def create(self):

       user_name=input("User name:")
       balance=float(input("enter the amount you wish to deposit:"))
       acc_no=randint(111111,999999)
       self.customer.update({user_name:{"account_no":acc_no,"Balance":balance}})
       print("Your account is successfully created!!!")
       self.display(user_name)
#check whether the username is already in the dictionary
    def check(self,name):
         if name not in self.customer:
             print("you are not a valid user ,create an account")
             self.create()
         else:
             return(True)
#print the balance of a customer
    def view_balance(self,name):
          print("Balance=",self.customer[name]['Balance'])
#function to withdraw money
    def withdraw(self,name):
        amount = float(input("enter the amount: "))
        if (0 < amount and amount <= self.customer[name]['Balance']):
            self.customer[name]['Balance'] -= amount
            print(f"Amount {amount} withdrawn successfully. Updated balance: {self.customer[name]['Balance']}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
#function to deposit in the account
    def deposit(self,name,amount):
        if amount > 0:
            self.customer[name]["Balance"] += amount
            print(f"Amount {amount} deposited successfully. Updated balance: {self.customer[name]['Balance']}")
        else:
           print("Invalid deposit amount. Please enter a positive value.")


    def display(self,name):

            print((self.customer[name]))
