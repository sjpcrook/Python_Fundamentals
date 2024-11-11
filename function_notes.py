# def say_hello():
#     print("Hello")

# say_hello()

# def say_goodbye():
#     print("Goodbye")

# say_goodbye()

# def cash_withdrawal(amount, accnum):
#     print(f"You have withdrawn £{amount} from account: {accnum}")

# cash_withdrawal(200, 56283103)
# # print(amount) #!Causes an error

# def take_order(size, drink_type):
#     print(f"You have ordered a {size} {drink_type}.")

# take_order("large", "mocha")
# take_order("hot chocolate", "small")

# def take_order2():
#     drink_type = input("What type of drink?  > ")
#     size = input("What size of drink?  > ")
#     print(f"You have ordered a {size} {drink_type}.")

# take_order2()

balance = 500
def cash_withdrawal(amount, accnum):
    global balance
    print(f"Your current balance is £{balance}.")
    print(f"You have withdrawn £{amount} from account: {accnum}")
    balance = balance - amount
    print(f"Your new balance is £{balance}.")

cash_withdrawal(200, 38204829)
cash_withdrawal(100, 38204829)
