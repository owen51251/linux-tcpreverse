# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request

def parser():
    req=urllib.request.Request('https://www.nccst.nat.gov.tw/Vulnerability')
    response = urllib.request.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page, "lxml")
    divs = soup.find('ul', 'news-list-group')
    soups=divs.select('li')
    link=divs.find_all('a', href=True)
    #print (link[0]['href'])
    #print(soups[0].text)
    for i in range(len(soups)):
        print("%d.%s"%(i+1,soups[i].text.strip("\n")))
        print ("https://www.nccst.nat.gov.tw/"+link[i]['href']+"\n")

def main():
    parser()

if __name__=="__main__":
    main()

