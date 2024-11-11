
#*Activity 1

# fav_websites = [
#     "Youtube",
#     "Twitter",
#     "Reddit"
# ]
# print(fav_websites)
# fav_websites.extend(["Facebook", "Instagram"])
# print(fav_websites)
# fav_websites.pop()
# print(fav_websites)

#*Activity 2
#* Remove - Gets rid of the first occurence of a given item in a list
# shoplist = ["eggs", "fruit", "pasta", "eggs", "cheese", "eggs"]
# #print("Original: ", shoplist)
# shoplist.remove("fruit")
# print("Removed: "shoplist)

# #* Reverse - Reverses the order of a list
# shoplist = ["eggs", "fruit", "pasta", "eggs", "cheese", "eggs"]
# #print("Original: ", shoplist)
# shoplist.reverse()
# print("Reversed: ", shoplist)

#* Sort - Sorts the items in a list into alphabetical/numerical order, or according to a key
# shoplist = ["eggs", "fruit", "pasta", "eggs", "cheese", "eggs"]
# #print("Original (shop): ", shoplist)

# shoplist.sort()
# print("Sorted by default: ", shoplist)

# shoplist.sort(key = len)
# print("Sorted by length: ", shoplist)

# numlist = [4,7,12,9,4,1,-5,0,12,22]
# #print("Original (num): ", numlist)

# numlist.sort(reverse=True)
# print("Reverse sort: ", numlist)

#* Count - Returns how many times an item appears in a list
# shoplist = ["eggs", "fruit", "pasta", "eggs", "cheese", "eggs"]
# #print("Original: ", shoplist)
# print("Number of eggs: ", shoplist.count("eggs"))

#* Extend - Adds more items to the end of a list
# shoplist = ["eggs", "fruit", "pasta", "eggs", "cheese", "eggs"]
# #print("Original: ", shoplist)
# numlist = [4,7,12,9,4,1,-5,0,12,22]
# shoplist.extend(numlist)
# print("Extended: ", shoplist)



#*Activity 3

# countries = ["England", "Spain", "Ethiopia", "Iran"]
# languages = ["English", "Spanish", "Amharic", "Farsi"]

# country_lang = {countries[i] : languages[i] for i in range(len(countries))}
# print("The dictionary for countries and their languages: ", country_lang.items())

#*Activity 4

# baby_animals = {
#     "Lion" : "Cub",
#     "Dog" : "Puppy",
#     "Cat" : "Kitten",
#     "Frog" : "Tadpole"
# }

# animal = input("What animal would you like to search for?  > ").capitalize()
# print(f"The baby version of {animal} is {baby_animals.get(animal, "not in this dictionary")}")