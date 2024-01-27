# Object Oriented Programming

#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
# Lesson 1: Introduction to Python Classes and Instance Methods

# Defining a class named 'Employee'
class Employee:
    # Special method called constructor (__init__) to initialize the instance variables
    def __init__(self, first, last, pay):
        self.first = first   # Instance variable for first name
        self.last = last     # Instance variable for last name
        self.pay = pay       # Instance variable for pay
        self.email = first + '.' + last + '@company.com'  # Instance variable for email

    # An instance method to return the full name of the employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Note: This method is incorrectly named as 'fullname', it should be something like 'apply_raise'.
    # It's also incorrectly overwriting the previous 'fullname' method. 
    # Correcting it to a method for applying a raise:
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)  # Apply a 4% raise to the employee's pay

# Creating two Employee instances with given names and pay
emp_1 = Employee('Bob', 'Bobby', 5000)
emp_2 = Employee('Test', 'User', 6000)

# Printing the email addresses of the employees
print(emp_1.email)
print(emp_2.email)

# Printing the full name of the first employee
# Corrected to use the 'fullname' method
print(emp_1.fullname())

"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
# Lesson 2: Inheritance and Method Overriding

# Defining a 'Dog' class
class Dog:
    
    def __init__(self, name, age):
        self.name = name  # Instance variable for the dog's name
        self.age = age    # Instance variable for the dog's age
        
    def speak(self):
        # Method to print a message including the dog's name and age
        print("Hi I am", self.name, "and I am", self.age, "years old")
        
    def talk(self):
        # A simple method for the dog to 'talk'
        print('Bark')
    

# Defining a 'Cat' class that inherits from 'Dog'
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Calling the constructor of the parent 'Dog' class
        self.color = color  # Additional attribute for the 'Cat' class

    def talk(self):
        # Overriding the 'talk' method for a cat
        print('Meow')

# Creating an instance of the 'Cat' class
tim = Cat('Tim', 5, 'Blue')
tim.speak()  # Calling the 'speak' method inherited from 'Dog'
"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
# Lesson 3: Basic Class Creation and Instance Usage

# Defining the 'Car' class
class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make    # Attribute for the make of the car
        self.model = model  # Attribute for the model of the car
        self.year = year    # Attribute for the year of the car
        self.color = color  # Attribute for the color of the car
    
    def drive(self):
        # Method to simulate driving the car
        print("This car is driving")
        
    def stop(self):
        # Method to simulate stopping the car
        print("This car is stopped")
                
# Creating an instance of 'Car'
car1 = Car("Honda", "Accord", 2024, "Silver")

# Accessing attributes of the 'Car' instance
print(car1.make)
print(car1.model)
print(car1.color)
print(car1.year)

# Calling a method of the 'Car' instance
car1.drive()

"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
# Lesson 4: Encapsulation and Simple Banking System

# Defining the 'BankAccount' class
class BankAccount:
    def __init__(self, initial_balance=0):
        self.current_balance = initial_balance  # Initializing the balance

    def deposit(self, amount):
        # Method to deposit money into the account
        self.current_balance += amount

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > self.current_balance:
            print("Insufficient funds.")
        else:
            self.current_balance -= amount

    def get_balance(self):
        # Method to get the current balance
        return self.current_balance

# Example usage of the BankAccount class
account = BankAccount(100)  # Starting with an initial balance of 100
account.deposit(50)         # Depositing 50
account.withdraw(20)        # Withdrawing 20
print("Current balance:", account.get_balance())  # Should output 130

"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
# Lesson 5: Creating a Car Class with Basic Methods

# Defining the 'Car' class
class Car:
    def __init__(self, make, model, year):
        self.make = make   # Attribute for the make of the car
        self.model = model # Attribute for the model of the car
        self.year = year   # Attribute for the year of the car
    
    def start_engine(self):
        # Method to simulate starting the car's engine
        print("Engine started.")
        
    def stop_engine(self):
        # Method to simulate stopping the car's engine
        print("Engine stopped.")
            
    def speak(self):
        # Method to display information about the car
        print(f"Hello, your car is a {self.make}, model: {self.model}, year: {self.year}")

# Creating an instance of the 'Car' class
car = Car("Toyota", "Camry", 2020)

# Using the methods of the 'Car' instance
car.speak()       # Displays information about the car
car.stop_engine() # Simulates stopping the engine

"""

#---------------------------------------------------------------------------------------------------------------------------------------------- 

"""
# Lesson 6: Encapsulation with Getter and Setter Methods in a Car Class

# Defining the 'Car' class with private attributes
class Car:
    def __init__(self, make, model, year):
        self._make = make   # Private attribute for the make of the car
        self._model = model # Private attribute for the model of the car
        self._year = year   # Private attribute for the year of the car
        self._mileage = 0   # Private attribute for the mileage of the car

    # Getter method for make
    def get_make(self):
        return self._make

    # Setter method for make
    def set_make(self, make):
        self._make = make

    # Getter method for model
    def get_model(self):
        return self._model

    # Setter method for model
    def set_model(self, model):
        self._model = model

    # Getter method for year
    def get_year(self):
        return self._year

    # Setter method for year
    def set_year(self, year):
        self._year = year

    # Getter method for mileage
    def get_mileage(self):
        return self._mileage

    # Setter method for mileage
    def set_mileage(self, mileage):
        if mileage >= self._mileage:  # Validation to ensure mileage can only increase
            self._mileage = mileage
        else:
            print("Mileage cannot decrease")

    # Method to display car information
    def display_info(self):
        print(f"{self._make} {self._model} ({self._year}), Mileage: {self._mileage} miles")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2015)

# Using setter methods to modify the car's attributes
my_car.set_mileage(15000)

# Using the display_info method to show the car's details
my_car.display_info()

# Attempting to set the mileage to a lower value
my_car.set_mileage(14000)  # Will not change the mileage and will display a message

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
# Lesson 7: Polymorphism in a Zoo Simulation

# Defining the base class 'Animal'
class Animal:
    def __init__(self, name):
        self.name = name  # Initializing the name of the animal

    def make_sound(self):
        pass  # To be overridden in subclasses

# Defining the 'Lion' class inheriting from 'Animal'
class Lion(Animal):
    def make_sound(self):
        return "Roar"  # Overridden method for Lion

# Defining the 'Elephant' class inheriting from 'Animal'
class Elephant(Animal):
    def make_sound(self):
        return "Trumpet"  # Overridden method for Elephant

# Defining the 'Zoo' class
class Zoo:
    def __init__(self):
        self.animals = []  # List to store animals

    def add_animal(self, animal):
        self.animals.append(animal)  # Adding an animal to the zoo

    def display_sounds(self):
        # Displaying the sounds of all animals in the zoo
        for animal in self.animals:
            print(f"{animal.name} says {animal.make_sound()}")

# Creating a zoo instance
my_zoo = Zoo()

# Creating instances of Lion and Elephant
simba = Lion("Simba")
dumbo = Elephant("Dumbo")

# Adding the animal instances to the zoo
my_zoo.add_animal(simba)
my_zoo.add_animal(dumbo)

# Displaying the sounds of each animal in the zoo
my_zoo.display_sounds()

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
# Lesson 8: Class Methods, Static Methods, and Class Attributes

# Defining the 'Employee' class
class Employee:
    _total_employees = 0  # Class attribute to track total number of employees
    _next_id = 1          # Class attribute to generate unique IDs

    def __init__(self, name, position):
        self.name = name      # Instance attribute for employee's name
        self.position = position  # Instance attribute for employee's position
        self.id = Employee._generate_id()  # Assigning a unique ID to each employee
        Employee._total_employees += 1     # Incrementing the total employees count

    @classmethod
    def _generate_id(cls):
        # Class method to generate a unique ID
        id = cls._next_id
        cls._next_id += 1
        return id

    @classmethod
    def get_total_employees(cls):
        # Class method to get the total number of employees
        return cls._total_employees

    @staticmethod
    def company_policy():
        # Static method returning the company policy
        return "All employees must adhere to the company policy."

# Creating employee instances
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

# Displaying employee IDs
print(f"Employee {emp1.name} ID: {emp1.id}")
print(f"Employee {emp2.name} ID: {emp2.id}")

# Displaying the total number of employees
print("Total employees:", Employee.get_total_employees())

# Accessing the static method to display the company policy
print(Employee.company_policy())
"""