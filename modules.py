# =================================================
################   modules     ####################
# =================================================
# Objesctives
# Define what a module is
# import code from built-in modules
# import code from other files 
# import code from external modules using pip
# describe common modules patterns
# describe the request/response cycle in HTTP 
# use the request module to make requests to web apps

# Why use modules
# keep python files small
# reuse code across multiple files by importing
# A module is just a python file!

# Built in modules Examples
# Google for them python site contains many nad indexed

# import random 

# print(random.choice(["apple", "banana", "cherry", "durian"]))
# random.shuffle(["apple", "banana", "cherry", "durian"])

# import random as rand 
# giving an alias for the name of the module 


# importing parts of a module 
# The form keyword lets you import parts of the module 
# handy rule of thumb : only import what you need 
# If you still want to import everything you can also use
# the form module import * pattern 

# from random import choice, randint

# print(choice(["apple", "banana", "cherry", "durian"]))

# Different ways to import 
# import random
# import random as rand 
# from random import * 
# from random import choice, randint
# from random import choice as ch, shuffle as mix_up_fruite


# custom modules

# you can import from own code too
# The syntax is the same as before
# important from the name of the python file

# # file1.py
# def fn():
#     return "do fun"

# # file2.py
# from file1 import fn 

# External Modules

# pypi : python package index contribution from developers

# you can download external modules using pip

# pip
# package management system for pythin
# python3 -m pip install name-of-package

# import termcolor
# dir(module) : list names comes with module or object
# help(module): show documwntion of module

# text = termcolor.colored("Hello There", color="yellow",on_color="on_green")
# print(text)

# import pyfiglet 

# msg = str(input("what would you like to print: "))
# color = input("what is the color:")

# valid_colors =("red", "green", "yellow", "blue", "magenta", "cyan", "white")

# if color not in valid_colors :
#     color = "magenta"


# result =pyfiglet.figlet_format(msg)
# col = termcolor.colored(result, color=color)
# print(col)


# autopep8 
# style guide for code : identation, spaces, empty lines ...
# python3 -m pip install autopep8
# autopep8 --in-place name-of-file

# autopep8 --in-pace -a -a name-of-file # -a : for aggressive

# __name__ variable 
# Special property
# when run , every python file has a __name__ variable
# If the file is the main file being run, its value is "__main__"
# otherwise its value is the file name

# import revisited
# when you use import , python ...
# 1- Tries to find the module (if it fails, It throws an errors)
# 2- Runs the code inside of the module being imported

# To prevent this, Ignore code om import
# if __name__ == __main__:
    # code


