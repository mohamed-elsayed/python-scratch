# =================================================
################ Tuples/sets #######################
# =================================================
# Describe , create and access tuples and sets
# use built in methods to modify sets and access values in tuples
# Iterate over sets using loops and set comprehensions

# what is a tuple?
# an ordered collection or grouping of items

# numbers = (1,2,3,4)
# It is immutable # can not be changed after creation

# x= (1,2,3)
# 3 in x# True
# x[0] = "change Item" # TypeError: 'Tuple' object does not support item assignement

# why use a tuple?
# Tuples are fster than lists
# It makes your code safer
# valid keys in a dictionary
# some methods return them to you like .items

# creating and accessing
#create using () or tuple function
# accessing is just like a list!
# can contain duplicate data

# note: can not use list as a key in dict
# key must be immutable data type to be hashable

# looping 
# we can use a for loop to iterate over tuple 

# for month in months:
#     print(month)

# methods

# count
#return the number of items a value appears in tuple

# index
# return the index at which a value is founf in atuple

# t=(1,2,3,3,3)
# t.index(1) # 0
# t.index(5) # valueError: tuple.index(x): x not in tuple
# t.index(3) # 2 -only the first matching index is returned

# nested tuple
# nums = (1,2,(3,4),5)
# # same slicing like list

# =================================================
################ Tuples/sets #######################
# =================================================
# sets are like formal mathematical sets
# sets do not have duplicate values
# Elements in sets are not ordered
# you can not access items in a set by index
# sets can be useful if you need to keep track of a collection of
# elements , but do not care about ordering, keys or values
# and duplicate

# creating and access
# s = set({1,2,3,4,5})
# s= {1,2,3,4,5}

# 4 in s # True

# accessing all values
# for thing in s:
#     print(thing)

# cities = ["Los Angles", "Kyoto", "solo", "Los Angles"]
# print(set(cities)) # to remove duplicat

# set methods
#add
#adds element to a set. If the element is already in the set 
# the set does not change

# remove
# remove a value from the set 
# return a keyError if the value is not found

# copy
# create a copy of the set
# different object in memory

# clear 
# remove entire content of set

# set Math
# intersection &
# symmetric_difference
# union |

# set comprehension
# {x**2 for x in range(20)} #set
# {x:x**2 for x in range(10)} # dict

# def are_all_vowels_in_string(string):
#     return ({char for char in string if char in 'aeiou'})

#Recap
# tuples are ordered collections of elements , they are immutables
# tuples are faster than lists and useful for protecting data
# sets are un ordered collections of unique values
# sets and tuples can be created with {} and () or the
# set() or the tuple() function
# set comprehension is useful when converting other data types to a set.