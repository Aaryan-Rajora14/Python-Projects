import random

a = random.randint(1,100)
def num(n):
    if a==n:
        print(f"You Guessed The correct Number {a} in {g} Guesses")
    else: 
        if n>a:
            print("Your Number Is Greater than Acutal Number")
        else:
            print("Your Number is Smaller than Actual Number")

n = None
g = 0
while n!=a:
    n = int(input("Guess The Number: "))
    g += 1
    num(n)
