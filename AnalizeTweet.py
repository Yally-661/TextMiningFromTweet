#!/usr/bin/env python
# coding: utf-8

# In[1]:


import MeCab
import GetTweet


# In[2]:


m = MeCab.Tagger ()


# In[3]:


x = GetTweet()


# In[4]:


x.get_text('Cuscha_661')


# In[8]:


splitted = []


# In[10]:


for x in m.parse(timeline).splitlines()[:-1] :
   if x.split('\t')[1].split(',')[0] in ['名詞']:
       splitted.append(x.split('\t')[0])


# In[1]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'AnalizeTweet.ipynb'])


# In[ ]:




