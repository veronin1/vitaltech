from tkinter import *
import tkinter as tk

"""
7 Inputs - userName, age, height, weight, steps, heartRate, waterIntake
7 Labels - userName, age, height, weight, steps, heartRate, waterIntake
1 Button
"""


# Create window
master = Tk()

# Create an expandable frame
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

b1 = Button(pane, text = "Button", background = "green", fg = "gray30")
b1.pack(fill = BOTH, expand = True)

b1 = Button(pane, text = "Button", background = "PeachPuff3", fg = "gray30")
b1.pack(fill = BOTH, expand = True, padx=100)

master.mainloop()

