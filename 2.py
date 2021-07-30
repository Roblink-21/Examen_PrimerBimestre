#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Librerias
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API de Twitter########################
ckey = "0wczvh9IwiT9iQyxqbNdr1PrQ"
csecret = "2pxbraO1mUeXJNkAIrHLFguenAcYWzP8x8ulczwT3dvOWM03VL"
atoken = "1415799839380676620-acKNBshhVoOGwe6C0L7zFNOlSgOPyj"
asecret = "U0QYqsDxrpmcnpPOd6ISXOp6jW0mOANC2PUtPIyHTDuIP"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Rob:RP38490ytFH@127.0.0.1:5984') 
try:
    db = server.create('juegos_olimpicos')
except:
    
    db = server['juegos_olimpicos']
    
'''===============TRACK=============='''   

twitterStream.filter(track=['juegosolimpicos','richardcarapaz', 'japon'])


# In[ ]:




