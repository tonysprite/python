#-*-coding:utf-8-*- #
#第五步 将抓取的章节html内容逐章写入txt
import os
import re
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
destinationFile=sys.argv[3]
htmlDir=sys.argv[2]
chapterFile=sys.argv[1]
f=open(chapterFile)
#存入文件
def readHtml(waitingReadFileName):
	htmlFileObj=open(waitingReadFileName)	
	html=htmlFileObj.read()
	htmlObj=BeautifulSoup(html,'html.parser')
	contentElement=htmlObj.findAll(id='content',limit=1)
        titleElement=htmlObj.findAll('h1',limit=1)
	if titleElement:
                destinationObj=open(destinationFile,'a+')
                destinationObj.write(titleElement[0].text)
                destinationObj.close()
	
        if contentElement:
                destinationObj=open(destinationFile,'a+')
                destinationObj.write(contentElement[0].text)
                destinationObj.close()


	htmlFileObj.close()


	
while 1:
	line=f.readline()
	if not line:
		break;
	else:
		formatedLine=re.sub(r'\n',"",line)
		waitingReadFileName=htmlDir+formatedLine
		if os.access(waitingReadFileName,os.F_OK):
			readHtml(waitingReadFileName)

f.close()

exit()
