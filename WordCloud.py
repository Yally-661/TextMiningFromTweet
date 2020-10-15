#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
import MeCab
from wordcloud import WordCloud
import GetTweet as gt


# In[35]:


m = MeCab.Tagger ()


# In[43]:


text = gt.get_tweet_text('Cuscha_661')


# In[44]:


splitted = []


# In[45]:


for x in m.parse(text).splitlines()[:-1] :
   if x.split("\t")[1].split(",")[0] in ["名詞"]:
       splitted.append(x.split("\t")[0])


# In[46]:


splitted


# In[47]:


mask = np.array(Image.open('apple.png'))


# In[48]:


mask = np.where(mask == 0, 0, 255)


# In[49]:


# 除外したい単語
stop_text = []

# wordcloudの設定
wordcloud = WordCloud(mask = mask,
            background_color = 'white',
            font_path = 'C:\Windows\Fonts\游ゴシック\YuGothM.ttc',
            collocations = False,
            stopwords = stop_text,
            contour_width=1,contour_color='steelblue').generate(' '.join(splitted))

# wordcloudの作成
wordcloud.to_file('./wordcloud/wordcloud.png')


# In[58]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'GetTweet.ipynb'])


# In[ ]:




