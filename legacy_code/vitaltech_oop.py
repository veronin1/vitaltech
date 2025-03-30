people = {}

def get_positive_input(prompt, type):
    while True:
        try:
            user_input = type(input(prompt))

            # Check for numeric inputs
            if type in [int, float]:
                if user_input <= 0:
                    raise ValueError

            # If type is string, check for non empty input
            elif type == str:
                if not user_input.strip():
                    raise ValueError

            return user_input

        except ValueError:
            print(f"{user_input} is an incorrect value")

def get_user_input():
    while True:
            userName = get_positive_input("Name:", str).title()
            age = get_positive_input("Age: ", int)
            height = get_positive_input("Height in metres (i.e. 1.7): ", float)
            weight = get_positive_input("Weight in kilograms (i.e. 65.4): ", float)
            steps = get_positive_input("Steps (i.e. 12000): ", int)
            heartRate = get_positive_input("Current Heartrate (i.e. 120): ", int)
            waterIntake = get_positive_input("Water Intake in ml (i.e. 830): ", int)

            person = Person(userName, age, height, weight, steps, heartRate, waterIntake)
            people[userName] = person
            return person

def print_to_text(userName, data):
    with open(f"{userName}.csv", "a") as f:
        f.write(f"{userName}: {data}\n")
        print(f"{userName} data printed to .csv file!")

class Person:
    def __init__(self, name, age, height, weight, steps, heartRate, waterIntake):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.steps = steps
        self.heartRate = heartRate
        self.waterIntake = waterIntake

    def __str__(self):
        return (
            f"Age: {self.age}, "
            f"Height: {self.height} m, "
            f"Weight: {self.weight} kg, "
            f"Steps: {self.steps}, "
            f"Heart Rate: {self.heartRate} bpm, "
            f"BMI: {self.calculate_bmi()}, "
            f"Max Heart Rate: {self.calculate_mhr()}, "
            f"Distance Walked: {self.step_count_conversion()} km, "
            f"Recommended Water: {self.water_intake():.2f} L"
        )


    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return f"{bmi:.2f}"

    def calculate_mhr(self):
        return 220 - self.age

    def step_count_conversion(self):
        stride_length  = self.height * 0.415
        distance_in_km = (self.steps * stride_length) / 1000
        return f"{distance_in_km}"

    def water_intake(self):
        return (self.weight * 35) / 1000

def main():
    person = get_user_input()
    print_to_text(person.name, people[person.name])
    return

if __name__ == "__main__":
    main()
