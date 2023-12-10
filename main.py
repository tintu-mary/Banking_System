from banking import *

c=Account()
while(True):
  ch=int(input("Welcome to ABC Bank\n1.New User \n2.Existing User\n3.Exit\n Enter your choice: "))
  if ch==1:
      c.create()

  elif ch==2:
       name=input("enter the username")
       if(c.check(name)):

        while(True):
         print("1.View Balance\n2.Withdraw \n3.Deposit\n4.Logout")
         r=int(input("Your Response:"))
         if(r==1):
           c.view_balance(name)
         elif(r==2):
           c.withdraw(name)
         elif(r==3):
           amount=float(input("enter the amount"))
           c.deposit(name,amount)
         elif(r==4):
           exit()
         else:
           print("invalid choice")
  elif ch==3:
    exit()
  else:
   print("Invalid option")
