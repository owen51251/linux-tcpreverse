from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyodbc

link=[]
tex=[]
def parsar(dr):
    soup = BeautifulSoup(dr.page_source, "lxml")
    div = soup.find("div", {"class": "main-container container-fluid"})
    soup=div.find_all("p", {"class": "title"})

    
    for i in range(len(soup)):
        links = soup[i].find('a', href=True)
        link.append("https://www.ithome.com.tw"+links['href'])
        tex.append(soup[i].text)

def connect():
    server = r'localhost\sqlexpress' 
    database = 'parsar' 
    username = 'sa' 
    password = '1qaz@WSX' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)      
    return cnxn 
 
def main():

    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    dr = webdriver.Chrome(r'C:\Users\owen\Desktop\chromedriver.exe', chrome_options=chrome_options)   
    url2='https://www.ithome.com.tw/security'
    dr.get(url2)
    time.sleep(2)

    parsar(dr) 
    for i in range(2): 
        if i ==0:  
            dr.find_element_by_xpath('/html/body/div[3]/div/section/div/div[2]/ul/li[11]/a').click()
            parsar(dr) 
            time.sleep(3) 
        else:
            dr.find_element_by_xpath('/html/body/div[3]/div/section/div/div[2]/ul/li[12]/a').click()
            parsar(dr) 
            time.sleep(3)
    for i in range(len(link)):
        print (link[i],tex[i])
    '''
    req=urllib.request.Request('https://www.ithome.com.tw/security')
    response = urllib.request.urlopen(req)
    the_page = response.read()
    '''
    
if __name__=='__main__':
    main()