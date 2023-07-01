#importing tkinter the GUI for python and random for randomizing pc moves
import tkinter as tk
import random
from PIL import ImageTk, Image


#defining the function for the game to work
def rps(theCHOICE, theBOTpicks):
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


#setting up a GUI object
window = tk.Tk()

# Configure rows and columns to stretch
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)

# Create the label with big fonts
title_label = tk.Label(window, text="Title with big fonts", font=("Arial", 16))
title_label.grid(row=0, column=0, sticky="nsew")

# Create a section to display GIF files
gif_frame = tk.Frame(window, bg="gray", padx=10, pady=10)
gif_frame.grid(row=1, column=0, sticky="nsew")

# Load and animate the GIF
gif_image = Image.open("rock.gif")
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(gif_image.copy()))
        gif_image.seek(len(frames))  # Move to the next frame
except EOFError:  # Reached the end of the frames
    pass

# Create the label to display the GIF
gif_label = tk.Label(gif_frame)
gif_label.pack()

# Function to animate the GIF frames
def animate_gif(frame_index):
    gif_label.config(image=frames[frame_index])
    window.after(50, animate_gif, (frame_index + 1) % len(frames))  # Delay in milliseconds

# Start animating the GIF
animate_gif(0)

# Create the label for the current state of the Arena
state_label = tk.Label(window, text="Current state of the Arena", font=("Arial", 12))
state_label.grid(row=2, column=0, sticky="nsew")

# Create the label for the winner
winner_label = tk.Label(window, text="Winner", font=("Arial", 12))
winner_label.grid(row=3, column=0, sticky="nsew")

# Create the buttons for Rock, Paper, and Scissors
buttons_frame = tk.Frame(window)
buttons_frame.grid(row=4, column=0, sticky="nsew")

rock_button = tk.Button(buttons_frame, text="Rock")
rock_button.pack(side="left", expand=True, fill="both")

paper_button = tk.Button(buttons_frame, text="Paper")
paper_button.pack(side="left", expand=True, fill="both")

scissors_button = tk.Button(buttons_frame, text="Scissors")
scissors_button.pack(side="left", expand=True, fill="both")

# Create the Strike button
strike_button = tk.Button(window, text="Strike", font=("Arial", 12))
strike_button.grid(row=5, column=0, sticky="nsew")

# Create the Quit button
quit_button = tk.Button(window, text="Quit", font=("Arial", 12))
quit_button.grid(row=6, column=0, sticky="nsew")


#making a label
# greeting = tk.Label(text="What do you want bro???")
# title = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  
#     background="black",
#     width=10,
#     height=10
# )
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# entry = tk.Entry(fg="yellow", bg="blue", width=50)

# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()

# label_b = tk.Label(master=frame_b, text="I'm in Frame B")

# frame1 = tk.Frame(master=window, height=100, width=50, bg="red")
# frame1.pack(fill=tk.BOTH)

# frame2 = tk.Frame(master=window, height=50, width=50,bg="yellow")
# frame2.pack(fill=tk.BOTH)

# frame3 = tk.Frame(master=window, height=25, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH)
# label_b.pack()

# frame_a.pack()
# frame_b.pack()

# entry.pack()
# title.pack()
# greeting.pack()
# button.pack()

window.mainloop()