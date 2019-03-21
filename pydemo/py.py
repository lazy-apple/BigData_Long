
#coding:utf8

import urllib.request as urllib2
#json解析库,对应到lxml
import json
#json的解析语法，对应到xpath
import jsonpath

url="http://www.lagou.com/lbs/getAllCitySearchLabels.json"
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}

request=urllib2.Request(url,headers=header)

response=urllib2.urlopen(request)
#取出json文件里的内容，返回的格式是字符串
html=response.read()

#把json形式的字符串转换成python形式的Unicode字符串
unicodestr=json.loads(html)
f = open(r"E:\IDEA_workspace\BigData_Long\pydemo\file\old.txt",'a',encoding='utf-8')#a:追加
str1 = str(unicodestr)
f.write(str1)
f.closed

f = open(r"E:\IDEA_workspace\BigData_Long\pydemo\file\data.txt",'a',encoding='utf-8')#a:追加
li = [chr(i) for i in range(ord("A"),ord("Z")+1)]
for i in li:
    sti = "$.."+i
    city_list1=jsonpath.jsonpath(unicodestr,sti)
    st = str(city_list1)[3:-3].split('}, {')
    for j in st :
        print(j)
        f.write(j)
        f.write("\n")
f.closed