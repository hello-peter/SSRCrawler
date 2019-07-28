#!/usr/bin/python
# encoding: utf-8
import requests 
from bs4 import BeautifulSoup
import bs4
import re                 
print('''
  ______    ______   _______        ______                           __                 
.' ____ \ .' ____ \ |_   __ \     .' ___  |                         [  |                
| (___ \_|| (___ \_|  | |__) |   / .'   \_| _ .--.  ,--.  _   _   __ | | .---.  _ .--.  
 _.____`.  _.____`.   |  __ /    | |       [ `/'`\]`'_\ :[ \ [ \ [  ]| |/ /__\\[ `/'`\] 
| \____) || \____) | _| |  \ \_  \ `.___.'\ | |    // | |,\ \/\ \/ / | || \__., | |     
 \______.' \______.'|____| |___|  `.____ .'[___]   \'-;__/ \__/\__/ [___]'.__.'[___]    
													
																									Author:V1lu0
[+] number=ALL      输出全部的ssr
[+] number>0        你写几个我给你几个
[+] file=write      输出到ssr.txt
[+] file=print      直接打印在屏幕上

Tip:每一次不建议弄很多，但是每爬虫一次都是最新的ssr
''')                                                                       
a=0
b=input("[+]number:")
file=input("[+]file:")
url="http://nulastudio.org/Freedom/"
response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')
ssr = soup.find_all(link=re.compile("ssr"))
#print(type(ssr))
if b=="ALL":
		for x1 in ssr:
			a=a+1
			need =x1.attrs["link"]
			if file=="write":
				with open('ssr.txt','a+') as file_object:
					file_object.write(need+"\n")
			elif file=="print":
				print(x1.attrs["link"])
else:
		for x1 in ssr[0:int(b)]:
			a=a+1
			need =x1.attrs["link"]
			if file=="write":
				with open('ssr.txt','a+') as file_object:
					file_object.write(need+"\n")
			elif file=="print":
				print(x1.attrs["link"])
flag = '%s %d %s!' % ('We can use',a, 'SSRs')
print(flag)