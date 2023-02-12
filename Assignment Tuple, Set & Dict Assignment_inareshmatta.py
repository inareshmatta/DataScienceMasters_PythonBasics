#!/usr/bin/env python
# coding: utf-8

# *** Q1. The characteristics of tuples in Python are:*** 
# 
# They are immutable, meaning the elements within a tuple cannot be changed.
# They use parentheses instead of square brackets like lists.
# They are ordered, meaning the elements within a tuple have a defined order.
# They can contain elements of different data types, including other tuples.

# *** Q2. The two tuple methods in Python are:***
# 
# count(): This method returns the number of occurrences of a specified element in a tuple.
# Example: t = (1, 2, 3, 1, 2, 3)
# t.count(1) # Output: 2
# 
# index(): This method returns the index of the first occurrence of a specified element in a tuple.
# Example: t = (1, 2, 3, 1, 2, 3)
# t.index(1) # Output: 0
# 
# Tuples have only two in-built methods as compared to Lists because tuples are immutable, meaning their elements cannot be modified, so they do not require as many methods as Lists.

# *** Q3. Sets are the collection datatype in Python that do not allow duplicate items.***
# Example code to remove duplicates from a list using a set:

# In[1]:


List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
set_list = set(List)
print(list(set_list)) 
# Output: [1, 2, 3, 4]


# *** Q4. The union() method returns a set that contains all the elements from two sets, but it does not modify the original sets.***
# The update() method adds all the elements from one set to another, and it modifies the original set.
# 
# Example:

# In[2]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union example
print(set1.union(set2))   # Output: {1, 2, 3, 4, 5}

# Update example
set1.update(set2)
print(set1)   # Output: {1, 2, 3, 4, 5}


# *** Q5. A dictionary in Python is an unordered collection of key-value pairs, where each key is unique.***
# Example:
# Dictionaries are unordered, meaning the elements within a dictionary do not have a defined order.

# In[3]:


dict1 = {'language': 'Python', 'version': '3.9.2'}


# *** Q6. Yes, we can create a nested dictionary in Python.***
# Example:

# In[4]:


nested_dict = {'A': {'a1': 10, 'a2': 20}, 'B': {'b1': 30, 'b2': 40}}


# *** Q7. Using the setdefault() method to create a key named topics in the given dictionary and add the value of the key as a list:***

# In[5]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topics', ['Python', 'Machine Learning', 'Deep Learning'])
print(dict1) 
# Output: {'language': 'Python', 'course': 'Data Science Masters


# *** A8. The three view objects in dictionaries are: keys(), values() and items().***
# 
# To display these three view objects, we can use the following code:

# In[6]:


dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# keys() method
print("keys(): ", dict1.keys())

# values() method
print("values(): ", dict1.values())

# items() method
print("items(): ", dict1.items())


# In[ ]:




