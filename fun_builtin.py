# =================================================
################ Built-in Funs ####################
# =================================================

# lambda
# Anonymous function or function without name only in one line
# def square (num): return num * num 

# square2 = lambda num: num * num # save function to avariable
# print(square2(7))

# add = lambda a,b: a+b 
# print(square.__name__) # square
# print(square2.__name__) #  <lambda>

# use case:
# we need to pass parameter as a function and never use it again

# import tkinter as tk 

# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# def say_hi():
#     print("HELLO!")

# button = tk.Button( frame,
#                     text="CLICK ME",
#                     fg="red",
#                     command = say_hi)


# button = tk.Button( frame,
#                     text="CLICK ME",
#                     fg="red",
#                     command = lambda: print("HELLO!"))


# button.pack(side=tk.LEFT)
# root.mainloop()

# map:
# Astandard function that accepts at least two arguments, 
# a function and an "iterable"
# iterable - something that can be iterated over (lists, strings,
#  dictionaries, sets, tuples)
# runs the lambda for each value in the iterable and returns
# a map object which can be converted into another data structure

# nums = [1,2,3,4]
# doubles = list(map(lambda num: num* 2,nums))
# print(doubles)

# people = ["man", "medo", "kandil"]
# peeps = list(map(lambda name: name.upper(), people))

# print(peeps)

# filter:
# There is a lambda for each value in the iterable
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda

# l =[1,2,3,4]
# evens = list(filter(lambda x: x%2 == 0, l))
# print(evens)

# users = [
# 	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
# 	{"username": "katie", "tweets": ["I love my cat"]},
# 	{"username": "jeff", "tweets": []},
# 	{"username": "bob123", "tweets": []},
# 	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
# 	{"username": "guitar_gal", "tweets": []}
# ]
# #extract inactive users using filter:
# inactive_users = list(filter(lambda u: not u['tweets'], users))
# print(inactive_users)
# #extract inactive users using list comprehension:
# inactive_users2= [user for user in users if not user["tweets"]]
# print(inactive_users2)
# # extract usernames of inactive users w/ map and filter:
# usernames = list(map(lambda user: user["username"].upper(), 
# 	filter(lambda u: not u['tweets'], users)))
# print(usernames)
# # extract usernames of inactive users w/ list comprehension
# usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

# print(usernames2)

# Any and all
# all  - Return True if all elements of the iterable are truthy (or the iterable is empty)

# all([0,1,2,3]) # False
# all([char for char in 'eip' if char in 'aeiou'])
# all([num for num in [4,2,10,6,8] if num % 2 == 0 ]) # true

# any - Return True if any element of the iterable is truthy, If the iterable is empty , return False.

# import sys
# list_comp = sys.getsizeof([x*10 for x in range(1000)])
# gen_exp = sys.getsizeof(x*10 for x in range(1000))

# print("To do the same thing, it takes ...")
# print(f"List comprehension: {list_comp} bytes")
# print(f"Generator Expression: {gen_exp} bytes")

# sorted
# Returns a new sorted list from the items in iterables (list, dict, ...)
# we also can sort based on property of an object.
# more_num = [6,1,2,7,3]
# sorted(more_num) # Ascending
# sorted(more_num, reverse=True)

# users = [
# 	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
# 	{"username": "katie", "tweets": ["I love my cat"]},
# 	{"username": "jeff", "tweets": [], "color": "purple"},
# 	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
# 	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
# 	{"username": "guitar_gal", "tweets": []}
# ]

# # To sort users by their username
# sorted(users,key=lambda user: user['username'])

# # Finding our most active users...
# # Sort users by number of tweets, descending
# sorted(users,key=lambda user: len(user["tweets"]), reverse=True)

# # ANOTHER EXAMPLE DATA SET==================================
# songs = [
# 	{"title": "happy birthday", "playcount": 1},
# 	{"title": "Survive", "playcount": 6},
# 	{"title": "YMCA", "playcount": 99},
# 	{"title": "Toxic", "playcount": 31}
# ]

# # To sort songs by playcount
# sorted(songs, key=lambda s: s['playcount'])

# Max vs min
# max - return the largest item in an iterable or the largest of two or more arguments

# names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# # finds the minimum length of a name in names
# min(len(name) for name in names) # 3

# # find the longest name itself
# max(names, key=lambda n:len(n)) #Ollivander

# songs = [
# 	{"title": "happy birthday", "playcount": 1},
# 	{"title": "Survive", "playcount": 6},
# 	{"title": "YMCA", "playcount": 99},
# 	{"title": "Toxic", "playcount": 31}
# ]

# # Finds the song with the lowerest playcount
# min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# # Finds the title of the most played song
# max(songs, key=lambda s: s['playcount'])['title'] #YMCA

# reversed
# return the revese of iterator

# reversed("Hello") # list_reverseiterator object
# for char in reversed("hello world"):
#     print(char)

# ''.join(list(reversed("hello")))
# "hello"[::-1]

# len
# return the length of an object
# the argument may be a sequence ( string, tuple, list, range) or a collection (dict or set)

# "heelo".__len__()
# that what is happenening behind the seen when calling len , __len__() method is called
# we can define our own __len__() method for the class that define the entity to describe how the length would be.

# class SpecialList:

#     def __init__(self, data):
#         self.__data = data 
    
#     def __len__(self):
#         return 50

# l1 = SpecialList([1,40,40,100])
# l1.__len__()
# print(len(l1))

# abs - 
# sum - takes an iterable and an optional start
# return the sum of start and theitems of an iterable from the left to the right and returns the total 
# start defaults to 0 
#  sum ([1.2.3],10) --> 16
# sum([1,2,3],-6) --> 0
# sum (['hi','there'],'lol') --> error
# ''.join('hi','there') --> works

# round
# return number rounded to n digits precesion after the decimal point. if ndigits is omitted or is none , it returns the nearest integer to its input.

# zip 
# make an iterator that aggregate elements from each of the iterables.
# returns an iterator of tuples , where thr i-th tuple contains the i-th element from each of the argument sequence or iterables
# The iterator stops when the shortest input iterable is exhausted

# first_zip = zip([1,2,3],[4,5,6]) # return zip object generator
# print(list(first_zip)) # [(1,4),(2,5),(3,6)]
# print(dict(first_zip)) # {1:4, 2:5, 3:6}
# five_by_two = [(0,1),(1,2),(2,3),(3,4),(4,5)]
# list(zip(* five_by_two)) # [(0,1,2,3,4),(1,2,3,4,5)]

midterms =[80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']

final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)

grades_names = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
            )

        )
)
avvg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)
