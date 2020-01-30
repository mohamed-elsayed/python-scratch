# =================================================
################  LISTS ###########################
# =================================================
# What is a list ?
# It is just a collection or grouping of items!

# Objective :
# Describe , create and access  a list data structure
# Use built in methods to modify and copy ists.
# Iterate over lists using loops and list comprehensions
# Work with nested lists to build ore complex data structures
# How are lists useful ?
# A fundamental data structure for organizing collections of items.
# comma seperated values, or even variables.
# tasks = ["Install python","learn python"]

# len(tasks) #return number of items in a list 
# It is abuilt in function (method)

# create a list using list() built in function.

# list(range(1,4))
# [1,2,3,4]

# accessing values in a list
# like ranges , lists always start counting at zero.
# friends = ["mohamed", "ali","kandil"]
# print (friends["1"]) # return ali
# accessing values from the End , index backwards.
# print (friends[-1]) # return kandil

# checking if the value in a list use the in operator
# "hany" in friends
# False

# accessing all values in a list
# using for loop
# for frind in friends:
#     print(frind)

# using while loop
# numbers = [1,2,3,4]
# i =0
# while i < len(numbers):
#     print (numbers[i])
#     i +=1

# list methods
# working with lists is very common

# append # add an item to the end of the list
# data = [1,2,3]
# data.append(4)
# print (data)
# [1,2,3,4]

# extend # add to the end of the list all values passed to extend
# first_list = [1,2,3,4]
# first_list.append(5,6,7,8) # does not work !
# first_list.append([5,6,7,8])
# print (first_list) # [1,2,3,4,[5,6,7,8]]

# correct_list = [1,2,3,4]
# correct_list.extend([5,6,7,8])
# print(correct_list) #[1,2,3,4,5,6,7,8] one level list not nested
# to add more items to the list use extend

# insert
# inser item at a given position
# first_list = [1,2,3,4]
# first_list.insert(2, "HI")
# print (first_list)#[1,2,"HI",3,4]
# first_list.insert(-1, "The end!")
# print(first_list)#[1,2,"HI",3,"The end!",4]

# clear
#first_list = [1,2,3,4]
# first_list.clear()
# print(first_list) # []

# pop
# remove the item at the given position in the list and return it.
# if no index is specified, removes and returns last item in te list.
# first_list = [1,2,3,4]
# first_list.pop() # 4
# first_list.pop(1) # 2 remove item at index 1
# print (first_list) #[1,3]


# remove
# remove the first item from the list hose value is x
# throws a ValueError if the item is not found.
# first_list = [1,2,3,4,4,4]
# first_list.remove(2)
# print(first_list) # [1,3,4,4,4]
# first_list.remove(4)
# print(first_list) # [1,3,4,4]

# index
# return the index of the specified item in the list
# numbers = [5,6,7,8,9,10]

# numbers.index(6) # 1 return the index of first occurence of value
# numbers.index(9) # 4

# numbers = [5,5,6,7,5,8,8,9,10]
# numbers.index(5) # 0 
# numbers.index(5, 1) # 1 return the index after the first occurence 
# numbers.index(5,2) # 4 return the index after the second occurence

# numbers.index(8,6,8) #6 return the index of occurence between index  and 8

# count
# return the number of times x appears in the list  
# numbers = [1,2,3,4,3,2,1,4,10,2]
# numbers.count(2) # 3
# numbers.count(21) #0
# numbers.count(3) # 2

# reverse 
# reverse the elemenrs of the list (in-place)
# first_list = [1,2,3,4]
# first_list.reverse() # no return value , changes in place
# print(first_list) # [4,3,2,1]

# sort
# sort the items f the list in place in ascending order 
# another_list = [6,4,1,2,5]
# another_list.sort() # return nothing 
# print (another_list) #[1,2,4,5,6]

# join 
# used to convert list to string
# technically a string method that takes an iterable argument
# concatenates a copy of the base string between each item of the iterable
# return a new string
# can be used to make sentences out of a list of words by
# joining on a space 
# words =[ 'codin', ' is', 'fun']
# ' '.join(words) # 'coding is fun '

# name = [ ' Mr' ,'Steel']
# '.'.join(name) # Mr.steele

# slicing
# make new lists using slices of the old list!
# some_list[start:end:step]
# first_list = [1,2,3,4]
# first_list[1:] # from index 1 to the end [2,3,4]
# first_list[3:] # [4]

# slicing back from the end slice : start
# first_list[-1:] # [4]
# first_list2[:]
# first_list == first_list2 # True 
# first_list is first_list2 # false
# same values but different objects due to copying

# The index to copy up to (exclusive ounting) slice: end

# with negative numbers , how many items to exclude from the end i.e 
# indexing by counting backwards.

# first_list = [1,2,3,4]
# first_list[:-1] # [1,2,3]
# first_list[1:-1] # [2,3]

# slice :step
# step in python is basically the number to count at a time
# same as astep with range
# with negative numbers, reverse the order

# Tricks with slices 
# Reversing lists / strings
# string = "This is fun!"
# string[::-1]

# modifying portion of a list
# numbers = [1,2,3,4,5]
# numbers[1:3] = ['a','b','c']
# print(numbers) # [1,'a','b','c', 4,5]

# swapping values
# names = ["james", "medo"]
# names[0], names[1] = names[1], names[0]

# print(names) # ["medo", "james"]

# practical examples: shuffling, sorting (in-place), algorithms


# list comprehension
# The syntax
# [----- for ---- in ------- ]
#   var-name for same-var-name in iteratable element

# nums = [1,2,3]
# [x*10 for x in nums] # [10,20,30]

# list comprehension vs looping
# numbers = [1,2,3,4,5]
# doubled_numbers = []

# for num in numbers:
#     doubled_number = num *2
#     doubled_numbers.append(doubled_number)
# print(doubled_numbers)

# numbers = [1,2,3,4]
# doubled_numbers = [num *2 for num in numbers ]
# print(doubled_numbers)

# name = 'colt'
# [char.upper() for char in name ] # ['C','O', 'L','T']

# [num* 10 for num in range(1,6)] # [10,20,30,40,50]
# [bool(val) for val in [0,[],'']] ## [False , False, False]

# numbers = [1,2,3,4,5]
# string_list = [ str(num) for num in numbers ] #['1','2','3','4','5']

# list comprehension with conditional logic
# numbers = [1,2,3,4,5,6]
# evens = [ num for num in numbers if num % 2 == 0]
# odds = [ num for num in numbers if num % 2 != 0 ]
# [num * 2 if num % 2 == 0 else num/2 for num in numbers ]
# # [0.5, 4, 1.5, 8, 2.5, 12]

# with_vowels = "This is so much fun!"
# '...'.join(["cool","dude"]) # cool...dude
# [char for char in with_vowels if char not in "aeiou"]#['T','s',' ','s',...]
# ''.join(char for char in with_vowels if char not in "aeiou")

# nested list
# list can contains any kind of element, even other lists
# why ?
# complex data structures - matricies
# Games Boards / mazes
# Rows and columns for visulaization
# tabulation and grouping data

# Accessing Nested lists
# listed_list = [[1,2,3],[4,5,6],[7,8,9]]
# listed_list[2][1] # 8
# listed_list[-1][1] # 8
# listed_list[2][-2] # 8

# printing values in nested lists

# for l in listed_list:
#     for val in l :
#         print(val)

# nested list comprehension

# [[print(val) for val in l ] for l in nested_list]

# board = [[num for num in range (1,4)] for val in range(1,4)]
# [["x" if num % 2 != 0 else "o" for num in range (1,4)]for val in range (1,4)]
# [["x","o","x"],["x","o","x"],["x","o","x"]]

# Recap
# lists are fundamental dat structures for ordered information
# lists can be include any type , eb=ven other lists!
# we can modify lists using a variety of methods
# slices are quite useful when making copies of lists
# list comprehension is used everywhere when iterating over
    # lists, strings, ranges and even more data types!
# nested lists are essential for building more complex data
# structures like matricies , game boards and mazes
# swapping is quite useful when shuffling or sorting