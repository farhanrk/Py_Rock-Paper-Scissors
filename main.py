import random

input = input("\n\n\nWanna play some Rock Paper Scissors with a bot and see how you fare? (y/n)\n").lower()

if (input == y):
    runGame = True
    while runGame==True:
        input = input("ROCK, PAPER or SCISSORS!? ").lower()
        if (input == "rock" or "r" or "rocks"):
            ##player rocks
            print("player rocks")
        elif (input == "paper" or "p" or "papers"):
            ##player papers
            print("player tries to fling around a paper")
        elif (input == "scissors" or "s" or "scissor"):
            ##player shreds
            print("player SHREDS~~!!")
        else:
            ##invalid input
            print("bruh")
