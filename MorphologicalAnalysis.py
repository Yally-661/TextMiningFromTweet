#!/usr/bin/env python
# coding: utf-8

# In[29]:


import re
import MeCab


# In[30]:


def remove_url(text):
    
    r = re.sub("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+",' ',text)
    return r


# In[31]:


def pic_and_analyze_noun(text):
    
    m = MeCab.Tagger ()
    splitted = []
    for x in m.parse(text).splitlines()[:-1] :
        if x.split('\t')[1].split(',')[0] in ['名詞']:
            splitted.append(x.split('\t')[0])
    
    return ' '.join(splitted)


# In[32]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'MorphologicalAnalysis.ipynb'])


# In[ ]:




