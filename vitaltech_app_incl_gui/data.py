"""
This file defines the UserData class which extends the Person class (via inheritance) to incorporate the actual userdata section of code. This performs health-related calculations and additional metrics like printing and storing the user data to text.
This design makes extensive use of inheritance, allowing the UserData class to build upon the foundamtional behaviours defined in the person class.
Encapsulation is also achieved by bundling both the data (attributes) and the functions (methods) that manipulate all the data into the same class, ensuring that the internal workings of this class are not accessible or modifiable otherwise.
This approach increases data integrity and reduces potential bugs.
As for coding standards in general, I used the Ruff linter to format the document to PEP 8 guidelines, and used OOP best practices to ensure that each method in the class had a single responsibility, whether it is calculating BMI, or converting the data to a dictionary etc.
Furthermore, the separation between core data processing and file I/O operations supports maintainability and scalability, enabling easy enhancements or modifications in the future.
"""
from person import Person


# UserData class inherits from Person class
class UserData(Person):
    def __init__(
        self, name, age, height, weight, steps, heart_rate, water_intake):
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
        return round(self.weight / (self.height**2), 2)

    # calcumate mhr (maximum hert rate)
    def calculate_mhr(self):
        return 220 - self.age

    # calculate estimated distance walked in km (makes more sense than miles?)
    def calculate_distance_walked(self):
        stride_length = (
            self.height * 0.415
        )  # average stride length in meters (google)
        return round(
            (self.steps * stride_length) / 1000, 2
        )  # convert to kilometers

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
            "recommended_water": self.recommended_water,
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
