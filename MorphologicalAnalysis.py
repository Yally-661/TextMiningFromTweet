#!/usr/bin/env python
# coding: utf-8

# In[29]:


import re
import MeCab


# In[1]:


def remove_url_from_text(text):
    '''
    文字列からurlをすべて取り除く

    Parameters
    ----------
    text : str
        urlを取り除く文字列

    Returns
    -------
    r : str
        urlを取り除いた文字列

    '''
    r = re.sub("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+",' ',text)
    return r


# In[3]:


def picup_noun(text):
    '''
    文字列を形態素解析し名詞のみを抽出する

    Parameters
    ----------
    text : str
        形態素解析する文字列

    Returns
    -------
    splitted : list
        名詞のみを抽出したリスト

    '''
    m = MeCab.Tagger ()
    splitted = []
    for x in m.parse(text).splitlines()[:-1] :
        if x.split('\t')[1].split(',')[0] in ['名詞']:
            splitted.append(x.split('\t')[0])
    
    return splitted


# In[33]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'MorphologicalAnalysis.ipynb'])


# In[ ]:




