from bs4 import BeautifulSoup
import requests
import os
import pas

host=os.getenv('host')
frppw=os.getenv('pw')

def receive(ignore):
  pas.pas(host.replace('http://','https://'),frppw)
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
