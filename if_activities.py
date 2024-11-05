
#* Activity 1

# password = input("Please enter a password:  > ")
# length = len(password)
# if length >= 8:
#     print(password)
# else:
#     print("That password is too short.")

#* Activity 2

# num = int(input("Please enter a number:  > "))
# mod3, mod5 = num%3, num%5
# if mod3 == 0 or mod5 == 0:
#     print("This number is divisible by 3 or 5")
# else:
#     print("This number is not divisible by 3 or 5")

#*Activity 3

# num = int(input("Please enter a number:  > "))
# mod3, mod7 = num%3, num%7
# if mod3 == 0 and mod7 == 0:
#     print("fizzbuzz")
# elif mod3 == 0:
#     print("fizz")
# elif mod7 == 0:
#     print("buzz")
# else:
#     print(num)

#*Activity 4

# print("What is the capital of England?")

# answer = input("Type your answer here >> ").capitalize()

# if answer == "London":
#     print(f"Correct! The answer is {answer}")
# else:
#     print(f"Incorrect, the answer is 'London', not {answer}")

#*Activity 5

# word = input("Please enter a string:  > ") #Requires a comparison
# if word[0] == word[-1]:
#     print(True)
# else:
#     print(False)

# word = input("Please enter a string:  > ") #Requires no comparison
# print(word[0] == word[-1])

#*Activity 6

# word = input("Please enter a string:  > ") #Requires a comparison
# if word == word[::-1]:
#     print(True)
# else:
#     print(False)

# word = input("Please enter a string:  > ") #Requires no comparison
# print(word == word[::-1])

#! [a:b:c] is a slice where a is the starting position, b is the end position and c is the interval.
#! This usually defaults a = 0, b = -1, c = 1, though will become a = -1, b = 0 if c is negative