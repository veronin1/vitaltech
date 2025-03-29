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

        # Frame for user info entries
        user_info_frame = tk.Frame(self.root)
        user_info_frame.pack(anchor="w", padx=10, pady=10)

        # Row counter
        row = 0

        # User Info Fields
        tk.Label(user_info_frame, text="Name:").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(user_info_frame)
        self.name_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(user_info_frame, text="Age:").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.age_entry = tk.Entry(user_info_frame)
        self.age_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(user_info_frame, text="Height:").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.height_entry = tk.Entry(user_info_frame)
        self.height_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(user_info_frame, text="Weight:").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.weight_entry = tk.Entry(user_info_frame)
        self.weight_entry.grid(row=row, column=1, padx=5, pady=5)

        # --------- Health Info ---------
        self.health_info_label = tk.Label(self.root, text="Health Info:", font=('Aptos', 14))
        self.health_info_label.pack(anchor="w", padx=10)

        # Frame for health info entries
        health_info_frame = tk.Frame(self.root)
        health_info_frame.pack(anchor="w", padx=10, pady=10)

        # Health Info Fields
        tk.Label(health_info_frame, text="Steps:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.steps_entry = tk.Entry(health_info_frame)
        self.steps_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(health_info_frame, text="Heart Rate:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.heart_rate_entry = tk.Entry(health_info_frame)
        self.heart_rate_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(health_info_frame, text="Water Intake (L):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.water_entry = tk.Entry(health_info_frame)
        self.water_entry.grid(row=2, column=1, padx=5, pady=5)

        # --------- Buttons --------- 
        b1 = Button(self.root, text = "Button", background = "green", fg = "gray30")
        b1.pack(fill = BOTH, expand = True)

def main():
    app = GUI()

if __name__ == "__main__":
    main()
