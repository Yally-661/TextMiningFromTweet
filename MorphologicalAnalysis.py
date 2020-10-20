#!/usr/bin/env python
# coding: utf-8

# In[29]:


import re
import MeCab


# In[30]:


def remove_url(text):
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


# In[31]:


def pic_and_analyze_noun(text):
    '''
    文字列を形態素解析し名詞のみを抽出する

    Parameters
    ----------
    text : str
        形態素解析する文字列

    Returns
    -------
    ' '.join(splitted) : str
        名詞のみを抽出した文字列(スペース区切り)

    '''
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




