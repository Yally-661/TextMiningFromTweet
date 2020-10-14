#!/usr/bin/env python
# coding: utf-8

# In[25]:


import re
import json
import sys
from requests_oauthlib import OAuth1Session


# In[26]:


CONSUMER_KEY = 'GH9vERo5nlddVVREXFIpaGAst'
CONSUMER_KEY_SECRET = 'K6Rs5QeT7v9i0b5d5SlxxN4rJqaE9O4dxV5bgdFnKnvpCsMbUI'
ACCESS_TOKEN = '1090500433-zanofeFnpZf0PeJrkhCuk6FzF1Cgq1mq7etWwzN'
ACCESS_TOKEN_SECRET = '7JA2j5D6sCc9o9VX2S6IZgp17QTqxNj9cNHkQEVc94yAX'


# In[27]:


#ツイートを抽出
def __get_tweet(user_id):
    twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_KEY_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {'count':'1000','screen_name':user_id}
    
    res = twitter.get(url,params = params)
    timelines = json.loads(res.text)
    tweets = []
    for x in timelines:
        tweets.append(x['text'])
    
    return tweets


# In[28]:


#getter
def get_tweet_text(tweet_user):
    return  __get_tweet(tweet_user)


# In[29]:


get_tweet_text('03natsuki30')


# In[30]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'GetTweet.ipynb'])


# In[ ]:




