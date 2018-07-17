# -*- coding: utf-8 -*-
from selenium import webdriver
import msvcrt, sys, os
import time

li = []
def pass_shield():
    
    while 1:
        ch = msvcrt.getch()
        #循環
        if ch == b'\r':
            msvcrt.putch(b'\n')
            return b''.join(li).decode()
        #退格
        elif ch == b'\x08':
            if li:
                li.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
        #Esc
        elif ch == b'\x1b':
            break
        else:
            li.append(ch)
            msvcrt.putch(b'*')
    

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
acc=input("請輸入帳號:\n")
account.send_keys(acc)
dr.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(2)

print("請輸入密碼:")
password = dr.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.clear()
passw=pass_shield()
password.send_keys(passw)
dr.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()

#dr.quit()