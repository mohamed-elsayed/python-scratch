# =================================================
################    OOP        ####################
# =================================================

# Objective 
# Define what OOP
# Understand encapsulation and abstraction
# Create classes and instances ans attach methodsand properties to each 

# What is OOP ?
# It is a methos of progamming that attempts to model some process
# or thing in the world as a class or object

# class - a blueprint for objects. Classes can contain methods
# (functions) and attributes (similar to keys in a dict).

# Instance - objects that are constrcted from a class blueprint
# that contain their classe's methods and properties. 

# Why OOP ?
# With OOP, the goal is to encapsulate your code into 
# logical , hierarical grouping using classes so that
# you can reason about code at a higher level.

# Example 
# say we want to model a gme of poker in our program.
# we could have the following entities:
# Game, Player, Card, Deck, Hand, Chip, Bet
#  Each entity can be its own class

# Card Deck possible implementaion (Pseudocode)
# Deck {class}

# _cards {private list attribute} # no access directly from code outside, not expose
    # python do not distinct about private or public
    # It is just convention, nothing prevent you from accessing these vars.
# _max_cards { private int attribute}
# shuffle  {Public method}
# deal_card {public method}
# deal_hand {public method}
# count {public method}

# Encapsulation
# the grouping of public and private attributes and
# methods into a programming class, making abstraction possible

# Example
# Designing the Deck Class , I make cards a private attributes (a list)
# I decide that the length of the cards should be accessed 
# via a public method called Count() -- i.e Deck.count()

# Abstraction
# Exposing only "relevant" data in a class interface , hiding
# private attributes and methods (a.k.a inner working)

# Creating a class    

# class Vehicle(object):

#     def __init__ (self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# classes in python can have a special __init__ method,
# which gets called every time you create an instance of the class (instantiate)

# In rare cases , we might not define __init__
# self - refer to a specific instance from the class
    # Does not have to be called self, but it is the standard and pretty much the only thing you will see.
    # IT must be the first parameter to __init__ and any methods and properties on class instances
# instantiating a class
# Creating an object that is an instance of a class is called
# instantiating a class

# v = vehicle("honda","civic", 2017)

# _name
    # convention to tell developer that this is such a private attribute or method
    # supposed not accessible from outside the class by convention
# __name
    # name mangling behind the scene to _class-name__msg
    # make the attributes or methods more related to the class.
# __name__
#     # convention should be respected as python defined method
      # can be used to override something already defined by python internally
# class Person ():
#     def __init__(self):
#         self.name = "Tony"
#         self._secret = "hi"
#         self.__msg = "Hello from the other side!"

# p = Person()

# print(p.name)
# print(p._secret)

# print(p._Person__msg)

# Instance Attributes and Methods

# class Person():
      # class attributes if defined
      # for exmple keep track for all instances created from class , that might
      # represent chat users, population ....
      # refer to it using the class name not the instnace
      # class-name.variable-name

      # active_users = 0
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_nam
#         Person.active_users += 1  

#     def full_name(self):
#         return f"My name is {self.first_name} {self.last_name}"

#     def likes(self, thing):
#         return f"{self.first_name} likes {thing}"
    #   def logout(self):
    #       Person.active_users -= 1
# p = Person("Mohamed", "kandil")
# p.full_name()
# p.likes("Python")

# class Attributes
# defined once
# we can also define attributes directly on a class that are shared by
# all instances of a class and the class itself.


# class Pet:
# 	allowed = ['cat', 'dog', 'fish', 'rat']

# 	def __init__(self, name, species):
# 		if species not in Pet.allowed:
# 			raise ValueError(f"You can't have a {species} pet!")
# 		self.name = name
# 		self.species = species

# 	def set_species(self,species):
# 		if species not in Pet.allowed:
# 			raise ValueError(f"You can't have a {species} pet!")
# 		self.species = species

# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "dog")

# id(cat.allowed) # same
# id(dog.allowed) # same
# id(Pet.allowed) # same

# class methods
# are methods (with the @classmethod decorator)
# that are not concerned with instances, but the class itself

# class Person():

#     # .......
#     @class classname
#     def fun(cls):
#         pass

# A User class with both instance attributes and instance methods
# class User:
# 	active_users = 0

# 	@classmethod
# 	def display_active_users(cls):
# 		return f"There are currently {cls.active_users} active users"

# 	@classmethod
# 	def from_string(cls, data_str):
# 		first,last,age = data_str.split(",")
# 		return cls(first, last, int(age)) # create a new user instance

# 	def __init__(self, first, last, age):
# 		self.first = first
# 		self.last = last
# 		self.age = age
# 		User.active_users += 1

# 	def logout(self):
# 		User.active_users -= 1
# 		return f"{self.first} has logged out"

# 	def full_name(self):
# 		return f"{self.first} {self.last}"

# 	def initials(self):
# 		return f"{self.first[0]}.{self.last[0]}."

# 	def likes(self, thing):
# 		return f"{self.first} likes {thing}"

# 	def is_senior(self):
# 		return self.age >= 65

# 	def birthday(self):
# 		self.age += 1
# 		return f"Happy {self.age}th, {self.first}"



# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
# # print(User.display_active_users())
# # user1 = User("Joe", "Smith", 68)
# # user2 = User("Blanca", "Lopez", 41)
# # print(User.display_active_users())

# tom = User.from_string("Tom,Jones,89")
# print(tom.first)
# print(tom.full_name())
# print(tom.birthday())

# NEW CODE
	# def __repr__(self):
	# 	return f"{self.first} is {self.age}"
# NEW CODE

# String representation example
# __repr__  :- executed when print object
# method is one of several ways to provide a nicer string representation
# there are also several other dunders to return classes in string formatss
# (notably __str__ and __format__ ), and choosing one is a bit complicated

