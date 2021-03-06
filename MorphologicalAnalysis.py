#!/usr/bin/env python
# coding: utf-8

import re
import MeCab


def remove_url_and_mention_from_text(text,url = True,mention = True):
    '''
    文字列からurlと@メンションをすべて取り除く

    Parameters
    ----------
    text : str
        urlと@メンションを取り除く文字列

    Returns
    -------
    r : str
        urlと@メンションを取り除いた文字列

    '''
    if url:
        text = re.sub("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+",' ',text)
    if mention:
        text = re.sub(r"@([A-Za-z0-9_]+) ",' ',text)
    return text


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
        ひらがな始まり、url、メンション除く

    '''
    url_removed = remove_url_and_mention_from_text(text)    
    m = MeCab.Tagger ()
    splitted = []
    pattern = r'[ぁ-ん]+'
    con = re.compile(pattern)
    for x in m.parse(url_removed).splitlines()[:-1] :
        if x.split('\t')[1].split(',')[0] in ['名詞']:
            if con.match(x.split('\t')[0]):
                continue
            splitted.append(x.split('\t')[0])
            
    return splitted



