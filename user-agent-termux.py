#!/data/data/com.termux/files/usr/bin/python
import requests as req
from bs4 import BeautifulSoup
import time

url = 'http://www.useragentstring.com/pages/useragentstring.php?name=Firefox'

def save(br,ua):
  
  file = br+'.txt'

  with open(file,'a') as f:
    f.write(ua+'\n')

def getUa(br):

  url = 'http://www.useragentstring.com/pages/useragentstring.php?name='+br
  r = req.get(url)

  if r.status_code == 200:
    soup = BeautifulSoup(r.content,'html.parser')
  else:
    soup = False

  if soup:
    div = soup.find('div',{'id':'liste'})
    lnk = div.findAll('a')

    for i in lnk:
      try:
        save(br,i.text)
      except:
        print('User Agents not found.')
  else:
    print('No soup for '+br)

lst = ['Firefox','Firefox+Beta','Opera','Opera+Beta','Safari','Chrome','Chrome+Beta','Edge','Edge+Beta','Brave','Brave+Beta','Android+Webkit+Browser','Android+Webkit+Browser+Beta']

for i in lst:
  getUa(i)
  time.sleep(10)