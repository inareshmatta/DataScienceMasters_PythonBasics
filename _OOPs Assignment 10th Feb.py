#!/usr/bin/env python
# coding: utf-8

# #### Q1. Which function is used to open a file? What are the different modes of opening a file? Explain each mode of file opening.

# The open() function is used to open a file in Python. It takes two arguments: the filename and the mode in which the file should be opened.
# 
# There are several modes in which a file can be opened:  
# 
# r: Read mode - This mode is used for reading files. It is the default mode. If the file does not exist in read mode, an error will occur.  
# 
# w: Write mode - This mode is used for writing files. If the file already exists, it will be truncated and the new data will be written to it. If the file does not exist, a new file will be created.  
# 
# a: Append mode - This mode is used for appending data to a file. If the file already exists, the new data will be written to the end of the file. If the file does not exist, a new file will be created.  
# 
# x: Exclusive mode - This mode is used for creating a new file. If the file already exists, an error will occur.  
# 
# b: Binary mode - This mode is used for reading or writing binary data like images, audio, etc. It can be combined with the other modes. For example, rb is read mode in binary.  
# 
# t: Text mode - This mode is used for reading or writing text data. It can be combined with the other modes. For example, wt is write mode in text.  
# 
# +: Read and write mode - This mode is used for both reading and writing to a file.  

# #### Q2. Why close() function is used? Why is it important to close a file?

# The close() function is used in Python to close a file that has been opened using the open() function. It is important to close a file once you are done using it because it frees up system resources that were being used to keep the file open. If you do not close a file, the operating system will eventually close it for you, but there is no guarantee when this will happen, and in the meantime, the file will be unavailable for use by other programs.
# 
# Moreover, when a file is not properly closed, data that has not yet been written to disk may be lost. This can happen if the program terminates unexpectedly, or if the operating system crashes. Closing the file ensures that all data has been written to disk and that the file is in a consistent state.
# 
# In summary, it is important to always close files that have been opened to free up system resources, prevent data loss, and ensure the file is in a consistent state.

# #### Q3. Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then close the file. Open this file and read the content of the file.

# In[1]:


# Create a text file
file = open("my_file.txt", "w")

# Write to the file
file.write("I want to become a Data Scientist")

# Close the file
file.close()

# Reopen the file to read the content
file = open("my_file.txt", "r")
content = file.read()

# Print the content of the file
print(content)

# Close the file again
file.close()


# #### Q4. Explain the following with python code: read(), readline() and readlines().

# In Python, the read(), readline(), and readlines() methods are used for reading data from a file.
# 
# read(): This method is used to read the entire content of a file. It reads and returns the content of the entire file as a string.

# readline(): This method is used to read a single line from a file. It reads and returns a single line from the file.

# readlines(): This method is used to read all the lines from a file and return them as a list of strings. Each element in the list represents a line from the file.

# #### Q5. Explain why with statement is used with open(). What is the advantage of using with statement andopen() together?

# The with statement in Python is used to wrap the execution of a block of code within the context of a particular resource, such as a file. The primary advantage of using the with statement with open() function is that it automatically takes care of closing the file once the block of code under the with statement has executed. This eliminates the need for explicitly calling the close() method of the file object.

# #### Q6. Explain the write() and writelines() functions. Give a suitable example.

# he write() function is used to write a single string to a file, while the writelines() function is used to write multiple strings to a file, typically in the form of a list. Both functions are used to write data to a file.
# 
# The write() function takes a string argument and writes it to the file. If the file doesn't exist, it will be created automatically. If the file already exists, the existing contents of the file will be overwritten.

# The writelines() function takes an iterable (like a list or a tuple) of strings as an argument, and writes each string to the file. Each string will be written on a new line in the file.

# In[3]:


# Open a file in write mode
file = open("example.txt", "w")

# Write a string to the file
file.write("This is an example file.")

# Close the file
file.close()


# In[4]:


# Open a file in write mode
file = open("example.txt", "w")

# Write multiple lines to the file
lines = ["This is the first line.", "This is the second line.", "This is the third line."]
file.writelines(lines)

# Close the file
file.close()


# In[ ]:




