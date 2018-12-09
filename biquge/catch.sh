#!/bin/sh
#分章读取子进程
startPage=$1
endPage=$startPage+10000
baseUrl="https://www.biquge.cc/html/166/166596/"

#获取链接的方法

getUrl(){
	pageNum=$1
	echo $pageNum
	currentUrlFormated=$baseUrl$pageNum".html"
}
getUrlContent(){
	/usr/bin/wget $currentUrlFormated -O /tmp/tuntianwudi/$pageNum -nc
}

for ((i=$startPage;i<=$endPage;i++));
do
	grep $i /tmp/tuntianwudi.txt

	if [ $? -eq 0 ]; then
        	echo 'found'
	else
        	echo 'not found'
		continue
	fi
	currentUrl=($i)
	getUrl $currentUrl
	echo $currentUrlFormated
	getUrlContent
done
