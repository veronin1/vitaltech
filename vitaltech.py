# Vitaltech Fitness App
# Users can enter and store their name, age, height and weight;
# Users can enter their health metrics such as steps, water intake and heart rate;
# The application will calculate fitness data, such as BMI. This can be a separate section of the application and is not required to be stored with other data;
# Save the users' data into a text file.

# Create empty dictionary
people = {}

# Function to ensure positive user inputs
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
            return f"{user_input} is an incorrect value"


# Function to calculate BMI based off 2 inputs and round to 2 d.p.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return f"{bmi:.2f}"

# Function to Calculate a rough estimate of the maximum number of heartbeats per minute during exercise
def calculate_mhr(age):
     return 220 - age

# Function to estimate the distance walked in km
def step_count_conversion(steps, height):
     stride_length  = height * 0.415
     distance_in_km = (steps * stride_length) / 1000
     return f"{distance_in_km}"

# Recommended water intake
def water_intake(weight):
     return (weight * 35) / 1000 

# Function to write user data to a
# 
# 0. text file.
# File is saved as username
def print_to_text(userName, data):
    with open(f"{userName}.csv", "a") as f:
        f.write(f"{userName}: {data}\n")
        print(f"{userName} data printed to .csv file!")


# ---------- Inputs ---------- # 
# While loop to continiously prompt user for input until valid data is provided
while True:  
            userName = get_positive_input("Name:", str).title()
            age = get_positive_input("Age: ", int)
            height = get_positive_input("Height in metres (i.e. 1.7): ", float)
            weight = get_positive_input("Weight in kilograms (i.e. 65.4): ", float)
            steps = get_positive_input("Steps (i.e. 12000): ", int)
            heartRate = get_positive_input("Current Heartrate (i.e. 120): ", int)
            waterIntake = get_positive_input("Water Intake in ml (i.e. 830): ", int)
            
            break


# ------------------ Calculations ------------------ #
# Calculate fitness metrics.
bmi = calculate_bmi(weight, height)
mhr = calculate_mhr(age)
distance = step_count_conversion(steps, height)
recommended_water = water_intake(weight)  # in liters


# ---------- Store Data ---------- #
# Nested dictionary storing user data
# The key is the username and the value is another dictionary
# this dictionary contains the user's age, height, weight, BMI
people[userName] = {
    "age": age,
    "height": height,
    "weight": weight,
    "bmi": bmi,
    "steps": steps,
    "heartRate": heartRate,
    "mhr": mhr,
    "waterIntake": waterIntake,
    "distanceWalkedInKM": distance,
    "recommended_water": recommended_water
}

# ---------- Write Data to File ---------- #
print_to_text(userName, people[userName])