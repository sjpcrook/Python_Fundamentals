# #Activity 1 - Asks for name, age and fav. colour, then states them back.

# name = input("What is your name?:  > ").capitalize()
# age = input("How old are you?:  > ")
# colour = input("What is your favourite colour?:  > ").lower()

# print(f"Your name is {name}, you are {age} years old and your favourite colour is {colour}.")


# #Activity 2 - Takes two numbers and performs multiple operations with them, returning each equation and answer

# num1 = int(input("Please choose your first number: "))
# num2 = int(input("Please choose your second number: "))

# print(f"{num1} + {num2} = {num1 + num2}") #Addition
# print(f"{num1} - {num2} = {num1 - num2}") #Subtraction
# print(f"{num1} / {num2} = {num1 / num2}") #Division
# print(f"{num1} * {num2} = {num1 * num2}") #Multiplication
# print(f"{num1} ** {num2} = {num1 ** num2}") #Exponent
# print(f"{num1} % {num2} = {num1 % num2}") #Modulus

# #Activity 3 - Asks for how apples and bananas are desired, then returns the price of each and the total

# apple_price = 0.25
# banana_price = 0.5

# apple_quantity = int(input(f"How many apples would you like? (£{apple_price:.2f} per apple)  > "))
# banana_quantity = int(input(f"How many bananas would you like? (£{banana_price:.2f} per banana)  > "))

# apple_total = apple_price * apple_quantity
# banana_total = banana_price * banana_quantity
# final_total = apple_total + banana_total

# print(f"{apple_quantity} apples will cost £{apple_total:.2f}.")
# print(f"{banana_quantity} bananas will cost £{banana_total:.2f}.")
# print(f"Altogether, that will be £{final_total:.2f}.")

# #Activity 3 (Stretch) #Demonstrates how to output desirable decimal placed (i.e £2.00)
# print("Using ':.nf' directly after a number in an f string will return the float to n decimal places, rounding if needs be")
# print(f"{2:.2f}")
# print(f"{4.5:.7f}")
# print(f"{2/3:.5f}")

# #CONSTANT VARIABLES
# PI = 3.14
# GRAVITY = 9.81

# #Multiple variables in one line
# a, b = 5, 8
# print(a + b)

