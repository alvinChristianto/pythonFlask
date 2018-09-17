from bs4 import BeautifulSoup
import urllib2

with open("python.html") as py:
    soup = BeautifulSoup(py, "lxml")

#soup = BeautifulSoup(soup, "lxml")

#url = "https://www.pythonforbeginners.com"

#content = urllib2.urlopen(url).read()

#soup = BeautifulSoup(content, "lxml")

#print soup.prettify()

#print title
#>>'title'? Python For Beginners

#print soup.title.string
#>> Pythonforbeginners.com - Learn Python by Example

#print soup.p
#none

#print soup.a.img
#<img alt="pythonforbeginners.com" src="/static/img/pfb_logo.png"/>

for link in soup.find_all('a'):
   
   # print(link.get('href')
    print link.get_text()
