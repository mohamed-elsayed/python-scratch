# =================================================
################ debugging     ####################
# =================================================

# Explain common errors and how they occur in python 
# Use pdb to set breakpoints and step through code
# use try and except blocks to handle error

# SyntaxError
# Occurs when python encounters incorrect syntax (something it does not parse).
# Usually due to typos or not knowing python well enough

# def first:
# None =1 
# return 

# NameError
# This occurs when a variable is not defined,.e.
# It has not been assigned

# TypeError
# Occurs when 
# An operation or function is applied to the wrong type
# python can not interpret an operation on two data types
# len(5)
# TyperError: object of type 'int' has no len()

# "awesome" + []
# TyperError: can not concatenate 'str'and 'list' objects.

# IndexError
# Occurs when you try to access an element in a list using an invalid index
# i.e. one that is outide the range of the list or string

# list = ["hello"]
# list[20]

# ValueError
# This occurs when a built-in operation or function receives an argument that has the right 
# type but an inappropriate value

# KeyError
# This occurs when a dictionary does not have a specific key

# AttributeError:
# This is occurs when a variable does not have an attribute
# "awesome".foo
# Attribute: 'str' object has no attribuite 'foo'


# Raise your own exception:
# using raise keyword
# raise ValueError("messages!")

# def colorize(text, color):
#     if type (text) is not str:
#         raise TypeError("text must be instance of str")
#     print (f"printed {text} in {color}")

# colorize("hello", "red")
# colorize(10, "red")

# def colorize(text, color):
#     colors = ("cyan", "yellow", "blue", "green")
#     if type (text) is not str:
#         raise TypeError("text must be instance of str")
#     if color not in colors:
#         raise Exception  # generic exception
#     print (f"printed {text} in {color}")

# colorize("hello", "red")
# colorize(10, "red")

# Handle Errors!
# try , except block
# try:
#     foobar
# except NameError as err:
#     print("Problem")
# print ("After the try")

# Why not catch them all?
# try:
#     colt
# except:
#     print(" You tried to use ")


# def get(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return None

# d = {"name" "ricky"}
# get(d, "name")

# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass # will run when except not running 
# finally:
#     pass # will run no matter what

# try:
#     num = int(input("please enter a number : "))
# except:
#     print(" That is not a number!")
# else:
#     print("Iam in the else")
# finally:
#     print("Runs no matter what")

# while True:
#     try:
#         num = int(input("please enter a number : "))
#     except ValueError:
#         print(" That is not a number!")
#     else:
#         print("Good job you entered the number!")
#         break
#     finally:
#         print("Runs no matter what")
    
# print("Rest of the game logic Runs")

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err:
# 		print("a and b must be ints or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except (ZeroDivisionError, TypeError) as err:
# 		print("Something went wrong!")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")



# print(divide(1,2))
# print(divide(1,'a'))
# print(divide(1,0))

# debugging with pdb
# to set breakpoints in our code we can use pdb by inserting this line:
# import pdb
# pdb.set_trace() # pause to interacte with code

