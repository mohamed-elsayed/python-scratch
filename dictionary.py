# =================================================
################ dictionary #######################
# =================================================
# Describe, create, and access all a dictionary data structure
# use built in methods to modify and copy dictionaries
# iterate over dictionaries using loops and dictionary comprehensions
# compare and constrast dictionaries and lists.

# limitations of lists
# not enough information, just a collection
# we want to describe this data in more details

# shoping cart 
#     Item:
#         name 
#         quantity
#         price 
#     Item:
#         name 
#         quantity
#         price 
# so, how to describe this data in data structure format
# we use a dictionary

# It is a data structure that consists of key value pairs
# we use the keys to describe our data and the values to represnt the data

# instructor ={
#     "name": "colt",
#     "own_dog": True,
#     "num_courses": 4,
#     "favourite_language": "Python"
# }

# keys and values seperated by colon :
# our keys are almost always numbers or strings

# Another approach is to use the dict function
# you assign values to keys by passing in keys and values seperated by an =

# another_dict = dict(key1 = 'value1', key2 = 'value2)

# accessing the individual values
# instructor["name"] # 'colt'
# if key does not exist raise keyError exception

# lets get all the values
# use.values()

# for val in instructor.values():
#     print(val)
#     # dict_values(['colt', 'True',...])
# # use .keys()
# for key in instructor.keys():
#     print(key)
#     # dict_keys(['name', ...])

# Accessing all keys and values
# use .items # return a list of tuples (key, value)
# for key,value in instructor.items():
#     print (f"key is {key} and value is  {value}")

# In dict no gurantee for order

# Does the dictionary has a key?
# "name" in instructor # True

# Does the dictionary has a value?
# "4" in instructor.values()

# Dictionary Methods
# clear
# clear all the keys and values in a dictionary

# instructor.clear()

# Copy
# d = dict(a=1,b=2)
# c= d.copy()
# c is d # False

# fromkeys
# create key-value pairs from comma seperated values
# {}.fromkeys("a","b") # {'a':'b'}
# {}.fromkeys(['name','score']) #
# more beneficial to create a default dictionary
# new_user = {}.fromkeys(['name','score','email','profile bio'], 'unknown')
# print(new_user)
# {'name': ' unknown', 'score': 'unknown', ...}

#  new_user.fromkeys('phone','unknown')
#  # {'p':'unknown','h':'unknown',...}

# new_user.fromkeys(range(1,4),'unknown')


# get
# retrieve a key in an object and return None instead of
# a keyError if the key does not exist

# instructor.get('name')
# instructor.get('email') # None

# pop
# Takes a single argument corresponding to a key and removes
# that key-value pair from the dictionary .
# return the value corresponding to the key that was removed.

# d = dict(a=1,b=2,c=3)
# d.pop() #TypeError : pop expected at least 1 argument, get 0
# d.pop('a') # 1
# d # {'b': 2 , 'c': 3}
# d.pop('e') # keyError

# popitem
# remove a random key from dict, takes no argument

# update
# update keys and values in a dictionary with a nother
# set of key value pairs

# first = dict(a=1,b=2,c=3,d=4)
# second = {}

# second.update(first) # take everything in first and put in second
# overwrite the key that are there with the new value

# second.update({}) # nothing happened

# playlist modeling
# playlist = {
#     "name":"medo",
#     "title":"rap songs",
#     "songs":[
#         {
#             "title":'song1',
#             'artist': ['blue 1'],
#             'duration':2.5
#         },
#         {
#             "title":'song2',
#             'artist': ['blue 1','kitty'],
#             'duration':2.5
#         }
#     ]
# }
# total_len = 0
# for song in playlist['songs']:
#     total_len += song['duration']
# print(total_len)

# Dictionary comprehension
# the syntax
# {------:----- for ------- in --------}
# iterate over keys by default
# to iterate over keys and values use .items

# numbers = dict(first =1, second =2, third=3)
# squared_numbers = {key : value**2 for key,value in numbers.items()}

# {num: num**2 for num in [1,2,3,4,5]}
# str1= 'ABC'
# str2 ='234'
# combo = {str1[i]: str2[i] for i in range(0,len(str1))}

# conditional logic with dictionaries

# num_list = [1,2,3,4]
# {num:("even" if num %2 == 0 else "odd") for num in num_list}
