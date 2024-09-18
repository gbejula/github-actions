import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    
    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print(("You must enter 1, 2, or 3."))
        return play_rps()

    player = int(playerchoice)


    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win.")
    elif player == 2 and computer == 1:
        print("🎉 You win.")
    elif player == 3 and computer == 2:
        print("🎉 You win.")
    elif player == computer:
        print("😮 Tie game!")
    else:
        print("🐍 Python win.")

    print("\nPlay again?")

    playagain = input("\n Y for Yes or \n Q to Quit\n\n")

    if (playagain.lower() == "y"):
        continue
    else:
        print("\n")
        print("Thank you for playing!\n")
        playagain = False

play_rps()

sys.exit("Bye!")