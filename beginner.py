#HELLO WELCOME TO MY Python Programming Lessons!

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
# Lesson 1: Introduction to If/Else Statements.


# Python If/Else Statement Example

# Prompt the user for input
online = input("Are you online?: ")

# If/Else condition to check the user's input
if online == "yes":
    print("Yes, I am online on PS4")
else:
    print("No, I am offline on PS4")
#----------------------------------------------------------------------------------------------------------------------------------------------

"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
# Lesson 2: Understanding Data Types and Variables

# Python Variables and Data Types Example

# Define variables with different data types
name = "Bob"
age = 21
gpa = 2.2
student = True

# Convert the boolean 'student' to a string
student = str(student)

# Display the type of the 'student' variable
print(type(student))
#----------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 3: Basic Arithmetic and User Input


# Python Arithmetic and User Input Example

# Ask the user for input and store it in variables
item = input("What item do you want? ")
price = float(input("How much is the item? $"))
quantity = float(input("How many? "))

# Perform a calculation using the input values
amount = price * quantity

# Print out the details and total amount
print(f"You ordered {item}, the price of {item} is ${price}.")
print(f"How many {item} you want: {quantity}")
print("Ok!")
print(f"Your total is ${amount}")
#----------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 4: Calculating Hypotenuse Using Math Module

import math

# Ask the user to input the lengths of the sides
a = float(input("Give me side a of the triangle: "))
b = float(input("Give me side b of the triangle: "))

# Calculate the hypotenuse using the Pythagorean theorem
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

# Print the result
print(f"The hypotenuse of your right triangle is: {hypotenuse}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 5: Age-Based Categorization with Conditional Statements

# Ask the user for their age
userage = input("How old are you?: ")

# Convert the input to an integer
age = int(userage)

# Use conditional statements to categorize the age
if 13 <= age < 20:
    print(f"You are {age}, so you are a teenager.")
elif 1 <= age < 13:
    print(f"You are {age}, so you are a kid.")
elif age >= 20:
    print(f"You are {age}, so you are an adult.")
else:
    print(f"Invalid age {age}, please enter a valid number.")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 6: Handling Invalid Inputs and Float Values

# Ask the user for their age
userage = input("How old are you?: ")

# Check if the input is a floating-point number
if "." in userage:
    print("Please enter a whole number for your age.")
elif not userage.isdigit():
    print("Invalid input. Please enter a valid number.")
else:
    # Convert the input to an integer
    age = int(userage)

    # Use conditional statements to categorize the age
    if 13 <= age < 20:
        print(f"You are {age}, so you are a teenager.")
    elif 1 <= age < 13:
        print(f"You are {age}, so you are a kid.")
    elif age >= 20:
        print(f"You are {age}, so you are an adult.")
    else:
        print("Invalid input. Please enter a valid number.")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 7: Calculating the Hypotenuse in a Right Triangle

import math

# Ask the user to input the lengths of the two sides of a right triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Calculate the hypotenuse using the Pythagorean theorem
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

# Print the hypotenuse
print(f"The hypotenuse of your right triangle is: {hypotenuse}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""
"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 8: Using Conditional Statements to Categorize Age

# Prompt the user for their age
userage = input("How old are you?: ")
age = int(userage)

# Conditional statements to determine the age category
if 13 <= age < 20:
    print(f"You are {age}, so you are a teenager.")
elif 1 <= age < 13:
    print(f"You are {age}, so you are a kid.")
elif age >= 20:
    print(f"You are {age}, so you are an adult.")
else:
    print(f"Invalid age {age}, please enter a valid age.")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 9: Validating Numeric Input for Age

# Prompt the user for their age
userage = input("How old are you?: ")

# Validate the input and ensure it is a whole number
if "." in userage:
    print("Please enter a whole number for your age.")
elif not userage.isdigit():
    print("Invalid input. Please enter a valid number.")
else:
    age = int(userage)

    # Conditional statements for different age categories
    if 13 <= age < 20:
        print
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 11: Calculating Compound Interest with Input Validation

# Initialize the variables
principle = 0
rate = 0
time = 0

# Validate principle amount
while principle <= 0:
    principle = float(input("Enter principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

# Validate rate amount
while rate <= 0:
    rate = float(input("Enter rate amount: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

# Validate time amount
while time <= 0:
    time = int(input("Enter time amount: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

# Calculate the total amount using compound interest formula
total = principle * pow((1 + rate / 100), time)

# Print the result
print(f"The total amount after {time} years is: {total}")

#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 12: Validating Credit Card Numbers (Luhn Algorithm)

# Input and pre-process card number
card_number = input("Enter your card number: ")
card_number = card_number.replace("-", "").replace(" ", "")[::-1]

sum_even = 0
sum_odd = 0

# Step 2: Sum of odd digits
for digit in card_number[::2]:
    sum_odd += int(digit)

# Step 3: Double every second digit and sum them
for digit in card_number[1::2]:
    doubled = int(digit) * 2
    sum_even += doubled if doubled < 10 else 1 + (doubled % 10)

# Step 4: Calculate total sum
total = sum_odd + sum_even

# Step 5: Check if the total modulo 10 is zero (valid card)
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")

print(f"Processed card number: {card_number[::-1]}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 13: Iterating Over a Set

fruits = {"apple", "orange", "kiwi"}

# Iterate over the set and print each element
for fruit in fruits:
    print(fruit)
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 14: Creating a Shopping Cart with Dynamic Inputs

foods = []
prices = []
total = 0

# Collect food items and prices from the user
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

# Display the shopping cart and calculate total
print("---------Your Cart------------")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Your total is ${total}, enjoy!")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 15: Nested Lists and Modifying Elements

fruits = ["apples", "orange", "pear", "banana"]
veggies = ["potato", "carrots", "tomato"]
meats = ["fish", "chicken", "steak"]

food = [fruits, veggies, meats]
fruits[0] = "pineapple"

# Print the modified fruits list
print(fruits)
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 16: Iterating Through a Nested Tuple

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# Iterate through each row and number in the nested tuple
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 17: Creating a Quiz Game with Multiple Choice Questions

questions = ("What color are bananas?: ",
             "How many continents are there on Earth?: ",
             "What is the largest mammal in the world?: ",
             "What is the capital of France?: ")

options = (("A. red", "B. car", "C. yellow", "D. green"), 
           ("A. 3", "B. 1", "C. 7", "D. 8"),
           ("A. dog", "B. hippo", "C. cat", "D. whale"),
           ("A. Man City", "B. Nothignton", "C. Paris", "D. India"))

answers = ("C", "C", "D", "C")
guesses = []
score = 0

# Loop through each question and present options
for questions_num, question in enumerate(questions): 
    print("-------------------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
        
    # Get the user's guess
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    # Check and respond to the guess
    if guess == answers[questions_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[questions_num]} is the correct answer")
    
# Display the results
print("-------------------------------------")
print("---------------RESULTS---------------")
print("-------------------------------------")
print("Answers: ", ' '.join(answers))
print("Guesses: ", ' '.join(guesses))
score_percentage = int((score / len(questions)) * 100)
print(f"{score_percentage}%")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 18: Exploring and Manipulating Dictionaries
capitals = {"USA": "Washington D.C.",
            "Sudan": "Khartoum",
            "India": "New Delhi",
            "China": "Beijing"}

# Display all key-value pairs in the dictionary
for country, capital in capitals.items():
    print(f"{country}: {capital}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 19: Building a Simple Ordering System

menu = {"pizza": 2.50,
        "chicken": 3.00,
        "nachos": 2.00,
        "fries": 1.00,
        "wrap": 5.00,
        "soda": 1.50,
        "water": 0.50}

cart = []
total = 0

# Display the menu
print("-------------MENU-------------")
for item, price in menu.items():
    print(f"{item:10} : ${price:.2f}")
print("------------------------------")

# Take orders from the user
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)

# Calculate the total and display the order
print("----------Your Order---------")
for food in cart:
    total += menu[food]
    print(food, end=" ")

# Print the total cost of the order
print(f"\nTotal is: ${total:.2f}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 20: Basic Random Number Guessing Game

import random

# Generate a random number
number = random.randint(1, 2)

# Game loop
while True:
    user_guess = int(input("Enter a number 1-2: "))
    
    if user_guess == number:
        print("Correct guess!")
        break
    else:
        print("Nope!")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 21: Enhanced Number Guessing Game

import random

# Generate a random number
number = random.randint(1, 2)

# Initial user input
user_guess = int(input("Enter a number 1-2: "))

# Game loop
while user_guess != number:
    print("Nope!")
    user_guess = int(input("Enter a number 1-2: "))

print("Correct guess!")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 22: Exploring Random Module Functions

import random

# Various random module functionalities
options = ("rock", "paper", "scissors")
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Shuffle the cards
random.shuffle(cards)
print(cards)
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 23: Basic Encryption and Decryption

import random
import string

# Prepare character sets for encryption
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

# Shuffle the key for encryption
random.shuffle(key)

# Encrypt the message
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt the message
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
# Lesson 24: Understanding Variable Scope

```python
# Global scope
a = 1

def hello():
    # Local scope
    b = 2
    print(b)

# Print global variable 'a'
print(a)

# Call function 'hello' which prints local variable 'b'
hello()

# This will result in an error as 'b' is not defined in the global scope
# print(b)

        print("Nope!")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 25: Basic Number Guessing Game with Random Module

import random

# Generate a random number between 1 and 2
number = random.randint(1, 2)

# Game loop
while True:
    user = int(input("Enter a number 1-2: "))
    if user == number:
        print("Correct guess!")
        break
    else:
        print("Nope!")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 26:  Enhanced Number Guessing Game

import random

# Generate a random number
number = random.randint(1, 2)

# Get the first guess
user = int(input("Enter a number 1-2: "))

# Loop until the correct guess
while user != number:
    print("Nope!")
    user = int(input("Enter a number 1-2: "))

print("Correct guess!")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 27: Using Random Module for Shuffling and Selection

import random

# List of cards
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Shuffle the cards
random.shuffle(cards)

# Display shuffled cards
print(cards)
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 28: Creating a Simple Encryption and Decryption Tool

import random
import string

# Create a list of characters for encryption
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

# Shuffle the key for encryption
random.shuffle(key)

# Encrypt the message
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt the message
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted original message: {cipher_text}")
print(f"Original message: {plain_text}")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""

"""
#----------------------------------------------------------------------------------------------------------------------------------------------
#Lesson 29: Handling Exceptions in Python

# Handling exceptions with try-except blocks
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
#---------------------------------------------------------------------------------------------------------------------------------------------- 
"""