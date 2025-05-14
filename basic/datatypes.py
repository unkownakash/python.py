# 1. Numeric Data Types in Python
## Step 1: Introduction to Numeric Data Types
# Python has several built-in numeric data types that can be used to represent numbers. These include integers, floating point numbers, and complex numbers.
a = 5
print(type(a)) # Integers 

b = 5.0
print(type(b)) # float

c = 2 + 4j
print(type(c)) # Complex

# 2.Sequence Data Types in Python
#The sequence Data Type in Python is the ordered collection of similar or different Python data types. Sequences allow storing of multiple values in an organized and efficient fashion
##String Data Type
s= " I am a Web devloper "
print(s) # String
##List Data Types
# It Just like a  array 
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b) 
#Tuple Data Type
# It is similar to list but it is immutable, Tuples cannot be modified after it is created.
tup1=("heelo", "my", 2,5)
print(tup1)
# tuples have -ve index value also  NOTES THIS 
tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[3])

#Set Data Type in Python
# in this  data type we create a set that is like a unorder listed item which is mutable with no duplicate items 
# initializing empty set
s1 = set()

s1 = set("ILovePython")
print("Set with the use of String: ", s1)

s2 = set(["Tiya", "Love", "Tiya"])
print("Set with the use of List: ", s2)
"""
output
Set with the use of String:  {'s', 'o', 'F', 'G', 'e', 'k', 'r'}
Set with the use of List:  {'Geeks', 'For'}
"""
# Dictionary Data Type
# it like  a  object 
# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)
