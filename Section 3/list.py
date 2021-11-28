# Lists

names = ["Fred", "Barney", "Wilma", "Betty"]

print (names)

print (names[1])


nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print (nums[0])

nums[2] = 2

print(nums)

print (nums * 3)

fruits = ["apple", "mango", "peach", "orange"]

# in

if "apple" in fruits:
    print ("We have an apple")

# append
    
fruits.append("pear")
print (fruits)

# len

print (len(fruits))

# insert

fruits.insert(1, "banana")
print(fruits)

# index

print(fruits.index("mango"))
# print(fruits.index("kiwi")) - gives an error because kiwi is not in the list



