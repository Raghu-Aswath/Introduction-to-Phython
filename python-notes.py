#!/usr/bin/env python
# coding: utf-8

# # python-notes
# 
# Use the "Run" button to execute the code.

# In[ ]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[ ]:


import jovian


# In[120]:


# Execute this to save new versions of the notebook
jovian.commit(project="python-notes")


# ### Introduction to Phython:

# ### What is Python?
# • Python is a popular general-purpose 
# programming language that can be used for 
# a wide variety of applications.
# 
# • Python is currently the most widely used 
# multi-purpose, high-level programming 
# language.
# 
# • Python allows programming in ObjectOriented and Procedural paradigms.
# 
# • Python programs generally are smaller than 
# other programming languages like Java.
# 
# • Programmers have to type relatively less and 
# indentation requirement of the language, 
# makes them readable all the time

# ### Print function
# The print() function prints the specified message to the screen, or other standard output device.
# 
# The message can be a string, or any other object, the object will be converted into a string before written to the screen.

# In[3]:


#example
print("Hellow World")
print("Raghu")
print("Raghu", "Mysore", "Data Science")


# ### 'Seperator' and 'End' functions in print
# 	sep = Specify how to separate the objects, if there is more than one. Default is ' '
# 	end = Specify what to print at the end. Default is '\n' (line feed)

# In[4]:


#example---- "\n" denotes new line
print("Name : Raghu", "Place : Mysore", "Course : Data Science", sep = "\n", end = "\n")
print("Welcome to Mysore")


# In[6]:


print ("A", "B", sep = "*", end = "-")
print("string")


# # Phython Data Types

# ### 1. Integer : 'int'
# 
# This value is represented by int class. It 
# contains positive or negative whole numbers (without 
# fraction or decimal). In Python there is no limit to how 
# long an integer value can be

# In[9]:


#example
a = 20                #"type" function is used to show the type of data stored in a declared variable
print(type(a))
b = 30
print(type(b))


# ### 2. Float : 'float'
# 
# This value is represented by float class. It is a real 
# number with floating point representation. It is specified 
# by a decimal point. Optionally, the character e or E 
# followed by a positive or negative integer may be 
# appended to specify scientific notation.

# In[16]:


#example
c = 3.5
print(type(c))

d = 4.5
print(type(d))


# ### 3. Complex Numbers : 'complex'
# 
# Complex number is represented by 
# complex class. It is specified as (real part) + (imaginary 
# part)j. For example – 2+3j

# In[17]:


e = 13+9j
print(type(e))

f = 3.5+9.5j
print(type(f))


# ### 4. List : '[ ]'
# 
# Lists are just like the arrays, declared in 
# other languages which is a ordered 
# collection of data. It is very flexible as the 
# items in a list do not need to be of the same 
# type

# In[21]:


g = [1, 2.5, "Python", "string"]
print(type(g))
h = []                    #empty list is defined as '[]'
print(type(h))


# * Indexing in List
#  
# Indexing starts from 'Zero' and count of number of elements in the list.
# 
# we can also count the number of elements in the list using 'len' function.
# 
# Stytax : x [i] :  
# 
# 'x' is the declared variable
# 
# 'i' is the index value

# In[25]:


g = [1, 2.5, "Python", "string"]
print(g[0])
print(g[1])
print(g[2])
print(g[3])


# In[37]:


#nested indexing : if you want to access the elements of string inside the list
#here index of string "python" is 2 and and index of 'P' inside string is 0 
g = [1, 2.5, "Python", "JUPYTER"]
print(g[2][0])
print(g[2][1])
print(g[2][2])
print(g[2][3])
print(g[2][4])
print(g[2][5])
len(g)            #'len' function is used to find the number of elements in the list


# In[50]:


g = [1, 2.5, "Python", "JUPYTER"]
print(g[3][0])
print(g[3][1])
print(g[3][2])
print(g[3][3])
print(g[3][4])
print(g[3][5])
print(g[3][6])

print(len(g[3]))            #we can also use index value in 'len' function
                            # here the length of the string "JUPYTER" IS 7 and "string" is 6
print(len(g[2]))


# * List is mutable : you can change the values in the list

# In[54]:


#example
L = ['a','b','c','1', 2, 3.5, "python"]
L


# In[58]:


#if you want to change the list complitely
L = ['string', 1,2,3,"pyton",20.5]
print(L)                                       #now the list 'L' have complete different element


# In[65]:


#if you want to change the values of certain elements in the list use indenxing function
#example
L = ['string', 1,2,3,"pyton",20.5]
L[0] = 1
L[1] = '2'
print(L)
print(type(L[0]))          # in index 0 string data type is converted into integer whereas in index 1 its string
print(type(L[1]))


# In[117]:


L = ['Silk', 1,2,3,"Metro",20.5]
x = L[0]
for x in L[0]:
    z = print(x)
    l == 1
    break
a = 'M'
z = a
x = a
print(a)
print(L)


# In[119]:


txt = "raghu A"

x = txt.split()

print(x)


# In[100]:


txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)


# In[ ]:




