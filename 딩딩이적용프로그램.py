#종합적인 프로젝트

#모듈모음
import time as t
import json
from datetime import datetime
from googletrans import Translator
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import pyowm
#===========


#함수모음
#==
def Print_City_Temp(City_ID):
        obs = owm.weather_at_id(City_ID)  
        
        L = obs.get_location()
        City_name = L.get_name()
        
        W = obs.get_weather()
        Status = W.get_status()
        
        Temp = W.get_temperature(unit='celsius')
        print('----------------------------------------------------------')
        print(City_name + '의 현재 날씨는 '+ Status + '이고 온도는 ' + str(Temp['temp']) + ' 입니다.')
        print('----------------------------------------------------------')
        print()
#==

#==
def format_number(number):
    return '{:,d}'.format(number)


def get_country_data(country):
    country_data_url = "https://corona.lmao.ninja/v3/covid-19/countries/" + country
    res = requests.get(country_data_url).text
    if 'Country not found or doesn' in res:
        print("나라이름을 잘못 작성하셨습니다.")
        print(country, " 는 존재하지 않는 나라이름이거나, 영문으로 작성되지 않았습니다.")
    else:
        country_corona_info = json.loads(res)
        print("[ %s Corona Data ]" % country)
        print("추가 확진자: +%s" % format_number(country_corona_info["todayCases"]))
        print("추가 사망자: +%s" % format_number(country_corona_info["todayDeaths"]))
        print("확진자: %s" % format_number(country_corona_info["cases"]))
        print("사망자: %s" % format_number(country_corona_info["deaths"]))
        print("격리해제: %s" % format_number(country_corona_info["recovered"]))
        print("격리중: %s" % format_number(country_corona_info["active"]))
        return country_corona_info


def get_global_data():
    global_data_url = "https://corona.lmao.ninja/v3/covid-19/all"
    res = requests.get(global_data_url).text
    country_corona_info = json.loads(res)
    print("[ Global Corona Data ]")
    print("확진자: %s" % format_number(country_corona_info["cases"]))
    print("사망자: %s" % format_number(country_corona_info["deaths"]))
    print("격리해제: %s" % format_number(country_corona_info["recovered"]))
    print("(%s 기준)" % datetime.fromtimestamp(country_corona_info["updated"]/1000.0))
    return country_corona_info


def main():
    stringCountry = input("Corona Data 를 출력할 나라를 영문으로 작성해주세요.\n추가 확진자와 추가 사망자는 각 국가가 공유한 정보가 부족할 수 있습니다.\n※주의!※남한은 S. korea, 북한은 데이터가 존재하지 않습니다.\n>>> ")
    print()
    get_country_data(stringCountry)
    print()
#==

#==
#==

#==
#==

#==
#==

#==
#==

#==
#==

#==
#==

#=====================


#=START=
print("안녕하세요!\n이 프로그램은 자율동아리 알고리즘 연구(DingCo)에서 개발한 챗봇의 기능중, 기능대화를 일부 모아둔 프로그램입니다.")
t.sleep(3)
print("흥미로운 시간되세요!")
t.sleep(2)
print("무슨 기능을 이용하시겠습니까?(추후 이 기능은 자연어 처리를 통해 대화형식으로 사용하실 수 있습니다.)")
t.sleep(3)
print("\n[전세계 날씨 알아보기(1)]")
t.sleep(1)
print("[대한민국 현재 날짜와 시간 알아보기(2)]")
t.sleep(1)
print("[현재지역의 미세먼지, 초미세먼지 농도 알아보기(3)]")
t.sleep(1)
print("[각국의 언어들을 번역하기(4)]")
t.sleep(1)
print("[간단한 식이나 사칙연산 계산하기(5)]")
t.sleep(1)
print("[전세계 코로나 확진자 및 특정나라 코로나 확진자 통계자료 알아보기(6)]")
t.sleep(1)
print("[프로그램 종료하기(0)]")
while True:
    t.sleep(2)
    Ans = int(input("사용하고자 하는 기능대화의 번호를 입력해주세요!\n>>> "))
    if Ans == 1: # 날씨
#================================================
        print('날씨 시스템을 시작합니다!')
        t.sleep(1)
        API_Key = '52a192d87186e871d8ad7c1300c3730d'
        owm = pyowm.OWM(API_Key)
        print('----------------------------------------------------------')
        print('0.종료 1.서울 2.도쿄 3.런던 4.뉴욕 5.파리 6.시드니 7.나이로비')
        print('----------------------------------------------------------')
        n = input('날씨를 알고싶은곳의 번호나 지역을 입력해주세요.\n>>> ')
        
        if n == "0" or n == "종료":
                break
        elif n == "1" or n == "서울":
                Print_City_Temp(1835848)
        elif n == "2" or n == "도쿄":
                Print_City_Temp(1850147)
        elif n == "3" or n == "런던":
                Print_City_Temp(2643743)
        elif n == "4" or n == "뉴욕":
                Print_City_Temp(5128581)
        elif n == "5" or n == "파리":
                Print_City_Temp(2988507)
        elif n == "6" or n == "시드니":
                Print_City_Temp(2147714)
        elif n == "7" or n == "나이로비":
                Print_City_Temp(184745)
        else:
                print("다시 입력해주세요.") 
#================================================
    elif Ans == 2: # 날짜와 시간
#================================================
        print('날짜와 시간 시스템을 시작합니다!')
        t.sleep(1)
        now = datetime.now()
        print ("%s년 %s월 %s일 %s시 %s분 %s초입니다." %(now.year, now.month, now.day, now.hour, now.minute, now.second))
#================================================
    elif Ans == 3: # 미세먼지와 초미세먼지
#================================================
        print('미세먼지와 초미세먼지 시스템을 시작합니다!')
        t.sleep(1)
        html = requests.get('https://search.naver.com/search.naver?query=날씨')
        # pprint(html.text)
        soup = bs(html.text,'html.parser')
        data1 = soup.find('div',{'class':'detail_box'})
        #pprint(data1)
        data2 = data1.findAll('dd')
        # pprint(data2)
        fine_dust = data2[0].find('span',{'class':'num'}).text
        ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
        print("대한민국 경상남도 양산시의 미세먼지 지수는",fine_dust,"초미세먼지 지수는",ultra_fine_dust,"입니다.")
#================================================
    elif Ans == 4: # 번역
#================================================
        print('번역 시스템을 시작합니다!')
        t.sleep(1)
        source = input("어떤 언어를 번역하시겠습니까?\n>>> ")
        destion = input("어떤 언어로 번역하시겠습니까?\n>>> ")
        forTranslatorString = input("번역할 내용을 입력해주세요!\n>>> ")

        translator = Translator()
        value = translator.translate(forTranslatorString, src=source, dest=destion)
                 
        #print(value)
        #print(value.src)  # 변환할 언어
        #print(value.dest)  # 변환될 언어
        print(value.text)  # 변환 결과
#================================================
    elif Ans == 5: # 계산기
#================================================
        print('계산기 시스템을 시작합니다!')
        t.sleep(1)
        s = input("값을 입력해 주세요 : ")
        print("결과 : {}".format(eval(s)))
#================================================
    elif Ans == 6: # 코로나 확진자
#================================================
        print('코로나 확진자 시스템을 시작합니다!')
        t.sleep(1)
        get_global_data()
        print()
        if __name__ == '__main__':
            main()
#================================================
    elif Ans == 0: # 종료하기
        print("흥미로운 시간 보내셨나요?")
        t.sleep(1)
        print("프로그램이 5초후 종료합니다!")
        t.sleep(5)
        break
    else:
        print("잘못 입력하셨습니다! 다시 입력해주세요.")
        t.sleep(1)
