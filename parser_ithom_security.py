from bs4 import BeautifulSoup
import urllib.request

req=urllib.request.Request('https://www.ithome.com.tw/security')
response = urllib.request.urlopen(req)
the_page = response.read()
soup = BeautifulSoup(the_page, "lxml")

div = soup.find("div", {"class": "main-container container-fluid"})
soup=div.find_all("p", {"class": "title"})

link=[]
tex=[]
for i in range(len(soup)):
    links = soup[i].find('a', href=True)
    link.append("https://www.ithome.com.tw"+links['href'])
    tex.append(soup[i].text)
print (link,tex)