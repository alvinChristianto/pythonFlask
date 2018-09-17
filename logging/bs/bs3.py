from bs4 import BeautifulSoup
import urllib2
import logging
#with open("python.html") as py:
#   soup = BeautifulSoup(py, "lxml")

#soup = BeautifulSoup(soup, "lxml")
logger = logging.getLogger('MAIN')
logger.setLevel(logging.DEBUG)

log = logging.FileHandler('runlogGsm.log')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#create FORMATER
formatter = logging.Formatter('%(asctime)s -  %(name)s : %(levelname)s >> %(message)s')

#add formatter to CH
log.setFormatter(formatter)
ch.setFormatter(formatter)

#add ch to logger
logger.addHandler(log)
logger.addHandler(ch)



url = "https://www.gsmarena.com/apple_iphone_xs-9318.php"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "lxml")

#print soup.prettify()

#print title
#>>'title'? Python For Beginners

#print soup.title.string
#>> Pythonforbeginners.com - Learn Python by Example

#print soup.p
#none
#print soup.a.img
#<img alt="pythonforbeginners.com" src="/static/img/pfb_logo.png"/>
logger.info('app started!!')
headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
headerText = headerDiv.find("h1").getText()
print headerText

headerDivSpec = soup.find("div", {"id": "specs-list"})
headerTbl = headerDivSpec.find("table")
headerTr =  headerTbl.find("tr", {"class":"tr-hover"})
headerTh = headerTr.find("th", {"rowspan": "15"}).getText()
print headerTh

logger.info('name of phone : %s' %headerText)
logger.info('name of connection : %s' %headerTh)
logger.info('App Finished!')
#for link in soup.find_all('a'):
   
   #print link.get('href')
 #  print link.get_text()
