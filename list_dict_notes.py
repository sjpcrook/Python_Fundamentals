# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Mocha"
# ]


# print("List: ", coffee_order)
# print("Second item of list: ", coffee_order[2])

# #*Change a specific item in the list
# coffee_order[2] = "Charlie - Hot Chocolate"
# print("New second item: ", coffee_order[2])

# #*Find the length of a list
# print("Length of list: ", len(coffee_order))

# #*Append - Add item to end
# coffee_order.append("Diane - Cappuccino")
# print("Appended list: ", coffee_order)

# #*Insert - Add item in a specific position
# coffee_order.insert(1, "Amelia - Tea")
# print("Inserted list at [1]: ", coffee_order)

# #*Pop - Remove an item of a list, defaults to the last item
# coffee_order.pop()
# print("List popped at end: ", coffee_order)

# coffee_order.pop(1)
# print("List popped at [1]: ", coffee_order)



# things_i_see = [
#     "Lamp",
#     "Notebook",
#     "Phone Charger"
# ]


# shopping_list = [    "apple",    "carrot",    "pizza",    "carrot",    "dog food",    "orange juice",    "egg",    "kale",    "carrot",    "kale",    "orange juice",    "kale",    "toilet roll",    "stamps",    "noodles",    "pasta sauce",    "egg",    "pasta sauce"] 


#*Count - Returns the number of times an item appears in a list
# print(f"You have ordered {shopping_list.count("egg")} egg(s).")
# print(f"You have ordered {shopping_list.count("kale")} lot(s) of kale.")
# print(f"You have ordered {shopping_list.count("stamps")} stamp(s).")
# print(f"You have ordered {shopping_list.count("carrot")} carrot(s).")
# print(f"You have ordered {shopping_list.count("orange juice")} orange juice(s).")

# item = input("What item would you like to count?  > ").lower()
# print(f"You have ordered {shopping_list.count(item)} {item}(s).")

#*Dictionaries - Key : Value
#* The key is immutable, the value is mutable

capital_cities = {
    "England" : "London",
    "Scotland" : "Edinburgh",
    "Wales" : "Washington",
    "Northern Ireland" : "Belfast",
    "Ireland" : "Dublin",
    "Wales" : "Cardiff"
}
#*If a key is inputted multiple times, only the last input is saved but keeps position of the first

# print("The dictionary is: ", capital_cities)
# print("Capital of Scotland: ", capital_cities["Scotland"])
# print("Capital of Wales (not Washington): ", capital_cities["Wales"])

baby_animals = {
    "Lion" : "Cub",
    "Dog" : "Puppy",
    "Cat" : "Kitten",
    "Frog" : "Tadpole"
}
# print("Baby cat: ", baby_animals["Cat"])

#* Keys - returns a list of the keys of a dictionary
# print("Keys of baby animals: ", baby_animals.keys())

#* Values - returns a list of the values of a dictionary
# print("Values of baby animals: ", baby_animals.values())

#*Items - returns a list with each key and value paired
# print("Items of baby animals: ", baby_animals.items())

#*Get - See the associated value of a key, or None/message if not a key
# print("Check for cow: ", baby_animals.get("Cow", "Key does not exist for that!"))

#*Set default - Add a new key-value pair to dictionary, does not change existing values
baby_animals.setdefault("Horse", "Foal")
baby_animals.setdefault("Dog", "Baby dog")
print(baby_animals)