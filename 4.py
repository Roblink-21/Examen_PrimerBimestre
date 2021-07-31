#!/usr/bin/env python
# coding: utf-8

# In[1]:


from facebook_scraper import get_posts
import couchdb
import json
import time


# In[6]:


couch=couchdb.Server('http://Rob:RP38490ytFH@127.0.0.1:5984')


nombredb='facebook_olimpico'

db=couch[nombredb]


# In[9]:


i=1
for post in get_posts('groups/873816170157536', pages=10, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[ ]:




