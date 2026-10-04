# Define a class called Person
class Person:
    # Define how a Person object can be created (a constructor)
    # This states that when a Person object is made, 3 values must be provided
    # We also have to supply self as the first parameter, so that python knows
    # WHICH Person to set the information for
    # The constructor's code should set up the new object in whatever way
    # you think is appropriate for the system - think of it as the set-up stage
    # This includes declaring the attributes that make up that object
    def __init__(self, f_name, l_name, age):
        # Store the first_name value provided by the calling code in the first_name attribute (self.first_name)
        self.first_name = f_name
        # Store the last_name value provided by the calling code in the last_name attribute (self.last_name)
        self.last_name = l_name
        # Store the age value provided by the calling code in the age attribute (self.age)
        self.age = age
    
    # Define a display method to print out the information of the current person object
    # self is specified as a parameter so this method knows whose version of the attributes to use
    def display(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")