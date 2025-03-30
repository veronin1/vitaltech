from person import Person

class UserData(Person):
    def __init__(self, name, age, height, weight, steps, heart_rate, water_intake):
        super().__init__(name, age, height, weight)
