## 2024-02-20 methods associated with list
# sort; pop; index; [:], enumerate, reversed
L = ['b', 'a','c']
L.sort() # will change L in place; nothing as explicit return; L is now ['a', 'b', 'c'];
L.pop() # will change L in place; the last element as return; L is now ['a', 'b']; should assign the return to a variable;
L.index('a') # will not change L, but return the index of the element in the bracket;

# neither enumerate() or reversed() would change the L itself; they return new objects
L = ['b', 'a','c']
enumerate(L) # return an enumerate object, which could be turn into a list; 
list(enumerate(L)) # each element is a tuple (index, element of L)

L = ['b', 'a','c']
reversed(L) # return reversed version of the list; but it is a iterator; could use next() to access each element;
next(reversed(L)) # return 'c'
# or turn it a list
list(reversed(L))


## 2024-02-21 function arguments 
# * and ** in front of the function arguments
# * When you prefix a parameter with *, Python collects any additional positional arguments into a tuple. 
def my_function(*args):
    for arg in args:
        print(arg)
my_function('apple', 'banana', 'cherry')

# **  The double asterisks before the parameter name indicate that 
# any additional keyword arguments will be collected into a dictionary 
# where the keys are the argument names and the values are the argument values. 
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
my_function(fruit='apple', color='red', size='medium')


## 2024-02-22 Regular Expressions
# '^' at the begining of [] means not; otherwise it means itself;
[^0-9] # not any digit
[a-z^] # any letter and ^
# \w means [a-zA-Z0-9_]; \W means not any of [a-zA-Z0-9_]
# '.' matches content itself; '*', '+', '?' matches times
# res = re.search('pattern', 'string')
# res.groups() # when use brackets in the pattern to indicate groups; this return all found groups in a tuple;
# res.group() # when use brackets in the pattern to indicate groups; this return all found groups in a string;
# res.group(1) # the first element in res.groups(); and so on
import re
l1 = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]
for i in l1:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+), (.*)", i)
    if res:
        print(res.group(3) + ' ' + res.group(2) + ' ' + res.group(1))
      
l2 = ["<composer> Wolfgang Amadeus Mozart </composer>",
      "<author> Samuel Beckett </author>",
      "<city> London </city>"]
for i in l2:
     res = re.search(r"<([a-z]+)>(.*)</\1>",i) # note that \1 to refer to the group
     print(res.group(1) + ": " + res.group(2))

## 2024-02-23 python class (Object Oriented Programming)
# __init__() is a method which is immediately and automatically called after an instance has been created
class A:
    def __init__(self):
        print("__init__ has been executed!")
x = A() # '__init__ has been executed!' will automatically printed

# Private attributes use '__' in front of the variable name
# Protected (restricted) Attributes use '_' in front of the varialbe name
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
