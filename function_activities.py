
#*Activity 1

# def birthday(name):
#     print(f"Happy Birthday to You!\nHappy Birthday to You!\nHappy Birthday dear {name}!\nHappy Birthday to You!\n")

# birthday("Sam")

#*Activity 2

order_count = 0

def take_order(size, topping1, topping2):
    global order_count
    print("{} pizza with {} and {}".format(size, topping1, topping2))
    order_count += 1
    print("There have been {} order(s) so far.".format(order_count))

take_order("large", "pineapple", "ham")
take_order("small", "onion", "pepperoni")

#*Activity 3

dataset = [34,67,5,81,2,45,9,23,55,41,42,84,109, 109, 109]

def mean_finder(numbers):
    length = len(numbers)
    mean = 0
    for i in numbers:
        mean = mean + i
    mean = mean/length
    print(mean)

mean_finder(dataset)

def median_finder(numbers):
    length = len(numbers)
    half = length/2
    numbers.sort()
    if length%2 == 0:
        median = (numbers[int(half) - 1] + numbers[int(half)])/2
    else:
        median = numbers[int(half-0.5)]
    print(median)

median_finder(dataset)
median_finder([1,2,3,4,5,6,7,8,9])
median_finder([1,2,3,4,5,6,7,8,9,10])

