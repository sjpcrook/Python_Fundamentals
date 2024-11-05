# music = input("What music is playing?  > ").lower() #*variable, assignment, string

#* = is an assignment operator
#* == is a comparison operator

# print(music)
# print(music == "classical") # returns True
# print(music == "britpop") # returns False

# if music == "classical":
#     print("Oh no, not classical again!")
# elif music == "no music":
#     print("Alexa, play some music!")
# elif music == "britpop":
#     print("My second favourite! Turn it up!")
# else:
#     print("I've not heard this before!")

#* COMPARISON OPERATORS
#* == - Equals
#* != - Does not equal
#* >  - Greater than
#* >= - Greater than or equal to
#* <  - Less than
#* <= - Less than or equal to

# if (music != "britpop") and (music != "oasis"):
#     print("I want to listen to britpop!")
# elif music == "oasis":
#     print("The best!")
# else:
#     print("Yay! Britpop!")



# age = int(input("What is your age?  > "))
# location = input("What country are you in?  > ").upper()
# if age >= 18 and location == "UK":
#     print("Yes, I can serve you.")
# elif age < 18:
#     print("You aren't old enough.")
# else:
#     print("You aren't in the UK.")


#* LOGICAL OPERATORS
#* and - True and True returns True, otherwise returns False
#* or - False and False returns False, otherwise returns True

# place = "MCR"
# weather = "Cloudy"
# if place == "MCR" and weather == "Sunny":
#     print("Check again!")
# elif place =="MCR" and weather == "Rain":
#     print("Obvs")
# else:
#     print("What? It isn't raining?")

day = input("What day is it?  > ").capitalize()
bank_holiday = bool(input("Is it a bank holiday").capitalize())
if day == "Saturday" or day == "Sunday" or bank_holiday:
    print("A day off!")
else:
    print("Off to work I go.")








