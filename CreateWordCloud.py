#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
from wordcloud import WordCloud
import GetTweet as gt
import MorphologicalAnalysis as ma


# In[2]:


def create_word_cloud(text,mask):
    stop_text = ''
    # wordcloudの設定
    wordcloud = WordCloud(mask = mask,
                background_color = 'white',
                font_path = 'C:\Windows\Fonts\游ゴシック\YuGothM.ttc',
                collocations = False,
                stopwords = stop_text,
                contour_width = 2,
                contour_color='black').generate(text)

    # wordcloudの作成
    wordcloud.to_file('./wordcloud/wordcloud.png')
    print('ワードクラウド出力')


# In[3]:


if __name__ == '__main__':
    mask = np.array(Image.open('apple.png'))
    mask = np.where(mask == 0, 0, 255)
    timeline = gt.get_timeline('Cuscha_661')
    analyzed = ma.picup_noun(' '.join(timeline))
    create_word_cloud(' '.join(analyzed),mask)


# In[8]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'CreateWordCloud.ipynb'])


# In[ ]:




