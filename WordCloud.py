#!/usr/bin/env python
# coding: utf-8

# In[26]:


from PIL import Image
import numpy as np
from wordcloud import WordCloud


# In[42]:


mask = np.array(Image.open('apple.png'))


# In[43]:


mask = np.where(mask == 0, 0, 255)


# In[47]:


# 作成したテキストの読み込み
with open('analyze.txt', 'r') as f:
    text = f.read()

# 除外したい単語
stop_text = []

# wordcloudの設定
wordcloud = WordCloud(mask = mask,
            background_color = 'white',
            font_path = 'ProductSans-Regular.ttf',
            collocations = False,
            stopwords = stop_text,
            contour_width=1,contour_color='steelblue').generate(text)

# wordcloudの作成
wordcloud.to_file('./wordcloud/wordcloud.png')


# In[49]:


import MeCab


# In[53]:


m = MeCab.Tagger ("-Owakati")
print(m.parse ("すもももももももものうち"))


# In[ ]:




