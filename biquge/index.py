#--encoding:utf-8--
#第二步 解析目录并将目录章节链接id存入章节编号文件中,便于后面分章下载
import sys
import re
from bs4 import BeautifulSoup


reload(sys)
localChapterHtmlPath=sys.argv[1]
charpterLinkPath=sys.argv[2]

f=open(localChapterHtmlPath,'r')
html=f.read()
f.close()

soupObj=BeautifulSoup(html,'html.parser')
chapterElementParent=soupObj.findAll('a')
charpterLinkPath=charpterLinkPath
charpterLinkObj=open(charpterLinkPath,'a+')
regParten='[0-9]{7}.html'
links=[]
splitParten='.html'

for content in chapterElementParent:
	href=content.get('href')
	if re.search(regParten,href)!=None:
		splitNumber=re.sub(r'.html',"",href)
		charpterLinkObj.write(splitNumber+"\n")	
		continue



links
charpterLinkObj.close()
