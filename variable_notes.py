# #Print the 8th character of __ and capitalise it
# print("All Around The World"[7].upper())

my_name = "Sam"
# print(my_name)

my_age = 21
# print(my_age)

is_a_teacher = False
# print(is_a_teacher)

# #snake_case

favourite_drink = "latte"

# print(my_name, "'s favourite drink is a", favourite_drink)
# print(my_name + "'s favourite drink is a " + favourite_drink)
# print(my_name + " is", my_age, "and their favourite drink is a " + favourite_drink) # can't concatenate integer to a string

# print("{} is {} years old and their favourite drink is {}".format(my_name, my_age, favourite_drink))
# print(f"{my_name} is {my_age} years old and their favourite drink is {favourite_drink}")

# username = input("Type your username here:  > ")
# print(f"Hello, {username}")
# print(type(username))

# print(3+7)
# print(7-4)
# print(3*2)
# print(3**3)
# print(15/3)
# print(16%3)

balance = 100
print(f"Your balance is currently £{balance}")
withdraw_amount = int(input("How much would you like to withdraw?:  > "))
balance = balance - withdraw_amount
print(f"You have withdrawn {withdraw_amount} and your balance is now £{balance}")

# print("Type in two numbers to multiply them")

# num1 = int(input("Number 1:  > "))
# num2 = int(input("Number 2:  > "))

# print(num1*num2)