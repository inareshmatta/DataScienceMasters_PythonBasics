#!/usr/bin/env python
# coding: utf-8

# # Data Science Master's Class - iSkillMatta Notes

# ## Day 1 
# 
# ### Python Objects, Number & Booleans, Strings.

# ##### Mathematical Operations + - / *

# In[1]:


1+2


# In[2]:


1*2


# In[3]:


1/2


# In[4]:


1-2


# FYI : writing 1+2 and writing print(1+2) is different as the cell is not created, rather the output console takes over the place of a new cell value, for example on top you can see the first in(2) it means it is count of the cell value and in this case the out is assigned the value of input cell. This is only for Collab, Notebooks etc 
# 

# In[5]:


print(1+2)


# # Strings : 
# 
# ### How to read inbuilt functions in Python : 
# Write function for example print ( press shift tab)
# 
# This is result : 
# 
# 
# Docstring:
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# 
# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file:  a file-like object (stream); defaults to the current sys.stdout.
# sep:   string inserted between values, default a space.
# end:   string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.
# Type:      builtin_function_or_method
# 
# #### We can also write our own Function which we will understand later

# #### Things to know about strings in Python
# 
# Escaping characters: If you need to include a quote character within a string, you can escape it by preceding it with a backslash (\). For example:
# 
# ##### message = "He said, \"Hello, how are you?\""
# 
# 
# Raw strings: If you need to include a backslash in a string and don't want it to be interpreted as an escape character, you can create a raw string by preceding the string with the letter r. Raw strings are useful when working with regular expressions and file paths:
# 
# ##### path = r"C:\Users\John\Documents"
# 
# 
# Multiline strings: If you need to create a string that spans multiple lines, you can use triple quotes (either single quotes or double quotes) to create a multiline string. For example:
# 
# ##### message = """This is a
# multiline
# string""" 
# 
# 
# Unicode strings: In Python 3, strings are Unicode by default, meaning that they can represent any character in the Unicode character set. This makes it easy to work with text in multiple languages. If you need to create a string that contains characters that are not part of the ASCII character set, you can use Unicode escape sequences to specify those characters. For example:
# 
# ###### message = "こんにちは"
# 
# 
# Formatting strings: You can use the format method to insert values into a string. The format method allows you to specify placeholders within the string, which are then replaced with values from the argument list. For example:
# 
# #####
# name = "John"
# age = 30
# message = "My name is {} and I am {} years old".format(name, age)
# 
# 
# String indexing and slicing: Strings can be indexed and sliced just like lists. The index of the first character in a string is 0, and you can use negative index values to access characters from the end of the string. For example:
# 
# name = "John Doe"
# print(name[0]) # Output: J
# print(name[-1]) # Output: e
# print(name[1:4]) # Output: ohn
# 

# In[6]:


"This is a string"


# In[7]:


print("This is a new line \n string")


# In[8]:


# Using %-formatting
name = "John"
age = 30
message = "My name is %s and I am %d years old" % (name, age)
print(message)

# Output: My name is John and I am 30 years old

# Using the format() method
name = "John"
age = 30
message = "My name is {} and I am {} years old".format(name, age)
print(message)

# Output: My name is John and I am 30 years old

# Using f-strings
name = "John"
age = 30
message = f"My name is {name} and I am {age} years old"
print(message)

# Output: My name is John and I am 30 years old


# ### Variables 
# 
# In Python, a variable is a name that refers to a value stored in memory. Variables are used to store values that can change during the execution of a program. A variable can be assigned a value using the assignment operator =. 
# 
# In Python, variables are dynamically typed, meaning that the type of a variable can change during the execution of the program. 
# 
# Variable naming conventions: In Python, variables can only contain letters, numbers, and underscores. They cannot start with a number and should not be one of the Python keywords. It's a common practice to use all lowercase letters with words separated by underscores for variable names.
# 
# Scope of variables: Variables can have different scopes depending on where they are defined. For example, variables defined inside a function are local to that function and are not accessible outside of it. On the other hand, variables defined outside of any function are global and can be accessed from anywhere in the program.
# 
# Mutability: In Python, some data types are mutable, meaning that their values can be changed, while others are immutable, meaning that their values cannot be changed once they are created. For example, lists and dictionaries are mutable, while strings and tuples are immutable.
# 
# Global and nonlocal keywords: The global keyword can be used to specify that a variable is a global variable, even if it's being assigned inside a function. The nonlocal keyword can be used to specify that a variable is non-local to the current function, meaning that it's defined in the nearest enclosing function that's not a global function.
# 
# Garbage collection: In Python, memory management is handled automatically, and objects that are no longer referenced by any variable are automatically cleaned up by the garbage collector. This means that you don't have to worry about freeing up memory yourself.

# In[9]:


a=10
a


# Here we are storing value 10 to a letter 'a' and when we store the value and call the variable name the result will be off the stored value

# In[10]:


name = "Matta"
name


# In[11]:


a="Matta"
b="MATTA"


# ### String is case senstive

# In[12]:


a


# In[13]:


b


# ### Dynamic Typing
# 
# Dynamic typing is a type system used in some programming languages where the data type of a value is determined at runtime. In contrast, in statically-typed languages, the data type of a variable is determined at compile-time and must remain the same throughout the execution of the program.
# 
# In dynamic typing, variables don't have to be explicitly declared with a specific data type, and the type of the value stored in a variable can change dynamically during runtime. This can allow for more flexible and versatile code, as well as faster development time. However, it can also make it harder to catch type errors and can result in unexpected behavior if the type of a variable changes in unexpected ways.
# 
# Examples of programming languages that support dynamic typing include Python, Ruby, JavaScript, and PHP.
# 
# ##### Python : 
# 
# x = 10
# print(type(x)) # Output: <class 'int'>
# 
# x = "hello"
# print(type(x)) # Output: <class 'str'>
# 
# 
# ##### Java : 
# int x = 10;
# System.out.println(x.getClass().getName()); // Output: int
# 
# // The following line would cause a compile error because the type of x cannot be changed
# x = "hello"; 
# 
# In the Python example, the type of the variable x can change dynamically, first being an int, and then being a str. In Java, once a variable has been declared with a specific data type, it cannot be changed.
# 
# This difference in type handling illustrates the contrast between dynamic and static typing in programming languages. While dynamic typing can provide more flexibility, static typing can provide more stability and catch type-related errors early on in the development process.
# 
# 
# 
# 
# 
# 

# In[14]:


x = 10 
print(type(x)) # Output: <class 'int'>

x = "hello" 
print(type(x)) # Output: <class 'str'>


# ### Reserved Keywords
# 
# Reserved keywords are special words in a programming language that have a specific meaning and cannot be used as identifiers (variable names, function names, etc.) in the code. They are reserved by the language and are used to perform specific tasks or operations. Some common reserved keywords in Python are:
# 
# 1. and
# 2. as
# 3. assert
# 4. break
# 5. class
# 6. continue
# 7. def
# 8. del
# 9. elif
# 10. else
# 11. except
# 12. False
# 13. finally
# 14. for
# 15. from
# 16. global
# 17. if
# 18. import
# 19. in
# 20. is
# 21. lambda
# 22. None
# 23. nonlocal
# 24. not
# 25. or
# 26. pass
# 27. raise
# 28. return
# 29. True
# 30. try
# 31. while
# 32. with
# 33. yield
# 

# ## Concatination 
# 
# Concatenation is the process of combining two or more values into a single value in programming. In Python, you can concatenate strings and numbers using the + operator.
# 
# Here are some examples of concatenation in Python:
# 
# 
# In Python, you can only concatenate values of the same type. If you try to concatenate a string and a number, you'll need to first convert the number to a string using the str function:
# 
# ###### example : 
# 
# a = "The answer is "
# b = 42
# c = a + str(b)
# print(c) # Output: The answer is 42
# 
# 
# Concatenation is a common operation in programming, and can be used to build complex values from smaller parts.

# In[15]:


name = "John"
last_name = "Doe"
full_name = name + " " + last_name
print(full_name) # Output: John Doe


# In[16]:


a = 5
b = 10
c = a + b
print(c) # Output: 15


# In[17]:


a = "The answer is "
b = 42
c = a + str(b)
print(c) # Output: The answer is 42


# ### Type Casting
# 
# Type casting, also known as type conversion, is the process of converting a value from one data type to another data type in programming. This can be useful in cases where you need to make sure that a value is of a certain data type in order to use it in a specific context.
# 
# For example, in real life you might use type casting when you want to calculate the average temperature for a certain period of time. Let's say that you have the daily temperatures stored as strings in a list:
# 
# 

# In[18]:


temperatures = ["32", "30", "28", "31", "29"]


# In order to calculate the average temperature, you would need to convert these strings to numbers. In Python, you can use the int function to convert a string to an integer:

# In[19]:


sum = 0
for temperature in temperatures:
    sum += int(temperature)
average = sum / len(temperatures)
print(average) # Output: 30.0


# In this example, we used type casting to convert the strings in the temperatures list to integers using the int function. This allowed us to sum up the temperatures and calculate the average temperature.
# 
# Type casting is a common operation in programming and can be used in a variety of situations to ensure that values are of the correct data type for a given context.

# You can permanently change the data type of elements in a list by iterating over the elements of the list and converting each element to the desired data type.
# 
# For example, consider the following list of temperatures stored as strings:

# In[20]:


temperatures = ["32", "30", "28", "31", "29"]
# This line initializes a list called temperatures with 5 strings representing daily temperatures.


# To permanently change the data type of the elements in the list, you could use a for loop to convert each element from a string to an integer:
# 
# 

# In[21]:


for i in range(len(temperatures)): 
    temperatures[i] = int(temperatures[i])
print(temperatures) # Output: [32, 30, 28, 31, 29]

# #This line starts a for loop that will run len(temperatures) times, 
# # where len(temperatures) is the length of the temperatures list. 
# # The variable i is used as the index of the temperatures list, 
# # and it will take on the values 0, 1, 2, 3, and 4 in each iteration of the loop.
# Next converts the element at the index i of the temperatures list from a string to an integer using the int function.
# The result is then stored back in the same location in the list, effectively replacing the original string with an integer.


# In this example, the for loop iterates over the indices of the temperatures list, and for each index, it converts the corresponding element from a string to an integer using the int function. The result is a list of integers, where the data type of the elements has been permanently changed.
# 
# This approach can be used to change the data type of elements in a list to any desired data type, as long as there is a corresponding conversion function available in Python.
# 
# 

# # Day : 2
# ### Conditions, if, else, ifelif, While, For Loops, AND , Llop Controls
# 
# Conditions, if, else, elif, while, for loops, and and loop controls are fundamental concepts in programming that allow you to control the flow of execution in your code.
# 
# Conditions:
# Conditions are used to evaluate whether a statement is true or false. If a condition is true, a certain block of code is executed; if it's false, the code is skipped. Conditions are often used in if statements to make decisions based on the state of your program.
# 
# if:
# The if statement allows you to execute a block of code only if a certain condition is met. If the condition is true, the code within the if block is executed. If the condition is false, the code is skipped.
# 
# else:
# The else statement is used in conjunction with an if statement. If the condition in the if statement is false, the code within the else block is executed.
# 
# elif:
# The elif statement, short for "else if", is used to specify additional conditions to test after an if statement. If the condition in the if statement is false, the conditions in the elif statements are evaluated in order until one of them is true.
# 
# while:
# The while loop is used to repeat a block of code as long as a certain condition is true. The code within the while loop will be executed repeatedly until the condition is no longer true.
# 
# for:
# The for loop is used to repeat a block of code for a specific number of times or for each element in a collection such as a list or a tuple. The for loop allows you to iterate over a collection and perform a certain action for each element.
# 
# and:
# The and operator is used to combine two or more conditions in a single statement. The conditions are evaluated from left to right and the result of the and operation is only true if all of the conditions are true.
# 
# Loop Controls:
# Loop controls, such as break and continue, allow you to control the flow of execution within loops. The break statement is used to exit a loop early, while the continue statement is used to skip the rest of the code in the current iteration of a loop and move on to the next iteration.
# 
# 
# 
# 
# 

# In[22]:


x = 5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")


# In[23]:


x = 5
if x > 0:
    print("x is positive")


# In[24]:


x = -5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")


# In[25]:


x = 5
if x > 10:
    print("x is greater than 10")
elif x > 0:
    print("x is positive and less than or equal to 10")
else:
    print("x is negative or 0")


# In[26]:


count = 0
while count < 5:
    print(count)
    count += 1


# In[27]:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# In[28]:


x = 5
y = 10
if x > 0 and y > 0:
    print("x and y are positive")
else:
    print("x or y is not positive")


# In[29]:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)


# Line 1: The variable fruits is assigned a list of strings, ["apple", "banana", "cherry"].
# 
# Line 2: A for loop is started to iterate through the items in the fruits list. For each iteration, the variable fruit will take on the value of the current item.
# 
# Line 3: A conditional if statement checks if the current value of fruit is equal to the string "banana".
# 
# Line 4: If the condition in line 3 is true (i.e. fruit is equal to "banana"), the break statement is executed and the loop is immediately terminated.
# 
# Line 5: The value of the current fruit is printed.
# 
# The output of this code will be: apple

# In[30]:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)


# Line 1: The variable fruits is assigned a list of strings, ["apple", "banana", "cherry"].
# 
# Line 2: A for loop is started to iterate through the items in the fruits list. For each iteration, the variable fruit will take on the value of the current item.
# 
# Line 3: A conditional if statement checks if the current value of fruit is equal to the string "banana".
# 
# Line 4: If the condition in line 3 is true (i.e. fruit is equal to "banana"), the continue statement is executed and the current iteration is skipped.
# 
# Line 5: The value of the current fruit is printed.
# 
# The output of this code will be: apple cherry

# ### 'break' stops the execution of the loop and moves the control outside the loop. On the other hand, 
# ### 'continue' skips the current iteration and moves on to the next one, without stopping the loop.

# ### This below section is from a QNA Session

# The below code was question from one of the participant and tried to help him with solution
# 
# His code was 
# 
# from functools import reduce
# i = [1,2,3,4,5,4]
# reduce(lambda x: x+1,1)
# 
# 
# The reduce function takes two arguments, the first being the function to apply to the elements of the list, and the second being the list. In the code you've provided, the second argument is 1, which is not a list, and will raise a TypeError.
# 
# The function passed as the first argument to reduce, lambda x: x+1, only takes one argument x. The reduce function requires a function that takes two arguments, as it applies the function to the elements of the list in pairs.
# 

# In[31]:


from functools import reduce

i = [1, 2, 3, 4, 5, 4]
reduce(lambda x, y: x + [y + 1], i, [])


# Ignore above code
# 
# In this code, the lambda function takes two arguments x and y and returns x + [y + 1], where y + 1 adds 1 to each element of the list i. The reduce function accumulates the results of the lambda function and returns a new list with each element increased by 1. The final value is stored in the result variable.

# ### Section ends here 

# ### Placeholder 
# 
# Placeholders are used in string formatting to represent values that will be filled in later. In Python, there are several ways to format strings and placeholders are used in some of these methods.
# 
# One way to use placeholders in Python is by using the % operator with the % operator. 
# 
# In this example, the placeholders %s and %d represent the data types that will be filled in. The %s placeholder represents a string and the %d placeholder represents an integer. The values of name and age are then passed in after the string as a tuple.
# 
# Another way to use placeholders in Python is by using the format() method. 
# 
# In this example, the curly braces {} serve as placeholders for the values that will be filled in. The values of name and age are then passed in as arguments to the format() method.
# 
# f-strings, introduced in Python 3.6, provide yet another way to format strings and use placeholders. 

# In[32]:


name = "Matta"
age = 35

print("My Name is {actualname} and age is {actualage}".format(actualage=age,actualname=name))


# In[33]:


name = "John"
age = 30
message = "My name is %s and I am %d years old" % (name, age)
print(message)

# Output: My name is John and I am 30 years old


# In[34]:


name = "John"
age = 30
message = "My name is {} and I am {} years old".format(name, age)
print(message)

# Output: My name is John and I am 30 years old


# In[35]:


name = "John"
age = 30
message = f"My name is {name} and I am {age} years old"
print(message)

# Output: My name is John and I am 30 years old


# In[36]:


name = "Matta"
age = 35
degree = "BCA"

print(f"My name is {name}, I am a {degree} graduate and my age is {age} .") # with f string format
print("My name is {name}, I am a {degree} graduate and my age is {age} .") # without f string formating 
print(f"My name is {name}, I am a {degree} graduate and my age is {age}".format(name,age,degree)) # with .format string formating
print(f"My name is {name}, I am a {degree} graduate and my age is {age}".format(name,age,degree))


# ### Control Flow
#    **Here, we are going to review and learn the most fundamentals of Python control flow: Decision making statement and loops.**

# In[37]:


## IF Statements 
## ==.>=,<=
age=18
if age>=18: ## Indentation -  after a if statement the ':' will automatically add indentation and start from a new line so that it understands that it inside the if block

    print("You are eligible to vote")
    
    


# In[38]:


if age<=18:
    print("you are not eligible")


# In[39]:


age = 17 
if age<18:
    print("you are not eligible")


# In[ ]:


# Input function allows to get imput from user and the default data type for Input function is String 

name=input("Enter your name ") # Here we are only deifining the variable but the data is entered by the user with input function


# In[ ]:


name


# In[ ]:


age=int(input("Enter tyour age ")) #This is the use of Type casting, Since the default datatype for Input is string 
# and if we want user to enter the age then we can typecast the Int function for the Input function


# In[ ]:


# Task
# take a input oif age
# check whether age >=18 and age <45
# display a message you are young blood

age=int(input("enter your age "))
if age>=18 and age<=40:
    print("You are young blood")
else:
    print("You are legend")


# In[ ]:


#Assignment 
# bill amount for shopping is take input from user
# if money is greater than 1000rs - 20% off
# print the product price after discount 
# if amount is less than = 1000 then 10% off 
# print the product price 


TotalBillAmount=int(input("Enter the Amount"))
if TotalBillAmount>1000:
    print(TotalBillAmount-TotalBillAmount*20/100)
if TotalBillAmount<=1000:
    print(TotalBillAmount-TotalBillAmount*10/100)
    
    


# In[ ]:


product_price = int(input("Enter the Price "))
if product_price > 1000:
    print("The Price after discount is {}".format(product_price * 0.8))
else:
    print("The Price after discount is {}".format(product_price * 0.9))


# In[ ]:


#Assignment 
# bill amount for shopping is take input from user
# if money is greater than 3000 - 20% off
# print the product price after discount 
# if money is greater than equal to 2000 and less than equal to 3000 - 15% off
# print the product price after discount 
# if money is greater than equal to 1000 and less than equal to 2000 - 10% off
# print the product price after discount 
# if money is less than equal to 1000  - 5% off
# print the product price after discount 

product_price = int(input("Enter the Price ₹"))
if product_price > 3000:
    print("The Price after discount is ₹{}".format(product_price * 0.8))
elif product_price>=2000 and product_price<=3000:
    print("The Price after discount is ₹{}".format(product_price * 0.85))
elif product_price>=1000 and product_price<=2000:
    print("The Price after discount is ₹{}".format(product_price * 0.90))
elif product_price<1000 and product_price>=500:
    print("The Price after discount is ₹{}".format(product_price * 0.95))
else:
    print("Thank you for Shopping with us, Enjoy discounts from 5% to 20% for amount more than ₹500")

    


# Retrospectrive : I have a habbit of not entering variable while using the comparison operators >= and <= 
# 
# My code was like this : 
# 
# if product_price > 3000:
#     print("The Price after discount is ₹{}".format(product_price * 0.8))
# elif product_price>=2000 and <=3000:
#     print("The Price after discount is ₹{}".format(product_price * 0.85))
# elif product_price>=1000 and <=2000:
#     print("The Price after discount is ₹{}".format(product_price * 0.90))
# elif product_price<1000 and >=500:
#     print("The Price after discount is ₹{}".format(product_price * 0.95))
# else:
#     print("Thank you for Shopping with us, Enjoy discounts from 5% to 20% for amount more than ₹500")

# In[ ]:


if product_price > 3000:
    print("The Price after discount is ₹{}".format(product_price * 0.8))
elif product_price>=2000 and <=3000:
    print("The Price after discount is ₹{}".format(product_price * 0.85))
elif product_price>=1000 and <=2000:
    print("The Price after discount is ₹{}".format(product_price * 0.90))
elif product_price<1000 and >=500:
    print("The Price after discount is ₹{}".format(product_price * 0.95))
else:
    print("Thank you for Shopping with us, Enjoy discounts from 5% to 20% for amount more than ₹500")


# #### Nested IF statements

# In[ ]:


product_price = int(input("Enter the Price ₹"))
if product_price > 3000:
    print("The Price after discount is ₹{}".format(product_price * 0.8))
    if product_price==3999: #nested if statement
        print("congratulations, you are eligible for a free gift")
elif product_price>=2000 and product_price<=3000:
    print("The Price after discount is ₹{}".format(product_price * 0.85))
elif product_price>=1000 and product_price<=2000:
    print("The Price after discount is ₹{}".format(product_price * 0.90))
elif product_price<1000 and product_price>=500:
    print("The Price after discount is ₹{}".format(product_price * 0.95))
else:
    print("Thank you for Shopping with us, Enjoy discounts from 5% to 20% for amount more than ₹500")

    


# ##### Round Off

# In[1]:


product_price = int(input("Enter the Price ₹"))
if product_price > 3000:
    discounted_price = round(product_price * 0.8, 3)
    print("The Price after discount is ₹{}".format(discounted_price))
    if product_price == 3999: # nested if statement
        print("Congratulations, you are eligible for a free gift")
elif product_price >= 2000 and product_price <= 3000:
    discounted_price = round(product_price * 0.85, 3)
    print("The Price after discount is ₹{}".format(discounted_price))
elif product_price >= 1000 and product_price <= 2000:
    discounted_price = round(product_price * 0.90, 3)
    print("The Price after discount is ₹{}".format(discounted_price))
elif product_price < 1000 and product_price >= 500:
    discounted_price = round(product_price * 0.95, 3)
    print("The Price after discount is ₹{}".format(discounted_price))
else:
    print("Thank you for Shopping with us, Enjoy discounts from 5% to 20% for amount more than ₹500")


# In[ ]:




