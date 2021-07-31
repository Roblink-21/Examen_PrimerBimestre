#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
import pandas as pd


# In[22]:


con=sqlite3.connect("database.db")


# In[9]:


irisData = pd.read_csv('juegosolimpicos1.csv')


# In[10]:


irisData


# In[15]:


olin=pd.DataFrame(irisData)


# In[24]:


olin.to_sql('irisData', con) 


# In[ ]:




