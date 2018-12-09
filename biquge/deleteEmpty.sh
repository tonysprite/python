#!/bin/sh
#第四步完成后监测是否有抓取异常的html 进行剔除
dir='/tmp/tuntianwudi/'
cd $dir
for size in `ls`
do
 if [ `ls -l $size|gawk '{print $5}'` == 0 ]; then
	`rm $size`
 fi

done
