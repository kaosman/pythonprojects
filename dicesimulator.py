import random

print("Welcome to the dice simulator program")
userChoice = "y"

def rollDice():
    print("You just rolled: ")
    print(random.randint(1,6))

while(userChoice == "y" or userChoice == "Y"):
    userChoice = input("Do you want to roll the dice? Enter 'y' to play and and 'n' to quit ")
    if (userChoice == "n" or userChoice == "N"):
        print("Thank you for playing, bye!")
        break
    else:
        rollDice()


