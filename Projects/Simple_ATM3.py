class centralbank:
    def show_balance(balance):
        print(f"Your current balance is {balance}")

    def deposit(balance):
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"You have deposited {amount} successfully. Now you have {balance} in your account.")
        return balance

    def withdraw(balance):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print(f"Insufficient funds! Your current balance is {balance}.")
        else:
            balance -= amount
            print(f"You have withdrawn {amount} successfully. Now you have {balance} in your account.")
        return balance

D = centralbank
class localbank(centralbank):
    def add_customer(customers):
        account_number = input("Enter the account number: ")
        name = input("Enter the customer's name: ")
        while True:
            pin = input("Enter the 4-digit PIN: ")
            if len(pin) == 4 and pin.isdigit():
                break
            else:
                print("Invalid PIN! Please enter a 4-digit PIN.")
        address = input("Enter the address: ")
        while True:
            phone_number = input("Enter the 10-digit phone number: ")
            if len(phone_number) == 10 and phone_number.isdigit():
                break
            else:
                print("Invalid phone number! Please enter a 10-digit phone number.")
        customers[account_number] = {
            'name': name,
            'pin': pin,
            'address': address,
            'phone_number': phone_number,
            'balance': 0.0}
        
        print(f"Customer {name} added successfully with account number {account_number}.")


    def check_customer(customers):
        account_number = input("Enter the account number: ")
        if account_number in customers:
            customer = customers[account_number]
            pin = input("Enter the PIN: ")
            if pin == customer['pin']:
                print(f"Customer {customer['name']} has a balance of {customer['balance']}.")
                while True:
                    print("\n1. Show Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check Full Details")
                    print("5. Quit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        D.show_balance(customer['balance'])
                    elif choice == 2:
                        customer['balance'] = D.deposit(customer['balance'])
                    elif choice == 3:
                        customer['balance'] = D.withdraw(customer['balance'])
                    elif choice == 4:
                        print(f"Full details of customer {customer['name']}:")
                        print(f"Account Number: {account_number}")
                        print(f"Name: {customer['name']}")
                        print(f"PIN: {customer['pin']}")
                        print(f"Address: {customer['address']}")
                        print(f"Phone Number: {customer['phone_number']}")
                        print(f"Balance: {customer['balance']}")
                    elif choice == 5:
                        print("Returning to main menu.")
                        break
                    else:
                        print("Invalid choice! Please enter a valid option.")
            else:
                print("Incorrect PIN! Access denied.")
        else:
            print(f"Customer with account number {account_number} not found.")

W = localbank
customers = {}
while True:
    print("\nWelcome to ATM")
    print("1. Add New Customer")
    print("2. Check Existing Customer")
    print("3. Quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        W.add_customer(customers)
    elif choice == 2:
        W.check_customer(customers)
    elif choice == 3:
        print("Thanks for using Simple ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option.")