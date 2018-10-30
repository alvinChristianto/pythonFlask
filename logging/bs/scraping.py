from bs4 import BeautifulSoup
import requests

def scrape():
    l = []
    base_url ="https://www.gsmarena.com/panasonic_eluga_ray_530-9376.php" 


       # Request URL and Beautiful Parse
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    headerDiv = soup.find("div", {"class": "article-info-line page-specs light border-bottom"})
    d = { }

    #product_image = item.find("img", {"class":"product-media__img"})
    d['headerText'] = headerDiv.find("h1").getText()
    # image = image.text.replace('\n', "").strip(
    headerDivSpec = soup.find("div", {"id": "specs-list"})
    headerTbl = headerDivSpec.find("table")
    headerTr1 =  headerTbl.find("tr")
    headerTh = headerTr1.th.getText()
    d['network_Td1'] = headerTr1.contents[1].getText()
    d['network_Td2'] = headerTr1.contents[3].getText()
    d['network_Td3'] = headerTr1.contents[5].getText()
        



           # link


           # product_link = item.find("a", {"class":"product-media__link"}, href=True)


           # product_link = 'https://www.bukalapak.com' + str(product_link.get('href'))


           # d['product_link'] = product_link
    l.append(d)
    return l
if __name__ == "__main__":
    print(scrape())

