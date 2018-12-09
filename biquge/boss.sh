#!/bin/sh
#第四步 分章读取总控 开启多进程 提高抓取速度
startPage=8498085
endPage=8962433

for ((i=$startPage;i<=$endPage;i=i+10000));
do
	/usr/bin/nohup /bin/sh /root/data/sh/catch.sh $i&
done
wait
