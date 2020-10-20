#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re
import json
import sys
from requests_oauthlib import OAuth1Session


# In[8]:


CONSUMER_KEY = 'GH9vERo5nlddVVREXFIpaGAst'
CONSUMER_KEY_SECRET = 'K6Rs5QeT7v9i0b5d5SlxxN4rJqaE9O4dxV5bgdFnKnvpCsMbUI'
ACCESS_TOKEN = '1090500433-zanofeFnpZf0PeJrkhCuk6FzF1Cgq1mq7etWwzN'
ACCESS_TOKEN_SECRET = '7JA2j5D6sCc9o9VX2S6IZgp17QTqxNj9cNHkQEVc94yAX'


# In[9]:


class TwitterAPI:
    def __fetch_timelines(self,user_id):
        '''
        Twitter APIから指定したユーザーの過去ツイートを取得する(RT除く)

        Parameters
        ----------
        user_id : str
            ツイートを取得するユーザーID

        Returns
        -------
        timelines : dict
            ツイートデータ
            200件分

        '''
        twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_KEY_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'count':'200','include_rts':'false','screen_name':user_id}
        res = twitter.get(url,params = params)
        timelines = json.loads(res.text)
        return timelines 
            

    def __create_text_from_timelines(self,timelines):
        '''
        Twitter APIから抽出したタイムラインの本文を文字列にまとめる

        Parameters
        ----------
        timelines : dict
            Twitter APIから取得したタイムライン

        Returns
        -------
        tweet_text : str
            ツイートの本文をすべてまとめたもの(半角スペース区切り)

        '''
        tweet_text = ''
        for tweet in timelines:
            tweet_text += tweet['text'] + ' '
        return tweet_text


    def get_timeline(self,user_id):
        '''
        ユーザーIDからTwitterタイムラインの本文テキストを取得する(RT除く)

        Parameters
        ----------
        user_id : str
            タイムラインを取得するユーザーID

        Returns
        -------
        tweet_text : str
            ツイートの本文をすべてまとめたもの(半角スペース区切り)

        '''    
        timelines = self.__fetch_timelines(user_id)
        tweet_text = self.__create_text_from_timelines(timelines)
        return tweet_text


# In[10]:


def get_timeline(user_id):
    '''
    ユーザーIDからTwitterタイムラインの本文テキストを取得する(RT除く)

    Parameters
    ----------
    user_id : str
        タイムラインを取得するユーザーID

    Returns
    -------
    tweet_text : str
        ツイートの本文をすべてまとめたもの(半角スペース区切り)

    '''               
    api = TwitterAPI()
    tweet_text = api.get_timeline(user_id)
    return tweet_text


# In[13]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'GetTweet.ipynb'])


# In[ ]:




