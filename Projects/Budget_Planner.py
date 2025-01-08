# Budget planning for a simple Household

def menu():
    print()
    print("="*20,"Budget Planner","="*20)
    print(" "*20,"1.Add Category")
    print(" "*20,"2.Show Summary")
    print(" "*20,"3.Increase Budget")
    print(" "*20,"4.Exit")
    print("__"*28)
    
def add_expense_category(expenses, salary):
    category = input("Enter the expense category: ")
    if category not in expenses:
        expenses[category] = {}
    while True:
        sub_head = input(f"Enter a sub-head for the category '{category}': ")
        amount = float(input(f"Enter the amount for '{sub_head}': "))
        expenses[category][sub_head] = amount
        total_expenses = sum(sum(sub_heads.values()) for sub_heads in expenses.values())
        remaining_balance = salary - total_expenses
        print(f"\nCategory: {category} = {expenses[category]}")
        print(f"Remaining Budget: ₹{remaining_balance}")
        
        more = input("\nDo you want to add another sub-head to this category? (yes/no): ").strip().lower()
        if more == 'no':
            break
        elif more != "yes":
            break
        else:
            print(f'Enter More Expenses in Category of {category}')
     
def display_expenses(expenses, salary):
    total_expenses = 0
    print()
    print('='*60)
    print(" "*20,'Monthly Expense Report')
    print("="*60)
    for category, sub_heads in expenses.items():
        print(f"{category} Expenses:-")
        for sub_head, amount in sub_heads.items():
            print(f"  {sub_head}: ₹{amount}")
            total_expenses += amount
        print()
    balance = salary - total_expenses
    print('-'*60)
    print(f"Total Expenses: ₹{total_expenses}")
    print(f"Remaining Balance: ₹{balance}")
    print('='*60)
     
def increase_salary(salary):
    increase_amount = float(input("Enter the amount to increase your salary: "))
    print(f'Your New Budget is {salary + increase_amount}' )
    return salary + increase_amount

expenses = {}
print('='*60)
salary = float(input("Enter your monthly salary To Begin Budget Planning:: "))
print('='*60)
print()
while True:            
    menu()
    choice = input("\nChoose an option: ")
    if choice == '1':
        add_expense_category(expenses, salary)
    elif choice == '2':
        display_expenses(expenses, salary)
    elif choice == '3':
        salary = increase_salary(salary)
        print(f"New Salary: ₹{salary}")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")