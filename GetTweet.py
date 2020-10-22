#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import json
import sys
from requests_oauthlib import OAuth1Session


# In[3]:


CK = 'GH9vERo5nlddVVREXFIpaGAst' #CONSUMER_KEY
CS = 'K6Rs5QeT7v9i0b5d5SlxxN4rJqaE9O4dxV5bgdFnKnvpCsMbUI' #CONSUMER_KEY_SECRET
AT = '1090500433-zanofeFnpZf0PeJrkhCuk6FzF1Cgq1mq7etWwzN' #ACCESS_TOKEN
AS = '7JA2j5D6sCc9o9VX2S6IZgp17QTqxNj9cNHkQEVc94yAX' #ACCESS_TOKEN_SECRET


# In[29]:


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
            ツイート本文(最大3200件)

        '''
        tweet_list = []
        unavailable_cnt = 0
        cnt = 1
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'count':'200','include_rts':'false','screen_name':user_id}
        while True:
            if self.max_id != 0:
                params['max_id'] = self.max_id
            res = self.session.get(url,params = params)
            if res.status_code == 503:
                #503 Service Unavailable
                unavailable_cnt += 1
                if unavailable_cnt == 10:
                    raise Exception('Twitter API error %d' % res.status_code)
                #503エラー10回で処理中断
                print('503: %d 回目' % unavailable_cnt)
                continue;
            if res.status_code != 200:
                #503以外のエラーの場合
                raise Exception('Twitter API error %d' % res.status_code)
            timelines = json.loads(res.text)
            if len(timelines) == 0:
                break
            tweet_list = self.__picup_text_and_set_max_id(tweet_list,timelines)
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

    
    def __picup_text_and_set_max_id(self,tweet_list,timelines):
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
        timelines : list
            ツイートの本文(最大3200件)

        '''    
        timelines = self.__fetch_timelines(user_id)
       # tweet_text = self.__create_text_from_timelines(timelines)
        return timelines


# In[28]:


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


# In[26]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'GetTweet.ipynb'])


# In[ ]:




