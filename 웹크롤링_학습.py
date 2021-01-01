from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
while True:
    nameS = input("알고자 하는 인물의 이름이나 예명을 입력해주세요!\n>>> ")
    nameU = nameS.encode('utf-8')
    nameU = str(nameU)
    nameU = nameU.replace("\\x","%")
    nameU = nameU.replace("'","")
    nameU = nameU.replace("b","",1)
    nameU = nameU.upper()
    html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='+nameU)
    #print(html.text)
    
    soup = bs(html.text,'html.parser')
    data1 = soup.find('dl',{'class':'detail_profile'})
    #print(data1)
    
    print()
    
    data2 = data1.findAll('span')
    #print(data2)
    for i in data2:
        print(i.text)
    
    print()
    
    data3 = data1.findAll('a')
    #print(data3)
    for i in data3:
        print(i.text)
    
    print()
