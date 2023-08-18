import random

def check(comp, user):
    if comp == user:
        return 0
    if (comp == 0 and user == 1):
        return -1
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 0):
        return -1
    
    return 1

while True:
    comp = random.randint(0, 2)
    user = int(input("0 for Rock, 1 for Paper, and 2 for Scissors. Enter your choice: "))
    
    if user < 0 or user > 2:
        print("Invalid input. Please enter a valid choice.")
        continue
    
    score = check(comp, user)
    
    
    
    
    print("You:", user)
    print("Computer:", comp)

    if score == 0:
        print("It's a draw!")
    elif score == -1:
        print("You lose!")
    else:
        print("You win!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
 