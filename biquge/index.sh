#!/bin/sh
#第一步 抓取目录页的html
#目录页面本地存储文件路径定义
chapterHtmlLocalPath='/tmp/index.html'
#目录页面网页地址定义
chapterHtmlWebUrl='https://www.biquge.cc/html/166/166596/'
#目录链接参数本地存储文件
chapterParamsLocalFile='/tmp/tuntianwudi.txt'
#初始化分章数据存储目录
chapterListLocalDir='/tmp/tuntianwudi/'
#初始化最终写入文件
novelFile='/tmp/tutianwudi_end.txt'

#抓取目录数据
echo "开始抓取目录信息"
/usr/bin/wget -O $chapterHtmlLocalPath $chapterHtmlWebUrl -q -nc >> /dev/null
if [ ! -f $chapterHtmlLocalPath ]; then
	echo '目录页面抓取失败'
	exit 0
fi
echo "目录信息抓取完毕:"$chapterHtmlLocalPath

echo "开始保存目录链接参数"
#读取目录链接信息并存入txt文件

/usr/bin/python ./index.py $chapterHtmlLocalPath $chapterParamsLocalFile

if [ ! -f $chapterParamsLocalFile ]; then
	echo "目录链接参数保存失败"
	exit 0
fi
echo "目录链接参数保存成功:"$chapterParamsLocalFile


echo "开始分章抓取小说"
if [ ! -d $chapterListLocalDir ]; then
	mkdir $chapterListLocalDir
	chmod 777 $chapterListLocalDir
	echo "创建目录："$chapterListLocalDir
fi

cat $chapterParamsLocalFile|while read line
do
{
	/usr/bin/wget $chapterHtmlWebUrl$line".html" -O $chapterListLocalDir$line -q -nc >> /dev/null
}
done

echo "分章抓取完毕"

echo "开始写入小说文件"
/usr/bin/python ./readHtml.py $chapterParamsLocalFile $chapterListLocalDir $novelFile
echo "小说写入文件完毕:"$novelFile
