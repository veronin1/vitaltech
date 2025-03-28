from tkinter import *
import tkinter as tk

# Create window
master = Tk()

# Create an expandable frame
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

b1 = Button(pane, text = "Button")
b1.pack(fill = BOTH, expand = True)

master.mainloop()

