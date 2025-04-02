"""
This file serves as the "entry point" for the application. It demonstrates the principle of minimalism by entrusting complex functionalities to other more specialised sections of the code to keep the main file easy to understand.
The design follows OOP best practices, by ensuring that each section has a single, clear responsibility.
The simplicity is a result of the modular approach I took to building the project.
I believe this approach improves maintainability and testability but also makes it easier for developers and others viewing the codebase to find issues and implement future enhancements, as there is a common structure and guideline for how code should look.
By simply instantiating the GUI class, the main module triggers the entire applicatio nworkflow demonstrating how effective encapsulation can lead to a clean program structure.
"""
from gui import GUI


def main():
    # Instantiate the GUI class to start the application, encapsulating the startup process
    GUI()


if __name__ == "__main__":
    main()
