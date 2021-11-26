# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:26:22 2021
AJAX页面解析

@author: -
"""

import lxml.etree as etree
import requests
import json
from urllib.parse import urlencode
from selenium import webdriver
import time

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
url='https://fanyi.baidu.com/'
url1='https://www.baidu.com'


res=requests.get(url=url)
res.encoding=res.apparent_encoding
#保存txt和html
# print(res.text)
# with open('E:/XPP-1/xpp-exercise/video-word/url-baidu001.html','w',encoding=('utf-8')) as fp:
#     fp.write(res.text)

# xpath打开txt和html
# html=etree.HTML('E:/XPP-1/xpp-exercise/video-word/url-baidu001.txt')
# result=html.xpath('//*')
# print(result)

html1=etree.parse('E:/XPP-1/xpp-exercise/video-word/url-baidu001.html',etree.HTMLParser())
result1=html1.xpath('//a/text()')
result2=html1.xpath('//a[@href="https://passport.baidu.com/v2/?login"]/@class')
print(result1,result2)






# browser=webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
# browser.get(url=url1)
# print(browser.page_source)
# browser.find_element_by_xpath('//div[@class="output-mod dictionary-wrap dictionary-wrap-f result-section"]')
# input=browser.find_element_by_xpath('//*[@id="kw"]')
# input.send_keys('apple')
# time.sleep(2)
# input.clear()
# input.send_keys('python')
# input2=browser.find_element_by_xpath('//*[@class="bg s_btn"]')
# input2.click()
# time.sleep(10)
# browser.close()


