#!/usr/bin/env python
# coding: utf-8

# 
# #### OOPS Assignment

# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.  
# Q2. Name the four pillars of OOPs.  
# Q3. Explain why the __init__() function is used. Give a suitable example.  
# Q4. Why self is used in OOPs?  
# Q5. What is inheritance? Give an example for each type of inheritance.  

# ###### Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.  
# 

# Q1. In object-oriented programming, a class is a blueprint for creating objects that defines a set of attributes (data) and methods (functions) that objects of that class will have. An object is an instance of a class, created using the class blueprint, that contains its own data and methods. For example, consider a class called Car that has attributes such as color, model, and make, and methods such as start(), stop(), and accelerate(). An object of this class would be a specific car with its own color, model, make, and ability to perform the methods defined in the Car class.

# ###### Q2. Name the four pillars of OOPs.  
# 

# The four pillars of OOPs are:
# 
# Encapsulation: the concept of binding data and methods together to protect them from external interference and misuse.  
# Abstraction: the ability to focus on essential features of an object while ignoring non-essential details.  
# Inheritance: the ability of a class to inherit attributes and methods from a parent class.  
# Polymorphism: the ability of an object to take on multiple forms or behave in different ways depending on the context.  

# ##### Q3. Explain why the __init__() function is used. Give a suitable example.  
# 

#  The init() function is used to initialize the attributes of an object when it is created. It is called automatically when an object is instantiated from a class, and allows us to set initial values for the object's attributes. For example, consider a class called Person with attributes name and age. The init() function would be used to set the initial values of these attributes for each object of the class, like so:

# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ###### Q4. Why self is used in OOPs?  
# 

# In OOPs, self is used as a reference to the current instance of a class. It is used within class methods to refer to the object that the method is being called on. By using self, we can access the attributes and methods of the object. For example, consider a class called Circle with a method called area() that calculates the area of the circle. The area() method needs to access the radius attribute of the Circle object, which is done using self:

# In[ ]:


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


# ##### Q5. What is inheritance? Give an example for each type of inheritance.  

#  Inheritance is the ability of a class to inherit attributes and methods from a parent class. There are four types of inheritance:
# 
# Single inheritance: when a class inherits from a single parent class.  
# Multiple inheritance: when a class inherits from multiple parent classes.  
# Multilevel inheritance: when a class inherits from a parent class, which in turn inherits from another parent class.  
# Hierarchical inheritance: when multiple classes inherit from a single parent class.  
# Example for each type of inheritance:  

# In[ ]:


class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

d = Dog()
d.eat()   # Output: Eating...
d.bark()  # Output: Barking...


# In[ ]:


class A:
    def foo(self):
        print("A")

class B:
    def foo(self):
        print("B")

class C(A, B):
    pass

c = C()
c.foo()   # Output: A


# In[ ]:


class A:
    def foo(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

c = C()
c.foo()   # Output: A


# In[ ]:


class Animal:
    def eat(self

