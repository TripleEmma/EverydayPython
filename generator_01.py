# 1. iterable VS. iterator:  A list is iterable, but it is not an iterator. 
#    1.1 When we apply for loop on a list, we call iter() on the list, and make it into an iterator. 
#    1.2 When an object is iterator, we can apply next() on it.

# 2. A generator automatically have methods \__iter__() and next(). Keyword **yield** turns functions into generators.

# 3. A generator starts like a normal function until it reaches the line **yield**. 
# It return the expression after **yield** and keep all other variable before the command line. 
# Then it wait until the next() called and will continue from **yield** and run until **yield** again and wait for another next().

# example 1 to illustrate point 3
def test(y):
    print('first y:', y, end='; ')
    x = 'Jena'
    yield x
    y += 1
    print('second y:', y, end='; ')
    x = 'Weimar'
    yield x
    y += 1
    print('third y:', y, end='; ')
    x = 'Erfurt'
    yield x
T = test(0) 
print(next(T)) # first y: 0; Jena
print(next(T)) # second y: 1; Weimar
print(next(T)) # third y: 2; Erfurt

# example 2 to illustrate point 3
def count(firstval=0, step=1):
    x = firstval
    while True:
        yield x
        x += step        
counter = count() # count will start with 0
for i in range(10):
    print(next(counter), end=", ")
print('Emma')
for i in range(10):
    print(next(counter), end=", ") # it starts from where it is left last time
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, Emma
# 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 

# 4. *send* method (though I don't understand why this is useful except it is fun)
def count(firstVal, step):
  counter = firstVal
  while True:
    newCounter = yield counter
    if newCounter == None:
      counter += step
    else:
      counter = newCounter
      
counter =  count(1, 0.2)
for i in range(10):
  print(next(counter), end = ', ')
print()

print('Now set a new start:')
counter.send(100)

for i in range(10):
  print(next(counter), end = ', ')
