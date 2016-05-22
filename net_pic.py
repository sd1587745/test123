__author__ = 'X'
from urllib import request
from html.parser import HTMLParser
import re
from bs4 import BeautifulSoup
from http import cookiejar

#cookie = cookiejar.CookieJar()
#handler = request.HTTPCookieProcessor(cookie)
#opener = request.build_opener(handler)
#response = opener.open('http://www.baidu.com')
#
#for iterm in cookie:
#    print('Name = '+iterm.name)
#    print('Value = '+iterm.value)
#


localpath = 'D:\\net_pic\\gif\\'
name = 100
reg = re.compile(r'img src=\'(https://3\d.{,100}\.gif)')

web = request.Request('http://dz.tuiaa.com/htm_data/7/1511/1736948.html')
web.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
try:
    f = request.urlopen(web)
    data =f.read().decode('GBK')
#    print(data)
    imglist = reg.findall(data)
#    for x in imglist:#
#
#        request.urlretrieve(x,localpath+str(name)+'.gif')
#        print(name,x,'is done.')
#        name +=1
    print('\nAll done!')
except request.HTTPError as e:
    print(e.code)
    print(e.reason)




