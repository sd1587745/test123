__author__ = 'X'
from urllib import request
from bs4 import BeautifulSoup

url ='http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent': user_agent }

req = request.Request(url, headers=headers)
responce = request.urlopen(req)
data = responce.read().decode('utf-8')

soup = BeautifulSoup(data,'html.parser')
con = soup.find_all('div',class_='content')
for x in con:
    print(x.ssd)
    print('#'*30)

print(soup.div.string)
