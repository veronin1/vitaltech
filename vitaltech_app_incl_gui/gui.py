from tkinter import *
import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk() # Creates window
        self.root.geometry("450x600") # Sets window size 
        self.root.title("Vitaltech Fitness App") # Sets window title

        self.widgets() # Calls the function that builds UI
        self.root.mainloop()  # Starts tkinter

    def widgets(self):
        # --------- App Title ---------
        self.title_label = tk.Label(self.root, text="Vitaltech Fitness App", font=('Aptos', 18, "bold"))
        self.title_label.pack(pady=20)

        # --------- User Info ---------
        self.user_info_label = tk.Label(self.root, text="User Info:", font=('Aptos', 14))
        self.user_info_label.pack(anchor="w", padx=10)

        # Create a new frame inside main window for 'Name'
        # Add the frame to the window and create a lebel, entry box etc styled
        name_frame = tk.Frame(self.root)
        name_frame.pack(anchor="w", padx=10, pady=5)
        tk.Label(name_frame, text="Name: ", width=10).pack(side=LEFT)
        self.name_entry = tk.Entry(name_frame)
        self.name_entry.pack(side=LEFT)

        # Age
        age_frame = tk.Frame(self.root)
        age_frame.pack(anchor="w", padx=10, pady=5)
        tk.Label(age_frame, text="Age: ", width=10).pack(side=LEFT)
        self.age_entry = tk.Entry(age_frame)
        self.age_entry.pack(side=LEFT)

        # Height
        height_frame = tk.Frame(self.root)
        height_frame.pack(anchor="w", padx=10, pady=5)
        tk.Label(height_frame, text="Height: ", width=10).pack(side=LEFT)
        self.height_entry = tk.Entry(height_frame)
        self.height_entry.pack(side=LEFT)

        # Weight
        weight_frame = tk.Frame(self.root)
        weight_frame.pack(anchor="w", padx=10, pady=5)
        tk.Label(weight_frame, text="Weight: ", width=10).pack(side=LEFT)
        self.weight_entry = tk.Entry(weight_frame)
        self.weight_entry.pack(side=LEFT)


def main():
    app = GUI()

if __name__ == "__main__":
    main()
