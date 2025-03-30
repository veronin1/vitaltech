#### Vitaltech Fitness App

### Requirements and How They Are Met

1. **Users can enter and store their name, age, height, and weight**
   - **Implementation:**  
     The program defines a Person class (in *person.py*) that holds the basic attributes—name, age, height, and weight. This serves as the foundation for capturing user details.
     citeturn0file3

2. **Users can enter their health metrics such as steps, water intake, and heart rate**
   - **Implementation:**  
     The `UserData` class (in *data.py*) extends the `Person` class by adding attributes for health metrics including steps, heart rate, and water intake. This enables the app to capture daily health-related data.
     citeturn0file0

3. **The application will calculate fitness data, such as BMI**
   - **Implementation:**  
     Upon instantiation, the UserData class immediately computes several key metrics:
     - **BMI (Body Mass Index):** Calculated using weight divided by the square of the height.
     - **Other Metrics:** Also calculates maximum heart rate (using the formula 220 - age), estimated distance walked (based on steps and stride length), and recommended water intake.
   - **Note:**  
     The calculated fitness data (like BMI) is generated on demand and is used within the application. It is displayed as part of the user feedback but is not stored in the text file alongside the other raw user data.
     citeturn0file0

4. **Save the users' data into a text file**
   - **Implementation:**  
     The print_to_text() method in the UserData class is responsible for writing the user's data to a text file. Each file is named after the user (e.g., *Alice.txt*) and is appended with every new data entry, ensuring persistence of the user's inputs.
     citeturn0file0

---

### How Object-Oriented Programming Is Used to Achieve This

- **Encapsulation and Inheritance:**  
  - The **Person** class encapsulates the basic user information.  
  - The **UserData** class inherits from Person and extends it by incorporating additional health metrics and methods to calculate fitness data.
  
- **Separation of Concerns:**  
  - **Data Handling:**  
    All calculations and data conversions are handled by UserData.  
  - **User Interface:**  
    The GUI (in *gui.py*) is built using Tkinter and handles user inputs, data validation, and interactions like adding information or calculating metrics.
  - **Application Flow:**  
    The main file (*main.py*) acts as the entry point, ensuring a clear and modular separation between the interface and data processing components.
  
- **Dynamic Calculation vs. Data Storage:**  
  - The fitness metrics (such as BMI) are calculated dynamically when a UserData object is created or when metrics are requested, rather than being permanently stored. This aligns with the requirement of having a separate section for fitness calculations.
