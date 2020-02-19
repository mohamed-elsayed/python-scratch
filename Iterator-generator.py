# =================================================
################ Iterator/generator     ###########
# =================================================

# Objectives
# Define Iterator and Iterable
# Understand the iter() and next() methods
# Build our own for loop
# Define what generators are and how they can be used
# Compare generator functions and generator expressions
# Use generators to pause execution of expensive functions

# Iterators ? Iterables ?

# Iterator -  an object that can be iterated upon .
# An object which returns data, one element at a time when next() is called on it

# Iterable - An object which will return an iterator when iter() is called on it

# "Hello" is an iterable , but it is not an iterator.
# iter("Hello") returns an iterator.

name = "Operah"
# next(name) # TypeError: 'str' object is not iterator.
iter(name) # return an Iterator
it = iter(name)
# for char in "Operah"
# for loop behind the scene call iter() on the string "Operah"  that return an iterator then for loop go through each item in the iterator using the next()

# when next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error

# these are standard protocol applied to any iterator from iteable.

# num = [1,2,3]
# next(num) # give TyperError as list object is not an iterator
# To make It Iterator, call iter(num) and then call next() over the Iterator

# custom for loop

# def my_for (iterable, func):
#     iterator = iter(iterable)
#     while True :
#         try:
#             thing = next(iterator)
#         except StopIteration:
#             break
#         else:
#             func(thing)

# def square(x):
#     print(x*x)       

# my_for("hello", print)
# my_for([1,2,3,4], square)

# Define our own Iterable and Iterator

# class Counter(object):
#     def __init__(self, low, high):
#         self.current = low
#         self.high = high 

#     def __iter__(self):
#         return self 
 
#     def __next__(self):
#         if self.current < self.high:
#             num = self.current
#             self.current += 2
#             return num
#         raise StopIteration


# for x in Counter(0, 20):
#     print(x)


from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)

    # VERSION USING A GENERATOR FUNCTION 
    # (covered in the next video)
    # def __iter__(self):
    #     for card in self.cards:
    #         yield card

    def reset(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        """
        Return a list of cards dealt
        """
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal

        if count == 0:
            raise ValueError("All cards have been dealt")

        if actual == 1:
            return [self.cards.pop()]

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)

# my_deck = Deck()
# my_deck.shuffle()

# for card in my_deck:
#     print(card)


# Generators
# Generators are iterators
# Generators can be created with generator functions
# Generator functions are thr yield keyword
# Generators can be created with generator expressions

# Functions vs Generator Functions
# use return        use yield
# return once       can yield multiple times
# when invoked,     when invoked
# returns the       returns a generator object
# return value

# our first generator
def count_up_to(max):
    count =1 
    while count <= max:
        yield count
        count += 1

# count_up_to(5) # return a generator object
# counter = count_up_to(5)
# print(next(counter)) # we get one thing at a time., not go back 
# for c in counter: # automatically catch StopIteration Error and break loop
    # print(c)
# print(list(counter))
# generator is returned from a generator function
# It is a way for making an iterator quickly
# Never have to determine what happen when calling next
# We do not define next() or iter()
# We never are raising the StopIteration Error
# We just define a function call it whatever you want  and yield
# wherever that yield is, it is going to stop immediately, return the value that we specify 
# stop execution and just wait.

# counter= count_up_to(10)
# print(list(counter))

# Infinite generator
# let us say we are making a music application, 

# def current_beat():
    # function return 1, 2, 3, 4 or any pattern
    # How could we have it return a single number. but every time return a different number then repeating. we can return one thing from a function ?
#     max = 100
#     nums = (1,2,3,4)
#     i =0 
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i =0
#         result.append(nums[i])
#         i+=1
#     return result

# print(current_beat())


def current_beat():
    nums = (1,2,3,4)
    i=0
    while True:
        if i >= len(nums): i =0 
        yield nums[i]
        i+=1

# for c in current_beat():
#     print(c)

# Testing memory usage with generators
def fib_gen(max):
    x=0
    y=1
    count =0 
    while count < max:
        x,y = y,x+y
        yield x
        count +=1


def fib_list(max):
    nums = []
    a,b = 0,1
    while len(nums) < max:
        nums.append(b)
        a,b = b,a+b
    return nums

# print(fib_list(10))

# Cautious following command will hang your PC. Memory eater
# for n in fib_list(1000000):
#     print(n)

# for n in fib_gen(1000000): # less memory footprint
#     print(n)

# generator Expressions
# look like list comprehesion
# use () instead of []

# def nums():
#     for num in range(1,10):
#         yield num

# g= (num for num in range(1,10))
# l= [num for num in range(1,10)]

# sum([num for num in range (1,10)])
# sum(num for num in range(1,10))

# import time

# gen_start_time = time.time()
# print(sum(n for n in  range(100000000)))
# gen_stop = time.time() - gen_start_time
# print (gen_stop)

# list_start_time = time.time()
# print(sum([n for n in  range(100000000)]))
# list_stop = time.time() - list_start_time
# print(list_stop)

