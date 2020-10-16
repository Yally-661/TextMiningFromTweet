#!/usr/bin/env python
# coding: utf-8

# In[54]:


from PIL import Image
import numpy as np
from wordcloud import WordCloud
import AnalizeTweet as at


# In[47]:


mask = np.array(Image.open('apple.png'))


# In[48]:


mask = np.where(mask == 0, 0, 255)


# In[49]:


text = at

# 除外したい単語
stop_text = []

# wordcloudの設定
wordcloud = WordCloud(mask = mask,
            background_color = 'white',
            font_path = 'C:\Windows\Fonts\游ゴシック\YuGothM.ttc',
            collocations = False,
            stopwords = stop_text,
            contour_width=1,contour_color='steelblue').generate(' '.join(text))

# wordcloudの作成
wordcloud.to_file('./wordcloud/wordcloud.png')


# In[57]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'CreateWordCloud.ipynb'])


# In[ ]:




