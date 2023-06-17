import random


def main():
    doBattle = input("\n\n\nWanna play some Rock Paper Scissors with a bot and see how you fare? (y/n)\n").lower()

    moooves = ["rock","paper","scissors"]
    runGame = True
    if (doBattle == "y"):
        del doBattle 
        while runGame==True:
            theBOTpicks = moooves[random.randint(0,2)]
            theCHOICE = input("ROCK, PAPER or SCISSORS!? ").lower()
            if (theCHOICE == "rock" or theCHOICE == "r" or theCHOICE == "rocks"):
                ##player rocks
                if(theCHOICE == "rocks"):
                    print("You want rocks but the universe only grants you one!")
                else:
                    print("You manifest the power of the earth into a single SOLID ROCK~!")
                if (theBOTpicks=="rock"):
                    print("Your profound ROCK clashes with the ROCK the bot chose, but like the Aesir and the Giants the battle never ends.")
                    print("TIE!")
                elif (theBOTpicks=="scissors"):
                    print("Your ROCK strikes down the frail pair of scissors chosen by the bot like The Spear of Triam stroke down the Titan Kronos!")
                    print("VICTORY!")
                elif (theBOTpicks=="paper"):
                    print("Your ROCK struggles against the durability of the bot's paper, like the God of War Tyr it is forever trapped and ensnared.")
                    print("DEFEAT!")
                else:
                    print("The world ends in confusion!")
            elif (theCHOICE == "paper" or theCHOICE ==  "p" or theCHOICE == "papers"):
                ##player papers
                if(theCHOICE == "papers"):
                    print("You want the power of all the paper in the realms but you only find one worthy of battle!")
                else:
                    print("You manifest the power of nature into one formidable piece of PAPER~!")
                if (theBOTpicks=="paper"):
                    print("Your PAPER swiftly moves in to strike the PAPER from the bot, but paper doesn't work against paper and the battle never starts forget about ending.")
                    print("TIE!")
                elif (theBOTpicks=="rock"):
                    print("Your righteous PAPER entangles and defeats the ROCK chosen by the bot like the Olympians trapping Kronos for eternity.")
                    print("VICTORY!")
                elif (theBOTpicks=="scissors"):
                    print("Your PAPER tries to subdue the ravenous hatred of the bot's SCISSORS, but alas is torn to shreds like Kratos's humanity was by Ares.")
                    print("DEFEAT!")
                else:
                    print("The world ends in confusion!")
            elif (theCHOICE == "scissors" or theCHOICE == "s" or theCHOICE == "scissor"):
                ##player shreds
                if(theCHOICE == "scissor"):
                    print("You gain the power of a single scissor but the universe grands you a pair and now you stand streadfast, ready for battle!")
                else:
                    print("You manifest the power of righteous fury into a razor sharp pair of SCISSORS~!")
                if (theBOTpicks=="scissors"):
                    print("Your SCISSORS clashses with the SCISSORS from the bot, like the battle between the immortals Ilarian and Beleth goes on to be an eternal conflict.")
                    print("TIE!")
                elif (theBOTpicks=="paper"):
                    print("Your righteous SCISSORS shreds through the PAPER chosen by the bot like the ronin Sasaki Kojiro shredded through the 70 Yoshioka samurai.")
                    print("VICTORY!")
                elif (theBOTpicks=="rock"):
                    print("Your SCISSORS throws a fury of slashses against the bot's ROCK, but like Thor's Mjolnir stroke down the Giants, you are down in one hit.")
                    print("DEFEAT!")
                else:
                    print("The world ends in confusion!")
            else:
                ##invalid theCHOICE
                print("The universe is confused by your choice of weapon and throws you out of the arena!")
            del theBOTpicks
            del theCHOICE
            doBattle = input("\n\nWoud you take this fight once again and see how you fare? (y/n)\n").lower()
            if (doBattle=="y"):
                runGame = True
            elif(doBattle=="n"):
                runGame = False
            else:
                print("The realms are confused by your indecisiveness as you disappear into the void!")
                runGame = False
    else:
        print("The realms wonder why you even stepped into the arena when you had no resolve to fight.")

if __name__ == "__main__":
    main()