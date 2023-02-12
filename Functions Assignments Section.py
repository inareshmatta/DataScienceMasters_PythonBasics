#!/usr/bin/env python
# coding: utf-8

# ## ***Functions Assignments Section*** 

# *** Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.***
# 
# def keyword is used to create a function
# 
# functions to return list of odd number is : 

# In[1]:


def odd_numbers():
    start = int(input("Enter the start of range:"))
    end = int(input("Enter the end of range:"))
 
# iterating each number in list
       
    for num in range(start, end):
 
    # checking condition
            if num % 2 != 0:
                print(num)


# *** Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to
# demonstrate their use.*** 
# 
# Creating functions that accept *args and **kwargs are best used in situations where you expect that the number of inputs within the argument list will remain relatively small. The use of *args and **kwargs is primarily to provide readability and convenience
# 

# In[2]:


def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)


# In[3]:


def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)

intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)


# *** Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,
# 18, 20].***
# 
# An iterator in Python is an object that can be iterated (looped) upon. They represent a stream of data, and you can traverse through elements one by one. In Python, an iterator object implements two methods, __iter__() and __next__().
# 
# The __iter__() method is used to initialize the iterator object and it returns the iterator object itself. The __next__() method is used for iteration. It returns the next value from the iterator. If there are no more items to return, it should raise StopIteration.
# 
# 
# 
# 

# In[4]:


class MyList:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        value = self.lst[self.index]
        self.index += 1
        return value

my_list = MyList([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
iterator = iter(my_list)

for i in range(5):
    print(next(iterator))


# *** Q4 What is a generator function in python? Why yield keyword is used? Give an example of a generator
# function.***
# 
# A generator function is a special type of function in Python that can be used to create an iterator. It uses the yield keyword instead of return. When a generator function is called, it returns a generator object that can be iterated over, but unlike a normal function, it does not return a value, instead it generates a series of values, one at a time, on-the-fly.
# 
# The yield keyword is used to produce a value and then pause the function's execution, retaining its state. When the function is next called, the execution resumes from where it left off, and continues until the next yield statement. The function can be called multiple times, and each time it will start producing the values from where it left off. This makes generator functions very efficient for producing a large number of values, as they only generate the values as they are requested, rather than generating all of the values upfront and returning them as a list.

# In[5]:


def fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci_sequence(10):
    print(number)


# ***Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.***

# In[6]:


def prime_numbers():
    yield 2
    primes = [2]
    number = 3
    while number < 1000:
        is_prime = True
        for prime in primes:
            if prime > number ** 0.5:
                break
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
            yield number
        number += 2

generator = prime_numbers()

for i in range(20):
    print(next(generator))


# In[ ]:




