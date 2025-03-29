from tkinter import *
import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("450x600")
        self.root.title("Vitaltech Fitness App")

        self.widgets()
        self.root.mainloop()  # Moved here after everything is built

    def widgets(self):
        # --------- App Title ---------
        self.title_label = tk.Label(self.root, text="Vitaltech Fitness App", font=('Aptos', 18, "bold"))
        self.title_label.pack(pady=20)

        # --------- User Info ---------
        self.user_info_label = tk.Label(self.root, text="User Info:", font=('Aptos', 14))
        self.user_info_label.pack(anchor="w", padx=10)

        self.name_label = tk.Label(self.root, text="Name: ")
        self.name_label.pack(side=LEFT, padx= 10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(side=LEFT)

        self.name_label = tk.Label(self.root, text="Age: ")
        self.name_label.pack(anchor="w", padx= 10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(anchor="w", padx= 10)

        self.name_label = tk.Label(self.root, text="Height: ")
        self.name_label.pack(anchor="e", padx= 10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(anchor="e", padx= 10)

        self.name_label = tk.Label(self.root, text="Weight: ")
        self.name_label.pack(anchor="e", padx= 10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(anchor="e", padx= 10)

def main():
    app = GUI()

if __name__ == "__main__":
    main()
