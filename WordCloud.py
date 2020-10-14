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


# In[59]:


# 作成したテキストの読み込み
with open('analyze2.txt', 'r') as f:
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


# In[62]:


m = MeCab.Tagger ()
print(m.parse ("すもももももももものうち"))


# In[86]:


splitted = ' '.join([x.split("\t")[0] for x in m.parse(text).splitlines()[:-1] if x.split("\t")[1].split(",")[0] not in ["助詞", "助動詞"]])


# In[87]:


splitted


# In[85]:


for i in m.parse(text).splitlines():
    splitted += i.split('\t')[0]
    print(splitted)


# In[1]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'textMining.ipynb'])


# In[ ]:




