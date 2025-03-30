from tkinter import *
import tkinter as tk
from data import UserData

class GUI:
    def __init__(self):
        self.root = tk.Tk()  # Creates window
        self.root.geometry("450x600")  # Sets window size
        self.root.title("Vitaltech Fitness App")  # Sets window title
        self.root.configure(bg="#f2f2f2")  # Light background

        self.widgets()
        self.root.mainloop()

    # function to ensure positive (valid) user input, altered from original
    def validate_input(self, value, expected_type):
        try:
            value = expected_type(value)

            if expected_type in [int, float] and value <= 0:
                raise ValueError

            if expected_type == str and not value.strip():
                raise ValueError

            return value
        except:
            return None


    def widgets(self):
        # --------- App Title ---------
        self.title_label = tk.Label(self.root, text="Vitaltech Fitness App", font=('Arial', 18, "bold"), bg="#f2f2f2", fg="#333")
        self.title_label.pack(pady=20)

        # --------- User Info ---------
        self.user_info_label = tk.Label(self.root, text="User Info:", font=('Arial', 14, "bold"), bg="#f2f2f2")
        self.user_info_label.pack(anchor="w", padx=10)

        user_info_frame = tk.Frame(self.root, bg="#f2f2f2")
        user_info_frame.pack(anchor="w", padx=10, pady=10)

        row = 0

        tk.Label(user_info_frame, text="Name:", bg="#f2f2f2").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(user_info_frame, width=30)
        self.name_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(user_info_frame, text="Age:", bg="#f2f2f2").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.age_entry = tk.Entry(user_info_frame, width=30)
        self.age_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(user_info_frame, text="Height in ft (i.e. 1.7):", bg="#f2f2f2").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.height_entry = tk.Entry(user_info_frame, width=30)
        self.height_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(user_info_frame, text="Weight in kg (i.e. 65.4):", bg="#f2f2f2").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.weight_entry = tk.Entry(user_info_frame, width=30)
        self.weight_entry.grid(row=row, column=1, padx=5, pady=5)

        # --------- Health Info ---------
        self.health_info_label = tk.Label(self.root, text="Health Info:", font=('Arial', 14, "bold"), bg="#f2f2f2")
        self.health_info_label.pack(anchor="w", padx=10)

        health_info_frame = tk.Frame(self.root, bg="#f2f2f2")
        health_info_frame.pack(anchor="w", padx=10, pady=10)

        tk.Label(health_info_frame, text="Steps:", bg="#f2f2f2").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.steps_entry = tk.Entry(health_info_frame, width=30)
        self.steps_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(health_info_frame, text="Heart Rate:", bg="#f2f2f2").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.heart_rate_entry = tk.Entry(health_info_frame, width=30)
        self.heart_rate_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(health_info_frame, text="Water Intake (L):", bg="#f2f2f2").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.water_entry = tk.Entry(health_info_frame, width=30)
        self.water_entry.grid(row=2, column=1, padx=5, pady=5)

        # --------- Buttons ---------
        button_frame = tk.Frame(self.root, bg="#f2f2f2")
        button_frame.pack(pady=20)

        add_info_button = tk.Button(button_frame, text="Add Info", bg="green", fg="white", width=15, command=self.add_info)
        add_info_button.pack(side="left", padx=10)

        calculate_button = tk.Button(button_frame, text="Calculate Metrics", bg="green", fg="white", width=15, command=self.calculate_metrics)
        calculate_button.pack(side="left", padx=10)

        view_button = tk.Button(button_frame, text="View Userdata", bg="green", fg="white", width=15, command=self.view_data)
        view_button.pack(side="left", padx=10)


        # --------- Output Textbox ---------
        self.output_label = tk.Label(self.root, text="System Output:", font=('Arial', 14, "bold"), bg="#f2f2f2")
        self.output_label.pack(anchor="w", padx=10)
        
        label_frame = tk.Frame(self.root, bg="#f2f2f2")
        label_frame.pack(pady=10)

        self.output_box = tk.Text(label_frame, height=7, width=50, bg="white", fg="black", relief="solid", bd=1)
        self.output_box.pack()

    def add_info(self):
        # get user input (text input) from entry boxes and validate
        name = self.validate_input(self.name_entry.get(), str)
        age = self.validate_input(self.age_entry.get(), int)
        height = self.validate_input(self.height_entry.get(), float)
        weight = self.validate_input(self.weight_entry.get(), float)
        steps = self.validate_input(self.steps_entry.get(), int)
        heart_rate = self.validate_input(self.heart_rate_entry.get(), int)
        water_intake = self.validate_input(self.water_entry.get(), float)

        # check if any input failed validation (checking for empty space)
        if None in [name, age, height, weight, steps, heart_rate, water_intake]:
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, "Entries are invalid")
            return

        # create a UserData object
        self.user = UserData(name, age, height, weight, steps, heart_rate, water_intake)

        # save to file by accessing the name inside user object and the function from userData!
        self.user.print_to_text()

        # show success message
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, f"Info added for{self.user.name}\n")

    def calculate_metrics(self):
        # checks if hte user has entered their info by checking if self.user exists
        if hasattr(self, 'user'):
            # Show health metrics
            output = (
                f"Name: {self.user.name}\n"
                f"BMI: {self.user.bmi}\n"
                f"Max Heart Rate: {self.user.mhr}\n"
                f"Distance Walked: {self.user.distance_walked} km\n"
                f"Water Intake: {self.user.water_intake} L\n"
                f"Recommended Water: {self.user.recommended_water} L"
            )
            # clears output box and inserts new data
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, output)
        else:
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, "Please add info first.")

    def view_data(self):
        # open the file just made for "comparison", read its content and save contents to variable
        try:
            with open(f"{self.user.name}.txt") as f:
                content = f.read()
        except FileNotFoundError:
                content = ""

        # count how many times the header appears
        count = content.count(f"{self.user.name} Data")

        output_message = f"Info added for {self.user.name} ({count})\n"
        output_message += content

        # show success message
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, output_message)