#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Librerias
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API de Twitter########################
ckey = "*************************"
csecret = "*************************************************"
atoken = "***************************************************"
asecret = "**************************************************"
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
    #db = server.create('paris_francia')
    #db = server.create('berlin_alemania')
    db = server.create('florida_eeuu')
except:
    #db = server['paris_francia']
    #db = server['berlin_alemania']
    db = server['florida_eeuu']
    
'''===============LOCATIONS=============='''   

#Pais-Ciudad: Paris-Francia
#twitterStream.filter(locations=[2.224122,48.815575,2.46976,48.902156])   


#Pais-Ciudad: Berlin-Alemania
#twitterStream.filter(locations=[-89.912101,39.750371,-89.893165,39.764932])   

#Pais-Ciudad: Florida-EEUU
twitterStream.filter(locations=[-87.63,24.4,-79.97,31.0])   


# In[ ]:




