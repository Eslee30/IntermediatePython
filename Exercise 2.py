#!/usr/bin/env python
# coding: utf-8

# ## Exercise 2

# 1. Generate a 1-D array containing 5 random integers from 0 to 100:

# In[24]:


import numpy
from numpy import random


# In[25]:


numpy.__version__


# In[26]:


random.randint(0,100, size=5)


# 2. Generate a 2-D array with 3 rows, each row contains 5 random integers from 0 to 100

# In[27]:


random.randint(0,100, size=(3,5))


# 3. Generate a 1-D array of 30 evenly spaced elements between 1.5 and 5.5, inclusive.

# In[28]:


numpy.linspace(1.5,5.5,30)

