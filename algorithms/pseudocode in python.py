# FUNCTION FOR GETTING USER INPUT
def GetUserInput():
    while True:
        try:
            print("Enter name, age, height, weight, steps, heart rate, water intake")
            # Getting all inputs as a single line split by comma could work, but for clarity we'll do one at a time
            name = input("Name: ")
            age = input("Age: ")
            height = input("Height: ")
            weight = input("Weight: ")
            steps = input("Steps: ")
            heartRate = input("Heart Rate: ")
            waterIntake = input("Water Intake: ")
            # We'll break here since you didn't want the extra validation
            break
        except ValueError:
            pass
        
    return name, age, height, weight, steps, heartRate, waterIntake

# FUNCTION FOR CALCULATING BMI
def CalculateBMI(weight, height):
    # Convert to float for calculation since inputs are strings
    bmi = float(weight) / (float(height) * float(height))
    return bmi

# DICTIONARY FOR STORING AND PRINTING userdata
userData = {}

# Get user input and add to dictionary
name, age, height, weight, steps, heartRate, waterIntake = GetUserInput()
bmi = CalculateBMI(weight, height)
userData['bmi'] = bmi
userData['name'] = name
userData['age'] = age
userData['weight'] = weight
userData['height'] = height
userData['steps'] = steps
userData['heartRate'] = heartRate
userData['waterIntake'] = waterIntake

# FUNCTION FOR PRINTING TO TEXT FILE
def SaveDataToFile(userName, userData):
    fileName = f"{userData['name']}"
    with open(fileName, 'a') as file:
        file.write(str(userData) + "\n")
    print("User data saved to file.")

# Call the save function
SaveDataToFile(name, userData)