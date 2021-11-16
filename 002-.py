# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:58:59 2021

@author: -
"""

import requests
import lxml.etree as etree

if __name__ == '__main__':
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    url='https://www.taobao.com'
    url1='https://bj.58.com/ershoufang/'
    res=requests.get(url=url1, headers=headers)
    res.encoding=res.apparent_encoding
    # with open('../video-word/url-tb.txt','w',encoding='utf-8') as fp:
    #     fp.write(res.text)
    
    tree=etree.HTML(res.text)
    
 
    print(res.text)
    

