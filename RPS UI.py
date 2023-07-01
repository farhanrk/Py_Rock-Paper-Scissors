#importing tkinter the GUI for python
import tkinter as tk

#settings up a GUI object
window = tk.Tk()

#making a label
greeting = tk.Label(text="What do you want bro???")
title = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  
    background="black",
    width=10,
    height=10
)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")

frame1 = tk.Frame(master=window, height=100, width=50, bg="red")
frame1.pack(fill=tk.BOTH)

frame2 = tk.Frame(master=window, height=50, width=50,bg="yellow")
frame2.pack(fill=tk.BOTH)

frame3 = tk.Frame(master=window, height=25, width=50, bg="blue")
frame3.pack(fill=tk.BOTH)
label_b.pack()

frame_a.pack()
frame_b.pack()

entry.pack()
title.pack()
greeting.pack()
button.pack()

window.mainloop()