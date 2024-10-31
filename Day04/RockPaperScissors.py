import random
import ascii

choicesAscii = [ascii.rock, ascii.paper, ascii.scissors]

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print(choicesAscii[playerChoice])

computerChoice = random.randint(0,2)
print(choicesAscii[computerChoice])

if playerChoice >= 3 or playerChoice < 0:
    print("Invalid number")
elif playerChoice == 0 and computerChoice == 2:
    print("You win")
elif playerChoice == 2 and computerChoice == 0:
    print("You lose")
elif playerChoice == computerChoice:
    print("Draw")
elif playerChoice < computerChoice:
    print("You lose")
elif playerChoice > computerChoice:
    print("You win")