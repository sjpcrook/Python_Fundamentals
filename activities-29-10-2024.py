#Activity 1
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")

#Activity 2

#.lower()
#This method turns all letters into their lower case counterparts.
text = " HELLO, WORLD. My nAMe is Sam! "
lowercase = text.lower()
print(lowercase) 

#.capitalize()
#This method turns all letters into their lower case counterparts except the first character, which becomes a capital if a letter.
capital = text.capitalize()
print(capital)
capitaltest = " hello"
print(capitaltest.capitalize())

#.count()
#This method takes a string as an input and returns how many times it appears in the original string as an integer.
counting = text.count("M")
print(counting)
counttest = "M M MM MMM MMMM" 
print(counttest.count("MM")) #Counts 4 at "m m MM MMm MMMM"

#.find()
#This method takes a string as an input and returns the first position it appears in the original string as an integer.
finding = text.find("M")
print(finding)
finding2 = text.find("Me") # Returns the position of the M in Me
print(finding2)

#.replace()
#This method takes two strings as input and, wherever the first string appears in the original, it is replaced by the second.
replacement = text.replace("Sam", "Michael")
print(replacement)

#.strip()
#This method removes the given string (or spaces if empty) at the start and end of the original string
stripped = text.strip()
print(stripped)
print(len(text))
print(len(stripped))