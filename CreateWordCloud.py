#!/usr/bin/env python
# coding: utf-8


from PIL import Image
import numpy as np
from wordcloud import STOPWORDS
from wordcloud import WordCloud
from GetTweet import TwitterAPI
import MorphologicalAnalysis as ma
from matplotlib import pyplot as plt


def create_word_cloud(text,mask = None):
    '''
    テキストからワードクラウドを作成し出力する

    Parameters
    ----------
    text : str
        ワードクラウドを作成する文字列
    mask : ndarray
        マスクする画像

    '''
    wordcloud = WordCloud(mask = mask,
                background_color = 'white',
                font_path = 'C:\Windows\Fonts\游ゴシック\YuGothM.ttc',
                collocations = False,
                
                contour_width = 2,
                contour_color='black').generate(text)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

     
def add_stop_word(stop_list):
    '''
    ワードクラウドから除外する文言をセットする

    Parameters
    ----------
    stop_list : list
        ワードクラウドから除外する文言
    '''
    for x in stop_list:
        STOPWORDS.add(x)


def get_mask(file):
    '''
    画像データをワードクラウドのマスク用に加工する

    Parameters
    ----------
    file : str
        マスク用ファイルのパス
    
    Return
    ----------
    mask : ndarray
        マスク用加工された画像ファイル
    '''
    mask = np.array(Image.open(file))
    mask = np.where(mask == 0, 0, 255)
    return mask


if __name__ == '__main__':
    mask = get_mask(setting.IMAGE)
    add_stop_word(setting.STOP)
    timeline = TwitterAPI().get_timeline(setting.USER)
    analyzed = ma.picup_noun(' '.join(timeline))
    create_word_cloud(' '.join(analyzed))



