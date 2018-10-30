###
###
from bs4 import BeautifulSoup
import urllib2
import logging

logger = logging.getLogger('MAIN')
logger.setLevel(logging.DEBUG)

log = logging.FileHandler('getUrl.log')
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


logger.info('app started!!')
url = "https://www.gsmarena.com/samsung-phones-9.php"
count = 1 
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "lxml")

headerDiv = soup.find("div", {"class": "makers"})
for x in range(count) : 
    print x
 #   headerText = headerDiv.ul.li.a['href']
    header = headerDiv.ul
    headercek =  header.find_all('a')
   # type(headercek)
    ceklagi =  headercek[2].get('href')
    #headerText = header.next_sibling.a['href']
   # header = headerDiv.ul.li[x]
    logger.debug('------------------')
    #logger.info('https://www.gsmarena.com/%s' %headerText)
    logger.info('App Finished!')

#    print headerText
    print headercek[0]
