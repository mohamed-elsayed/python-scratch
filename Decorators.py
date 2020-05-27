# =================================================
################ Decorators     ###################
# =================================================

# class method is an example of decorator

# Higher order function 
# It is a function that return a nother function or accept a function as argument

# def sum(n, func):
#     total = 0 
#     for num in range(1, n+1):
#         total += func(num)
#     return total

# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# print(sum(3, cube)) 

# from random import choice 
# we can nest functions inside one a nother
# def greet(person):
#     def get_mood():
#         msg = choice (('Hello There ', 'Go away ', 'I love you '))
#         return msg
#     result = get_mood() + person 
#     return result

# print(greet("Toby"))

# def make_laugh_func(person):
#     def get_laugh():
#         l = choice(('HAHAHAHAH ', 'lol ', 'teheheh '))
#         return l
#     return get_laugh

# laugh_at = make_laugh_func("Linda ")
# print(laugh_at())


# Decorators: whats is ?
# They are functions
# They wrap other functions and enhance their behaviour
# They are examples of higher order functions
# They have their own syntax, using "@" (syntactic sugar)

# Decorators as functions

# def be_polite(fn):
#     def wrapper():
#         print("what apleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# def greet():
#     print("My name is Colt.")

# wrapped_greet = be_polite(greet)
# <class 'function'>
# greet = be_polite(greet)

# greet()
# wrapped_greet()

# Decorator Syntax
# @be_polite
# def greet():
#     print("My name is kandil")
# greet()

# we don not need to set greet=be_polite(greet)

# we are decorating our function with politeness !
#####################################################
# Functions with Different Signatures/ multiple arguments of decrated functions
# def shout(fn):
#     def wrapper(*args, **kwargs):
#         return fn(*args, **kwargs).upper()
#     return wrapper 

# @shout 
# def greet(name):
#     return f"Hi, I'm {name}"

# @shout
# def order(main, side):
#     return f"Hi, I'd like the {main}, with a side of {side}, please."

# print(order("burger", " fries"))
#####################################################
# using wraps for Preserving metadata
# This problem that decorated function does not maintaing 
# meta data but instead it will respond with the meta data 
# of the wrapper function 
# To overcome that behaviour we have to use wraps function 

# from functools import wraps
# def log_function_data(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         """I AM WRAPPER FUNCTION"""
#         print(f"you are about to call {fn.__name__}")
#         print(f"Here is the documentation {fn.__doc__}")
#         return fn(*args, **kwargs)
#     return wrapper 

# @log_function_data
# def add(x,y):
#     """" Adds two number together"""
#     return x+y

# print(add.__doc__)
# print(add.__name__)
# help(add)
#####################################################

# from functools import wraps 

# def ensure_no_kwargs(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             raise ValueError("No kwargs allowed!")
#         return fn(*args, **kwargs)
#     return wrapper 

# @ensure_no_kwargs
# def greet(name):
#     print (f"Hi there {name}")

# greet(name="kandil")
#####################################################
# speed testing our code as a use case for decorator

# from time import time 
# def speed_test(fn):
#     def wrapper(*args, **kwargs):
#         start_time =time()
#         result = fn(*args, **kwargs)
#         end_time = time()
#         print(f"Time Elapsed: {end_time - start_time}")
#         return result
#     return wrapper

# @speed_test
# def sum_nums_gen():
#     return sum(x for x in range(90000000))

# @speed_test
# def sum_nums_list():
#     return sum([x for x in range(90000000)])

# print(sum_nums_gen())
# print(sum_nums_list())
#####################################################
# Ensure first arg is of a certain value

# Not woring code just to illustrate something
# when we write
# @decorator 
# def func(*args, **kwargs):
    # pass

# we are really doing:
# func = decorator(func)

# when we write:
# @decorator_with_args(arg)
# def func(*args, **kwargs):
    # pass 
# we are really doing:
# func = decorator_with_args(arg)(func)

# so essentially we need an extra layer of function 
# because the argument that we are trying to pass in 
# from functools import wraps

# def ensure_first_arg_is(val):
#     def inner(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != val:
#                 return f"First argument needs to be {val}"
#             return fn(*args, **kwargs)
#         return wrapper
#     return inner

# @ensure_first_arg_is("burrito")
# def fav_foods(*foods):
#     print(foods)

# # print(fav_foods("burrito","ice_cream"))
# # print(fav_foods("ice_cream","burrito"))

# @ensure_first_arg_is(10)
# def add_to_ten(num1, num2):
#     return num1 + num2 

# # print(add_to_ten(10,12))
# # print(add_to_ten(15,12))
#####################################################
# # enforces types over function via decorator
# def enforce(*types):
#     def decorator(fn):
#         def new_func(*args, **kwargs):
#             # convert args into something mutable
#             newargs = []
#             for (a, t) in zip (args, types):
#                 newargs.append(t(a))
#             return fn(*newargs, **kwargs)
#         return new_func
#     return decorator

# @enforce(str, int )
# def repeat_msg(msg, times):
#     for tim in range(times):
#         print (msg)

# repeat_msg("mohamed", "5")

# @enforce(float, float)
# def divide(a, b):
#     print(a/b)

# divide("1", "4")
