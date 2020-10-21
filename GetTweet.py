#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import json
import sys
from requests_oauthlib import OAuth1Session


# In[4]:


CK = 'GH9vERo5nlddVVREXFIpaGAst' #CONSUMER_KEY
CS = 'K6Rs5QeT7v9i0b5d5SlxxN4rJqaE9O4dxV5bgdFnKnvpCsMbUI' #CONSUMER_KEY_SECRET
AT = '1090500433-zanofeFnpZf0PeJrkhCuk6FzF1Cgq1mq7etWwzN' #ACCESS_TOKEN
AS = '7JA2j5D6sCc9o9VX2S6IZgp17QTqxNj9cNHkQEVc94yAX' #ACCESS_TOKEN_SECRET


# In[12]:


class TwitterAPI:
    
    def __init__(self):
        self.session = OAuth1Session(CK, CS, AT, AS)
        self.max_id = 0
        
    def __fetch_timelines(self,user_id):
        '''
        Twitter APIから指定したユーザーの過去ツイートをすべて取得する(RT除く)

        Parameters
        ----------
        user_id : str
            ツイートを取得するユーザーID

        Returns
        -------
        tweet_list : list
            全ツイート内容

        '''
        #要エラーハンドリング追加
        tweet_list = []
        cnt = 1
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'count':'200','include_rts':'false','screen_name':user_id}
        while True:
            if self.max_id != 0:
                params['max_id'] = self.max_id
            res = self.session.get(url,params = params)
            timelines = json.loads(res.text)
            if len(timelines) == 0:
                break
            tweet_list = self.__picup_tweet_text(timelines)
            print(str(cnt)+'ループ目'+' max_id:' + str(self.max_id))
            cnt += 1
        return tweet_list 
            

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

    
    def __picup_tweet_text(self,timelines):
        tweet_list = []
        for tweet in timelines:
            tweet_list.append(tweet['text'])
        self.max_id = tweet['id']-1
        
        return tweet_list
        
        
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
       # tweet_text = self.__create_text_from_timelines(timelines)
        return timelines


# In[6]:


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


# In[11]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'GetTweet.ipynb'])


# In[ ]:




