#!/usr/bin/env python
# coding: utf-8

# In[48]:


import re
import json
import sys
from requests_oauthlib import OAuth1Session


# In[49]:


CONSUMER_KEY = 'GH9vERo5nlddVVREXFIpaGAst'
CONSUMER_KEY_SECRET = 'K6Rs5QeT7v9i0b5d5SlxxN4rJqaE9O4dxV5bgdFnKnvpCsMbUI'
ACCESS_TOKEN = '1090500433-zanofeFnpZf0PeJrkhCuk6FzF1Cgq1mq7etWwzN'
ACCESS_TOKEN_SECRET = '7JA2j5D6sCc9o9VX2S6IZgp17QTqxNj9cNHkQEVc94yAX'


# In[ ]:


#ツイートを抽出しJsonで整形する
def get_text(self,user_id):
    twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_KEY_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {'count':'200','screen_name':user_id}

    res = twitter.get(url,params = params)
    
    
    timelines = json.loads(res.text)

    return timelines


# In[8]:





# In[54]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'GetTweet.ipynb'])


# In[ ]:




