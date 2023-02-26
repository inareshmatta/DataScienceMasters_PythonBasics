#!/usr/bin/env python
# coding: utf-8

# #### Q1. You are writing code for a company. The requirement of the company is that you create a python
# function that will check whether the password entered by the user is correct or not. The function should
# take the password as input and return the string “Valid Password” if the entered password follows the
# below-given password guidelines else it should return “Invalid Password”.
# Note: 
#  
# 1. The Password should contain at least two uppercase letters and at least two lowercase letters.  
# 2. The Password should contain at least a number and three special characters.  
# 3. The length of the password should be 10 characters long. 

# In[10]:


def validate_password():
    password = input("Please enter a password: ")
    if len(password) <= 10:
        return "Invalid Password: Password should be exactly 10 characters long"
    
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0
    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isalnum() and char != " ":
            special_count += 1
    
    if uppercase_count < 2:
        return "Invalid Password: Password should contain at least two uppercase letters"
    elif lowercase_count < 2:
        return "Invalid Password: Password should contain at least two lowercase letters"
    elif digit_count < 1:
        return "Invalid Password: Password should contain at least one digit"
    elif special_count < 3:
        return "Invalid Password: Password should contain at least three special characters"
    
    return "Valid Password"

# call the function to check the password
print(validate_password())


# #### Q2. Solve the below-given questions using at least one of the following:
# 1. Lambda function
# 2. Filter function
# 3. Zap function
# 4. List Comprehension
# 
# 
# -Check if the string starts with a particular letterY  
# -Check if the string is numericY  
# -Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)-  
# -Find the squares of numbers from 1 to 10
# -Find the cube root of numbers from 1 to 10  
# -Check if a given number is even
# -Filter odd numbers from the given list
# [1,2,3,4,5,6,7,8,9,10
# -Sort a list of integers into positive and negative integers lists.  
# [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

# In[ ]:


string_list = ['apple', 'banana', 'cherry', 'date']
letter = 'a'

result = list(filter(lambda x: x.startswith(letter), string_list))
print(result)  # Output: ['apple']


# In[ ]:


string_list = ['apple', 'banana', 'cherry', 'date']
letter = 'a'

result = [x for x in string_list if x.startswith(letter)]
print(result)  # Output: ['apple']


# In[ ]:


string_list = ['123', '1.5', 'apple', '5', '6.2']

result = list(filter(lambda x: x.isnumeric(), string_list))
print(result)  # Output: ['123', '5']


# In[ ]:


string_list = ['123', '1.5', 'apple', '5', '6.2']

result = [x for x in string_list if x.isnumeric()]
print(result)  # Output: ['123', '5']


# In[ ]:


fruit_list = [("mango", 99), ("orange", 80), ("grapes", 1000)]

result = sorted(fruit_list, key=lambda x: x[1])
print(result)  # Output: [('orange', 80), ('mango', 99), ('grapes', 1000)]


# In[ ]:


fruit_list = [("mango", 99), ("orange", 80), ("grapes", 1000)]

result = sorted(fruit_list, key=lambda x: x[1])
print(result)  # Output: [('orange', 80), ('mango', 99), ('grapes', 1000)]


# In[ ]:


numbers = list(range(1, 11))

result = list(map(lambda x: x**2, numbers))
print(result)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[ ]:


numbers = list(range(1, 11))

result = [x**2 for x in numbers]
print(result)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[ ]:


import math

numbers = list(range(1, 11))

result = list(map(lambda x: math.pow(x, 1/3), numbers))
print(result)  # Output: [1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968, 1.8171205928321397, 1.912931182772389, 2.0, 2.080083823051904, 2.154434690031884]


# In[ ]:


import math

numbers = list(range(1, 11))

result = [math.pow(x, 1/3) for x in numbers]
print(result)  

