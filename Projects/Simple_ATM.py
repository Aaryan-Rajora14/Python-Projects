def show_balance(balance):
    print(f"Your current balance is {balance}")
    
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print((f"You have deposited {amount} successfully now your have {balance} in your Account"))
    return balance
    
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print(f"Insufficient funds!! Your Current Balance is {balance}")
    else:
        balance -= amount
        print(f"You have withdrawn {amount} successfully")
        return balance 


balance = int(input("Enter Your Balance: ")) 
while True:
    print("Welcome to ATM\n1. Show Balance\n2. Deposit\n3. Withdraw\n4. Quit\n")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        show_balance(balance) 
    elif ch == 2:
        balance = deposit(balance)
    elif ch == 3:
        balance = withdraw(balance)
    elif ch == 4:
        print("Thanks For using Simple ATM")
        break
    else:
        print("Your Choice is Invalid !! Plesae Enter Valid Choices")