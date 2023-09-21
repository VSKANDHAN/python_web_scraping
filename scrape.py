# Here we are scraping the paragraphs from the boston university page with the help of BeautifulSoup 
# and saving the scraped data as json file

import requests
from bs4 import BeautifulSoup
import json
url='https://www.bu.edu/president/boston-university-facts-stats/'

res=requests.get(url)
content=res.content
soup=BeautifulSoup(content,'html.parser')
soup_dict={}
for p in soup.find_all('p'):
    soup_dict[str(p)]=p.text
with open('webscrap.json','w') as file:
    json.dump(soup_dict,file,indent=4)