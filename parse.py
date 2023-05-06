import requests
from bs4 import BeautifulSoup
data=requests.get("https://mindstale.com/")
#print(data.content)
soup = BeautifulSoup(data.content,features="html.parser")
#print(soup.html.head.title)
#print(soup.find_all("a"))
for a in (soup.find_all("a")):
    print(a)