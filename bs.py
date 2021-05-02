from bs4 import BeautifulSoup
import requests
import os

host=os.getenv('host')

def receive(ignore):
  notfound=True
  while notfound:
    re=requests.get(host+'/Meow-Chat/read.php').text
    soup=BeautifulSoup(re,features="lxml")
    talk=soup.find_all('div')[-3].find_all('font')[-1].string
    if talk:
      talk=talk.rstrip()
      #print(talk,talk==ignore)
      if not talk==ignore:
        notfound=False
  return talk
