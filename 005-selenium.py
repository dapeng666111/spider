# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:11:55 2021

@author: dap
"""

from selenium import webdriver
import time

url='https://www.bilibili.com/video/BV1Mb411e7re?p=17'
url1='https://www.baidu.com'
browser=webdriver.Chrome()
browser.get(url=url1)

# 查找节点
# browser.find_element_by_id()
# browser.find_element_by_xpath()

#百度输入查找
#输入文字时用 send_keys （）方法，清空文字时用 clear （）方法，点击按钮时用 click （）方法
# input=browser.find_element_by_id('kw')
# input.send_keys('无人机')
# button=browser.find_element_by_xpath('//input[@value="百度一下"]')
# button.click()

#子frame链接



time.sleep(5)
browser.close()
