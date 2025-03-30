from person import Person

# UserData class inherits from Person class
class UserData(Person):
    def __init__(self, name, age, height, weight, steps, heart_rate, water_intake):
        # call the parent constructor (Person class) to set name, age, height, weight
        super().__init__(name, age, height, weight)

        # Set additional attributes specific to this class
        self.steps = steps
        self.heart_rate = heart_rate
        self.water_intake = water_intake  # in milliliters

        # This performs methods(functions) immediately when object is created
        self.bmi = self.calculate_bmi()
        self.mhr = self.calculate_mhr()
        self.distance_walked = self.calculate_distance_walked()
        self.recommended_water = self.calculate_recommended_water()

    # calculate bmi
    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    # calcumate mhr (maximum hert rate)
    def calculate_mhr(self):
        return 220 - self.age

    # calculate estimated distance walked in km (makes more sense than miles?)
    def calculate_distance_walked(self):
        stride_length = self.height * 0.415  # average stride length in meters (google)
        return round((self.steps * stride_length) / 1000, 2)  # convert to kilometers

    # Calculate recommended daily water intake in liters (common guideline)
    def calculate_recommended_water(self):
        return round((self.weight * 35) / 1000, 2)

    # convert the user’s full data into a dictionary
    def convert_to_dictionary(self):
        return {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "steps": self.steps,
            "heartRate": self.heart_rate,
            "mhr": self.mhr,
            "waterIntake": self.water_intake,
            "distanceWalkedInKM": self.distance_walked,
            "recommended_water": self.recommended_water
        }

    # Function to write user data to a text file
    # File is saved as username
    # provides type hint so that the data is expected to always be a dictionary
    def print_to_text(self):
        filename = f"{self.name}.txt"
        with open(filename, "a") as f:
            f.write(f"{self.name} Data\n")
            for key, value in self.convert_to_dictionary().items():
                f.write(f"{key}: {value}\n")
            f.write("\n")  # Add a blank line between entries
        print(f"Saved data to {filename}")

