# -*- coding: utf-8 -*-
from selenium import webdriver
import time
dr = webdriver.Chrome(r'C:\Users\owen\Desktop\chromedriver.exe')
#dr.maximize_window() #最大化視窗
dr.set_window_size(240, 320) #設定視窗大小
url2='https://www.google.com/intl/zh-TW/gmail/about/#'
dr.get(url2)
time.sleep(2)

dr.find_element_by_xpath('/html/body/nav/div/a[2]').click()
time.sleep(2)

account = dr.find_element_by_xpath('//*[@id="identifierId"]')
account.clear()
account.send_keys("帳號")
dr.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(2)

password = dr.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.clear()
password.send_keys("密碼")
dr.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()

#dr.quit()
