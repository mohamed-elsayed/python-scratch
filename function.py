# =================================================
################  Functions #######################
# =================================================
# Describe what a function is and how they are useful
# Explain exactly what the return keyword does and some of
# the side effects when using it
# Add a parameters to functions to output difference data 
# Define and diagram how scope works in a function 
# Add keyword arguments to a function 

# What is a function ? 
#  a process for executing a task 
# IT can accept input and return an output
# useful for executing similar procedures over and over

# why use functions?
# Stay DRY - Do not repeat yourself
# Clean up and prevent code duplication 
# abstract away code for other users
#     Imagine if you had to rewrite the "print()" function
#     for every program you wrote.

# Function structure
# def name_of_function():
#     block of runnable code

# Returning values from functions
# return value
    # exits the function
    # outputs whatever value is placed after the return keyword
    # pops the function off of the call stack

# from random import  random 

# def flip_coin():
#     r = random()
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# print (flip_coin())

# def square(num):
#     return num * num

# parameters
# variables that are passed to a function - think of them as
# placeholders that get assigned when you call the function 
 # parameter is a variable in method definition 
 # when a method is called , the arguments are the data you pass
 #  into the method's parameters
 # parameter is a variable in the declaration of function
 # argument is the actual value of this variable that gets
#    passed to function
# 
# common return mistakes:
#  unnecessary else

# Default parameters
#
# def exponent(num, power=2):
#     return num ** power

# why?
# Allows you to be more defensive
# Avoid errors with incorrect parameters

# what can default parameters be?
# Anything! Functions, lists, dictionaries, strings, boolean

# def add(a,b):
#     return a+b 

# def math(a,b,fn =add):
#     return fn(a,b) 

# def subtract(a,b):
#     return a-b 

# default parameters are the list ones in the definition

# keyword arguments:
# passing variables by name and then order does not matter

# you may not see the value , but it is useful when passing a dictionary
# to a function and unpacking it's valuse 

# Different from Default parameters
# when you define a function and use an = you are
# setting a default parameter

# when you invoke a function and use an = you 
# are making a keyword argument 

# scope
# where our variables can be accessible?
# variabales created in functions are scoped in that function!

# total =0 
# def increment():
#     total += 1 # Error referenced before assigned # global total 
#     return total
# increment()
# total inside function cause error as it is unknown

# nonlocal
# let us modify a parent's variables in a child function

# def oueter():
#     count =0 
#     def inner():
#         nonlocal count 
#         count +=1
#         return count 
#     return inner()

# Documenting functions
# use """ """
# essential when writing a complex function

# def say_hello():
#     """ A simple function that return a string hello"""
#     return "Hello"

# say_hello.__doc__ 

# Introduction and args
# Use the * and ** operator as parameters to a function 
# and outside of a function

# Leverage dictionary and tuple unpacking to create more 
# flexible functions

# *args
# A special operator we can pass to functions
# Gathers remaining arguments as a tuple
# This is just a parameter - you can call it whatever
# you want !
# It is a tuple

# def sum_all_nums(num1, num2, num3, num4):
#     return num1+num2+num3+num4 

# def sum_all_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# def ensure_correct_info(*args):
#     if "medo" in args and "kandil" in args:
#         return "Welcome back medo!"
#     return "Not sure who you are"
# print(ensure_correct_info(1,True,"medo","kandil"))

# **kwargs
# A special operator we can pass to functions
# Gathers remaining keyword arguments as a dictionary
# This is just a parameter - you can call it whatever you want!

# def fav_colors(**kwargs):
#     print(kwargs)

# fav_colors(colt= "purple", ruby="red", ethel="teal")

# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f" {person}'s favorite color is {color} ")
# fav_colors(colt= "purple", ruby="red", ethel="teal")

# parameter ordering 
# parameters, *args, defaultt parameters, **kwargs

# def display_info(a,b, *args, instructor="Colt", **kwargs):
#     return [a,b,args,instructor,kwargs]

# print(display_info(1,2,3, last_name="Steele", job="Instructor"))

# a - 1
# b -2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": " Instructor"}
# [1,2,(3,),{'last_name': "Steele", "job": " Instructor"}]

# using * as an Argument: Argument unpacking
# we can use * as an argument to a function to "unpack" values

# def sum_all_nums(*args):
#     print(args)
#     total =0
#     for num in args:
#         total += num 
#     print(total)

# nums = [1,2,3,4,5,6] # or nums = (1,2,3,4,5,6)
# sum_all_nums(*nums)

# using ** as an argument: Dictionray unpacking
# def display_names(first, second):
#      print(f"{first} says hello to {second}")

# names = {"first": "Colt", "second": "Rusty"}

# display_names(**names)

# def add_and_mul(a,b,c,**kwargs):
#     print(a+b*c)
#     print("Other Stuff ...")
#     print(kwargs)

# data = dict(a=1,b=2,c=3,d=55,name="Tony")

# add_and_mul(**data, cat="blue")