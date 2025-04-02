"""
This file defines the Person class which is the fundamental class for representing individuals in my program. 
The coding standards implemented here are in full compliance with "PEP 8 Guidelines", like using the 4-space rule for nesting, no lines are longer than 79 characters, top-level functions and class definitions are surrounded by 2 blank lines, whilst functions are surrounded by a single blank line. 
The class is designed to in a way that mimics the core OOP concepts of encapsulation and abstraction. 
The person class encapsulates properties like name, age, height, and weight providing a reusable structure for other classes. 
Inheritance is used in other files like data.py to extend this person class without duplicating code which demonstrates the DRY (Don't Repeat Yourself) principle. 
As well as this, the simplicity of the Person class allows for other classes to only use the key, important attributes. Promoting a clear and logical codebase.
"""


class Person:

    def __init__(self, name, age, height, weight):
        # Initialise the Person object with following attributes. Using title() on the name ensures uniformity.
        self.name = name.title()
        self.age = age
        self.height = height
        self.weight = weight

