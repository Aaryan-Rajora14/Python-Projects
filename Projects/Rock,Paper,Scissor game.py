import random

#Rock Paper Scissors
while True:
    def gameWin(comp, you):
        if comp == you:
            return None

        elif comp == 's':
            if you=='r':
                return False
            elif you=='p':
                return True
        
        elif comp == 'r':
            if you=='p':
                return False
            elif you=='s':
                return True
        
        elif comp == 'p':
            if you=='s':
                return False
            elif you=='r':
                return True

    print("Comp Turn: Scissor(s) Rock(r) or Paper(p)?")
    randNo = random.randint(1, 3) 
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'r'
    elif randNo == 3:
        comp = 'p'

    you = input("Your Turn: Scissor(s) Rock(r) or Paper(p)?").lower().strip()
    a = gameWin(comp, you)

    print(f"Computer chose {comp}")
    print(f"You chose {you}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")