#--encoding:utf-8--
#第二步 解析目录并将目录章节链接id存入章节编号文件中,便于后面分章下载
import re
from bs4 import BeautifulSoup

f=open('/tmp/index.html','r')

html=f.read()

f.close()

soupObj=BeautifulSoup(html,'html.parser')
chapterElementParent=soupObj.findAll('a')
charpterLinkPath='/tmp/tuntianwudi.txt'
charpterLinkObj=open(charpterLinkPath,'a+')
regParten='[0-9]{7}.html'
links=[]
splitParten='.html'
for content in chapterElementParent:
	href=content.get('href')
	if re.search(regParten,href)!=None:
		splitNumber=re.sub(r'.html',"",href)
		print(splitNumber)
		charpterLinkObj.write(splitNumber+"\n")	
		continue



links
charpterLinkObj.close()
