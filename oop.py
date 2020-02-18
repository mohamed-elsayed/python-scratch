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

# from random import shuffle
# class Card():

#     def __init__(self, value, suit):
#         self.value = value
#         self.suit = suit 

#     def __repr__(self):
#         return f"{self.value} of {self.suit}"

# class Deck():
#     def __init__(self):
#         suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#         values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#         self.cards = [Card(value, suit) for suit in suits for value in values]


#     def __repr__(self):
#         return f"Deck of {self.count()} cards"


#     def count (self):
#         return len(self.cards)

#     def _deal(self, num):
#         count = self.count()
#         actual = min([count, num])

#         if count == 0 : 
#             raise ValueError ("All Cards have been dealt")
#         cards = self.cards[-actual:]    
#         self.cards = self.cards[:-actual]
#         return cards
#         # print(f"Going to remove {actual} cards")

#     def deal_card(self):
#         return self._deal(1)[0]

#     def deal_hand(self, hand_size):
#         return self._deal(hand_size)

#     def shuffle(self):
#         if self.count() < 52:
#             raise ValueError ("Only full decks can be shuffled")
        
#         shuffle(self.cards)
#         return self

    
# # c= Card("A", "Hearts")
# # print(c)

# d= Deck()
# d.shuffle()

# card = d.deal_card()
# print(card)

# hand = d.deal_hand(5)
# print(hand)

# Inheritance and objectives
# Objectives
# Implement inheritance, including multiple.
# Understand Method Resolution Order
# Understand Polymorphism
# Add Special methods to class

# Inheritance:
# A key feature of OOP is the ability to define a class
# which inherits from another calss (a "base" or "parent" class)

# In python, inheritance works by passing the parent class as an
# argument to the defenition of a child class:

# class Animal(Object):
#     def make_sound(self, sound):
#         print(sound)
    
#     cool = True 
# class Cat (Animal):
#     pass

# gandalf = Cat()
# gandalf.make_sound("meow")
# gandalf.cool 

# print(isinstance(gandalf, Animal))

# class Human():
#     def __init__(self, first, last, age):
#         self.first = first 
#         self.last = last
#         if age >= 0 :
#             self._age =age
#         else:
#             self._age = 0

#     # def get_age(self):
#     #     return self._age

#     # def set_age(self, new_age):
#     #     if new_age >= 0 :
#     #         self._age = new_age
#     #     else:
#     #         self._age = 0

#     # act as getter like get_age
#     # It is a decorator that alter how this function works
#     # we set up a property called age
#     # can be called as attributes not a method
#     @property
#     def age(self):
#         return self._age

#     # act as setter
#     @age.setter
#     def age(self, value):
#         if value >= 0 :
#             self._age = value
#         else:
#             raise ValueError("age can not be negative")
# # 
#     @property
#     def full_name(self):
#         return f"{self.first} {self.last}"

#     @full_name.setter
#     def full_name(self, name):
#         self.first, self.last = name.split(" ")

# jane = Human("mohamed", " kandil", 9)
# # jane.set_age(13)
# # print(jane.get_age())

# print(jane.age)
# # age act as a proxy to internal _age attribute

# print(jane.__dict__)
# the previous point act syntax sugar

# Introduction to Super()

# class Animal(object):
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self, sound):
#         print(f"This animal says {sound}")

#     def __repr__(self):
#         return f"{self.name} is a {self.species}"

# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         #self.name = name # duplication
#         #self.species = species # duplication
#         # Animal.__init__(self, name, species)
#         super().__init__(name, species="cat")
#         self.breed = breed
#         self.toy = toy
    
#     def play(self):
#         print(f"{self.name} plays with {self.toy}")

    

# blue = Cat("Blue", "Scottish Fold", "String")
# print(blue.__dict__)
# blue.play()

class Aquatic:
  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"

class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
  def __init__(self,name):
    print("PENGUIN INIT!")
    super().__init__(name=name)
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")















# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ?


# Method Resolution Order (MRO)
# Whenever you create a class, python sets a Method Resolution Order, or
# MRO, for that class, which is the order in which python will look for
# methods on instances of that class

# you can programmatically reference the MRO three ways:
# __mro__ attribute on the class
# use the mro() method on the class
# use the builtin help(cls) method

# print(Penguin.__mro__)
# Penguin.mro()

# help(Penguin)

# class A(object):
#     def do_something(self):
#         print("Method defined in: A")
# class B(A):
#     def do_something(self):
#         print("Method defined in: B")

# class C(A):
#     def do_something(self):
#         print("Method defined in: C")

# class D(B,C):
#     def do_something(self):
#         print("Method defined in: D")

# print(D.__mro__)

# Polymorphism
# A key principle in OOP is the idea of Polymorphism
# an object can take on many(poly) forms (morph)

# While a formal definition of polymorphism is more difficult,
# here are two important practical applications:
# 1- The same class method works in a similar way for different classes
    # cat.speak()
    # Dog.speak()
    # Human.speak()
# 2- The same operation works for different kinds of objects
    # sample_list = [1,2,3]
    # sample_tuple = (1,2,3)
    # sample_string = "awesome"

    # len(sample_list)
    # len(sample_tuple)
    # len(sample_string)

# Polymorphism and inheritance
# 1- The same class method works in a similar way for different classes
# A common implementation of this is to have a method in a base (or parent)
# class that is overridden by a subclass. This is called method overriding
# Each subclass will have a different implementation of the method
# If the method is not implemented in the subclass, the version in the
# paranet class is called instead.

# class Animal (object):
#     def speak(self):
#         raise NotImplementedError ("subclass needs to implement this method")

# class Dog(Animal):
#     def speak(self):
#         return "woof"

# class Cat(Animal):
#     def speak(self):
#         return "meow"

# class Fish(Animal):
#     pass

# d = Dog()
# print(d.speak())
# f= Fish()
# print(f.speak())

# Special Methods
# 2- (polymorphism) the same operation works for different kinds of objects
# How does the following work in python ?
# 8 + 2 # 10
# "8" + "2" # 82 
# The answer is "special methods"

# Python classes have special (also known as "magic") methods
# that are dunders (double underscore-named)

# These are methods with special names that give instructions to python for how 
# to deal with objects.


# The + operator is shorthand for a special method called 
# __add__() that gets called on the first operand

# If the first (left) operand is an instance of int, __add__() does mathematical
# addition . IF it is string , it does string concatenation.

# Special method applied
# Therefore, you can declare special methods on your own classes to mimic
# the behaviour of builtin objects, like so __len__:

# class Human(object):
#     def __init__(self, height, name):
#         self.height = height
#         self.name = name
    
#     def __len__(self):
#         return self.height

#     def __repr__(self):
#         return self.name

# colt = Human(60, "mohamed")
# print(len(colt))

# # The most common use case for special methods is to make classes
# # "look pretty" in strings

# print(colt) # <__main__.Human at 0x12321b5456>

# # String Representation Example
# # The __repr__ method is one of several ways to provide a 
# # nicer string representation


# from copy import copy
# class Human:
# 	def __init__(self, first, last, age):
# 		self.first = first
# 		self.last = last
# 		self.age = age
		
# 	def __repr__(self):
# 		return f"Human named {self.first} {self.last} aged {self.age}"

# 	def __len__(self):
# 		return self.age

# 	def __add__(self, other):
# 		# When you add two humans together...you get a newborn baby Human!
# 		if isinstance(other, Human):
# 			return Human(first='Newborn', last=self.last, age=0)
# 		return "You can't add that!"

# 	def __mul__(self, other):
# 		# When you multiply a Human by an int, you get clones of that Human!
# 		if isinstance(other, int):
# 			return [copy(self) for i in range(other)]
# 		return "CANT MULTIPLY!"
	


# j = Human("Jenny", "Larsen", 47)
# k = Human("Kevin", "Jones", 49)
# # print(j)
# # print(len(j))
# # triplets = j * 3

# # kevin and jessica have triplets!
# triplets = (k + j) * 3
# print(triplets)

class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value)

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return False

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data

class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"THAT THING YOU WANT ISN'T IN HERE")

	def __setitem__(self, key, value):
		print("Why do you always have to change things?")
		print(f"Ugh fine, setting {key} to {value}")
		super().__setitem__(key, value)