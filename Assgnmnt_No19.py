#!/usr/bin/env python
# coding: utf-8

# # Assignment 19 Solution

# # 1..Create a function that takes a string and returns a string in which each character is repeated once.

# In[2]:


def double_char(string):
    string = ''
    for i in string:
        string+= i*2
    return string
print(f'{double_char("strings")}')
print(f'{double_char("Hello World")}')
print(f'{double_char("1234!_")}')


# # 2.Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

# In[4]:


def reverse(ibool):
    if type(ibool) == bool:
        return not ibool
    else:
        return "Boolean Expected"
print(f'reverse(True)--{reverse(True)}')
print(f'reverse(False)--{reverse(False)}')
print(f'reverse(0)--{reverse(0)}')
print(f'reverse(None)--{reverse(None)}')


# # 3. Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.

# In[6]:


def num_layer(num):
    outnum = 0.5
    for i in range(num):
        num *= 2
    print(f'output -- {num/1000}m')
num_layer(1)
num_layer(4)
num_layer(21)


# # 4.Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.

# In[7]:


def index_of_caps(string):
    out_string = []
    for i in string:
        if i.isupper():
            out_string.append(string.index(i))
    print(f'{string}--{out_string}')
index_of_caps("eDaBiT")
index_of_caps("eQuINoX")
index_of_caps("determine")
index_of_caps("STRIKE")
index_of_caps("sUn")


# # 5.Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

# In[8]:


def find_even_numb(num):
    out_list = [i for i in range(1,num+1)if i%2 == 0]
    print(f'output--{out_list}')
find_even_numb(8)
find_even_numb(4)
find_even_numb(2)


# In[ ]:




