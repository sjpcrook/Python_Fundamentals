import random

# print(random.random()) #random float between 0 and 1

# print(random.uniform(1,10)) #random float between 1 and 10

# print(random.randint(1, 10)) #random integer between 1 and 10 inclusive


def rng_game():
    my_number = int(input("What is your number?  > "))
    comp_number = None
    attempts = 0
    if (0 <= my_number) and (my_number <= 50):
        while comp_number != my_number:
            comp_number = random.randint(1,50)
            print(f"I guess {comp_number}!")
            attempts = attempts + 1
        print(f"I guessed your number in {attempts} attempts!")
    else:
        print("error: please pick between 1 and 50")

rng_game()