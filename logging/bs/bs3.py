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


logger.info('app started!!')
url1 = "https://www.gsmarena.com/panasonic_eluga_ray_530-9376.php"
url2 = "https://www.gsmarena.com/apple_iphone_xs-9318.php"
url3 = "https://www.gsmarena.com/apple_iphone_8_plus-8131.php"
url = [url1, url2, url3]

for x in url :
    print x

    content = urllib2.urlopen(x).read()

    soup = BeautifulSoup(content, "lxml")


    headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
    headerText = headerDiv.find("h1").getText()


    headerDivSpec = soup.find("div", {"id": "specs-list"})
    headerTbl = headerDivSpec.find("table")

    headerTr1 =  headerTbl.find("tr")
    headerTh = headerTr1.th.getText()
#headerTd = headerTr.find("td", {"class" : "nfo"}).getText()
    network_Td1 = headerTr1.contents[1].getText()
    network_Td2 = headerTr1.contents[3].getText()
    network_Td3 = headerTr1.contents[5].getText()
    headerTblNext = headerTbl.find_next_sibling("table")

    headerTr2 =  headerTblNext.find("tr")
    launch_Td21 = headerTr2.contents[1].getText()
    launch_Td22 = headerTr2.contents[3].getText()
    launch_Td23 = headerTr2.contents[5].getText()

    headerTr2Next = headerTr2.find_next_sibling("tr")
    launch_status_Td21 = headerTr2Next.contents[1].getText()
    launch_status_Td22 = headerTr2Next.contents[3].getText()

    headerThN = headerTr2.th.getText()
#headerThN1 = headerThN.find("rowspan").getText()
    headerTdN = headerTr2.find("td", {"class" : "nfo"}).getText()




#    print "cek 1 :"+str(network_Td1)+str(network_Td2)+str(network_Td3)
#    print "cek 2 :"+str(launch_Td21)+str(launch_Td22)+str(launch_Td23)
#    print "cek 3 :"+str(launch_status_Td21)+str(launch_status_Td22)

    logger.info('Name of phone : %s' %headerText)
    logger.info('%s : %s' %(network_Td1, network_Td3))
    logger.info('%s : %s' %(launch_Td21, launch_Td23))
    logger.info('%s : %s' %(launch_status_Td21, launch_status_Td22))
    logger.debug('------------------')
logger.info('App Finished!')



#for link in soup.find_all('a'):
   
   #print link.get('href')
 #  print link.get_text()
