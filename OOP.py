#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
class Employee:
    
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + '.' + last + '@company.com'
        
    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def fullname(self):
        self.pay=int(self.pay * 1.04)
    

emp_1 = Employee('bob','bobby',5000)
emp_2 = Employee("test","user",6000)

print (emp_1.email)
print (emp_2.email)


print(emp_1.fullname())
"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
class Dog:
        
    def __init__(self, name, age):
        self.name= name
        self.age= age
        
    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")
        
    def talk(self):
        print('Bark')
    

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def talk(self):
        print('Meow')

tim = Cat('tim', 5, 'blue')
tim.speak()
"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
class Car:
    
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This car is driving")
        
    def stop(self):
        print("This car is stopped")
                
car1 = Car("Honda", "Accord", 2024,"sliver")
car1 = Car("Honda", "Accord", 2024,"sliver")


print (car1.make)
print (car1.model)
print (car1.color)
print (car1.year)

car1.drive()
"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 

"""
class BankAccount:
    def __init__(self, initial_balance=0):
        self.current_balance = initial_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if amount > self.current_balance:
            print("Insufficient funds.")
        else:
            self.current_balance -= amount

    def get_balance(self):
        return self.current_balance

# Example usage:
account = BankAccount(100)
account.deposit(50)
account.withdraw(0)
print("Current balance:", account.get_balance())  # Should output 130
"""
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine started.")
        
    def stop_engine(self):
        print("Engine stopped.")
            
    def speak(self):
        print(f"Hello, your car is a {self.make}, model: {self.model}, year: {self.year}")

car = Car("Toyota", "Camry", 2020)
car.speak()

car.stop_engine()
"""

#---------------------------------------------------------------------------------------------------------------------------------------------- 

"""
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_mileage(self):
        return self._mileage

    def set_mileage(self, mileage):
        if mileage >= self._mileage:  # Ensuring mileage can only increase
            self._mileage = mileage
        else:
            print("Mileage cannot decrease")

    def display_info(self):
        print(f"{self._make} {self._model} ({self._year}), Mileage: {self._mileage} miles")

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2015)

# Accessing and modifying attributes via methods
my_car.set_mileage(15000)
my_car.display_info()

# Trying to decrease the mileage
my_car.set_mileage(14000)  # This will not change the mileage and display a message

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # This will be overridden in each subclass

class Lion(Animal):
    def make_sound(self):
        return "Roar"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_sounds(self):
        for animal in self.animals:
            print(f"{animal.name} says {animal.make_sound()}")

# Creating a zoo instance
my_zoo = Zoo()

# Creating animal instances
simba = Lion("Simba")
dumbo = Elephant("Dumbo")

# Adding animals to the zoo
my_zoo.add_animal(simba)
my_zoo.add_animal(dumbo)

# Displaying sounds of all animals in the zoo
my_zoo.display_sounds()
"""
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
class Employee:
    _total_employees = 0
    _next_id = 1
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.id = Employee._generate_id()
        Employee._total_employees += 1

    @classmethod
    def _generate_id(cls):
        id = cls._next_id
        cls._next_id += 1
        return id

    @classmethod
    def get_total_employees(cls):
        return cls._total_employees
    
    @staticmethod
    def company_policy():
        return "All employees must adhere to the company policy."
   
# Creating employees
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

# Displaying employee IDs
print(f"Employee {emp1.name} ID: {emp1.id}")
print(f"Employee {emp2.name} ID: {emp2.id}")

# Displaying total number of employees
print("Total employees:", Employee.get_total_employees())

# Accessing the static method
print(Employee.company_policy())
"""