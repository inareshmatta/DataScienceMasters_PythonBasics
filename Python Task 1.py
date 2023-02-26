#!/usr/bin/env python
# coding: utf-8

# Q1. Create a function which will take a list as an argument and return the product of all the numbers
# after creating a flat list.
# 
# Use the below-given list as an argument for your function.
# list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
# 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
# 
# Note: you must extract numeric keys and values of the dictionary also.

# In[1]:


def product_of_numbers(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, (int, float)):
            flat_list.append(item)
        elif isinstance(item, (list, tuple)):
            for nested_item in item:
                if isinstance(nested_item, (int, float)):
                    flat_list.append(nested_item)
                elif isinstance(nested_item, (list, tuple)):
                    for deeper_item in nested_item:
                        if isinstance(deeper_item, (int, float)):
                            flat_list.append(deeper_item)
                elif isinstance(nested_item, dict):
                    for key, value in nested_item.items():
                        if isinstance(key, (int, float)):
                            flat_list.append(key)
                        if isinstance(value, (int, float)):
                            flat_list.append(value)
        elif isinstance(item, set):
            if item:
                for nested_item in item:
                    if isinstance(nested_item, (int, float)):
                        flat_list.append(nested_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, (int, float)):
                    flat_list.append(key)
                if isinstance(value, (int, float)):
                    flat_list.append(value)
    product = 1
    for num in flat_list:
        product *= num
    return product


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
result = product_of_numbers(list1)
print(result)


# The issue with the input list is that it contains a boolean value False and a string value 'Machine Learning' which are not numeric values. When the function encounters these non-numeric values, it appends them to the flat_list but then tries to multiply them with the product variable which is initially set to 1. Since these values cannot be multiplied with an integer, the final result becomes 0.  
# 
# To fix this issue, you should modify the function to skip over non-numeric values and only multiply the numeric values together. You can use the isinstance() function to check whether a value is numeric or not. 

# #### Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption should be such that, for a the output should be z. For b, the output should be y. For c, the output shouldbe x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation marks unchanged.
# 
# Input Sentence: I want to become a Data Scientist.  
# Encrypt the above input sentence using the program you just created.  
# Note: Convert the given input sentence into lowercase before encrypting. The final output should be
# lowercase.  

# In[ ]:


def encrypt_message(message):
    encrypted = ""
    for char in message.lower():
        if char.isalpha():
            encrypted += chr(ord('a') + ord('z') - ord(char))
        elif char == ' ':
            encrypted += '$'
        else:
            encrypted += char
    return encrypted

input_sentence = input("Enter a sentence to encrypt: ")
encrypted_sentence = encrypt_message(input_sentence)
print("Encrypted Sentence:", encrypted_sentence)


# In[ ]:


def decrypt_message(message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            decrypted_message += chr(219 - ord(char))
        else:
            decrypted_message += char
    decrypted_message = decrypted_message.replace("$", " ")
    return decrypted_message.lower()

encrypted_message = input ("Enter the encrypted message: ")
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted message:", decrypted_message)


# In[ ]:





# In[ ]:





# In[ ]:




