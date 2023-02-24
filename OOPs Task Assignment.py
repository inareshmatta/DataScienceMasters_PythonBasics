#!/usr/bin/env python
# coding: utf-8

# ### OOPs Task Assignment

# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.  
# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.  
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.  
# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.  
# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.  
# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.  

# ##### Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.

# In[1]:


#  example implementation of a Vehicle class with an __init__ method that sets the name_of_vehicle, 
# max_speed, and average_of_vehicle instance variables:

class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


# With this class definition, you can create instances of Vehicle with different names, maximum speeds, and averages, like so:
# 
# 

# In[2]:


car = Vehicle("Toyota Corolla", 180, 30)
bike = Vehicle("Honda CB Unicorn", 120, 60)

#In this example, car and bike are both instances of the Vehicle class, 
#with their own name_of_vehicle, max_speed, and average_of_vehicle instance variables.


# ##### Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.

# In[3]:


class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        super().__init__(name_of_vehicle, max_speed, average_of_vehicle)
    
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} persons."


# In this implementation, the Car class inherits from the Vehicle class, and its __init__ method calls the parent class's __init__ method using the super() function.
# 
# The seating_capacity method takes a capacity argument, which is the seating capacity of the car. The method returns a string that includes the name of the car and its seating capacity.
# 
# Here's an example of how you can create an instance of the Car class and call the seating_capacity method:

# In[4]:


my_car = Car("Toyota Corolla", 180, 30)
print(my_car.seating_capacity(5))
# Output: Toyota Corolla has a seating capacity of 5 persons.


# ##### Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

# Multiple inheritance is a feature in object-oriented programming languages, including Python, where a class can inherit from multiple parent classes. This allows the child class to inherit the attributes and methods of all its parent classes.

# In[5]:


class A:
    def method_A(self):
        print("This is method A")

class B:
    def method_B(self):
        print("This is method B")

class C(A, B):
    def method_C(self):
        print("This is method C")

obj = C()
obj.method_A() # This is method A
obj.method_B() # This is method B
obj.method_C() # This is method C


# In this example, we have three classes: A, B, and C. Classes A and B are the parent classes, and class C is the child class that inherits from both A and B.  
# 
# Class A has a method method_A, class B has a method method_B, and class C has a method method_C. The child class C inherits the methods of both A and B.  
# 
# We create an object obj of the C class and call its methods method_A, method_B, and method_C. Since C inherits from both A and B, we can call methods from both parent classes.  

# ##### Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this class.

# Getter methods are used to access the private attributes of a class. They are used to retrieve the values of private attributes without accessing them directly.
# 
# Setter methods are used to modify the private attributes of a class. They are used to set the values of private attributes without modifying them directly.

# In[6]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age should be greater than 0.")

person = Person("John", 30)
print(person.get_age()) # Output: 30
person.set_age(40)
print(person.get_age()) # Output: 40
person.set_age(-10) # Output: Age should be greater than 0.


# In this example, the Person class has a private attribute __age which can only be accessed and modified through its getter and setter methods. The __init__ method sets the name and __age instance variables.
# 
# The get_age method is a getter method that returns the value of the private attribute __age. The set_age method is a setter method that sets the value of the private attribute __age only if the new value is greater than 0.
# 
# We create an instance of the Person class and call its getter and setter methods to retrieve and modify the private attribute __age. When we set the age to a negative value, the setter method prints an error message.

# ##### 5.What is method overriding in python? Write a python code to demonstrate method overriding.

# Method overriding is a feature in object-oriented programming languages, including Python, where a child class can provide its own implementation of a method that is already defined in its parent class. This allows the child class to change the behavior of the method inherited from the parent class.

# In[7]:


class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Cat(Animal):
    def sound(self):
        print("Meow!")

class Dog(Animal):
    def sound(self):
        print("Woof!")

animal = Animal()
cat = Cat()
dog = Dog()

animal.sound() # This animal makes a sound.
cat.sound() # Meow!
dog.sound() # Woof!


# In[ ]:




