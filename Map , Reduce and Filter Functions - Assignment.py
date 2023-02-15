#!/usr/bin/env python
# coding: utf-8

# Q1. Create a python program to sort the given list of tuples based on integer value using a
# lambda function.   
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# In[2]:


my_list = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)


# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
# lambda and map functions.      
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In[4]:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_list = list(map(lambda x: x**2, my_list))

print(squared_list)


# Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
# lambda functions     
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[5]:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_tuple = tuple(map(lambda x: str(x), my_list))

print(my_tuple)


# Q4. Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.     

# In[7]:


from functools import reduce

my_list = range(1, 26)

product = reduce(lambda x, y: x * y, my_list)

print(product)


# Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
# filter function.      
# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]     

# In[8]:


my_list = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

filtered_list = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, my_list))

print(filtered_list)


# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.    
# ['python', 'php', 'aba', 'radar', 'level']    

# In[9]:


lst = ['python', 'php', 'aba', 'radar', 'level']

# Define a lambda function to check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]

# Use filter to create a new list of palindromes
palindromes = list(filter(is_palindrome, lst))

# Print the palindromes
print(palindromes)


# In[ ]:




