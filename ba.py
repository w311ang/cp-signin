import requests
import time
import os
import pas

name='苦力怕签到'
pw=os.getenv('talk_pw')
host=os.getenv('host')
frppw=os.getenv('pw')

def send(content):
  global name,pw
  pas.pas(host.replace('http://','https://'),frppw)
  name="<font color='5BA783'>"+name+'</font>'
  ticks=str(int(time.time()))
  file={'username':(None,name),'file':('captcha_'+ticks,content)}
  re=requests.post(host+'/Meow-Chat/image.php',files=file).text
  print(re)
  re=requests.get(host+'/Meow-Chat/write.php?password=%s&message=%s&username=%s'%(pw,'请输入验证码',name)).text
  print(re)
