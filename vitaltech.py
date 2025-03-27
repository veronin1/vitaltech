# Luke Stackhouse.py

# Create empty dictionary
people = {}

# Function to calculate BMI based off 2 inputs and round to 2 d.p.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return f"{bmi:.2f}"

# Function to Calculate a rough estimate of the maximum number of heartbeats per minute during exercise
def calculate_mhr(heartRate, age):
     return 220 - age

# Function to estimate the distance walked in km
def step_count_conversion(steps, height):
     stride_length  = height * 0.415
     distance_in_km = (steps * stride_length) / 1000
     return f"{distance_in_km}"

# Recommended water intake
def water_intake(weight):
     return (weight * 35) / 1000 

# Function to write user data to a text file.
# File is saved as username
def print_to_text(userName, data):
    with open(f"{userName}.csv", "a") as f:
        f.write(f"{userName}: {data}\n")


# ---------- Inputs ---------- # 
# While loop to continiously prompt user for input until valid data is provided
while True:  
        try: 
            userName = input("Name: ").title()
            age = int(input("Age: "))
            height = float(input("Height in metres (i.e. 1.7): ")) 
            weight = float(input("Weight in kilograms (i.e. 65.4): "))
            steps = int(input("Steps (i.e. 12000): "))
            heartRate = int(input("Current Heartrate (i.e. 120): "))
            waterIntake = int(input("Water Intake in ml (i.e. 830): "))
            break
        except ValueError:
            # If there is a value error, print an error message and reprompt user to input
            print("Invalid")


# ------------------ Calculations ------------------ #
# Calculate fitness metrics.
bmi = calculate_bmi(weight, height)
mhr = calculate_mhr(heartRate, age)
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