#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Librerias
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

#Variables
db_client = MongoClient()
my_db = db_client.juegos
my_posts = my_db.posts
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[10]:


response = requests.get("https://resultados.as.com/resultados/juegos_olimpicos/medallero/")
soup = BeautifulSoup(response.content, "lxml")

Sport=[]
Event=[]
Country=[]
Start_Time=[]


post_all = soup.find_all("td", class_="table-estadisticas-team")
post_Country=soup.find_all("a", title_="Ver medallero: China")

extracted = []
    
for element in post_country:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Country.append(limpio.strip())

for element in post_event:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Event.append(limpio.strip())

for element in post_sport:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Sport.append(limpio.strip())

    
for element in post_country:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Sport.append(limpio.strip())






# In[ ]:




