#-*-coding:utf-8-*- #编码声明，不要忘记！
import ssl
import urllib2
import re
from bs4 import BeautifulSoup
import sys
import time
#开始抓取的url
novelUrl="http://m.xiaoshuoli.com/i36480/18734036.html"
#小说保存的文件
savePath="/tmp/minqinitaihuai.txt"
def writeNovel(url):
    print("\n cureent url=="+url)
    print("开始抓取")
    reload(sys)
    sys.setdefaultencoding('utf-8')

    
    req = urllib2.Request(url)
    req.add_header('Referer',url)
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
    #req.add_header('Accept-Encoding','gzip, deflate, br')
    req.add_header('Accept-Language','zh-CN,zh;q=0.9')
    req.add_header('Cache-Control','max-age=0')
    req.add_header('Connection','keep-alive')
    req.add_header('Host','m.xiaoshuoli.com')
    req.add_header('Upgrade-Insecure-Requests',1)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    req.add_header('Cookie','fikker-Ax9H-iKQM=EMad7ImruDGT5rNRKHETi05fQbAtmxAN; fikker-Ax9H-iKQM=EMad7ImruDGT5rNRKHETi05fQbAtmxAN; Hm_lvt_5eb81c3b57ea700d51556a83f9cebcfe=1527657804,1527751971,1528348622; Hm_lpvt_5eb81c3b57ea700d51556a83f9cebcfe=1528348697')
    obj = urllib2.urlopen(req)
    html=obj.read()

    httpCode=obj.getcode()
    if httpCode!=200:
        print("服务器响应错误，httpCode=="+httpCode)
        return


    soupObj = BeautifulSoup(html, 'html.parser')
    ulList=soupObj.findAll(id='chaptercontent')
    urlArr=soupObj.findAll(id='pt_prev')
    if urlArr:
        #存在上一章节按钮的是本章首页
        paragrahTitleArr=soupObj.findAll('title')
        paragrahTitleTextFullArr=paragrahTitleArr[0].text.split('_')
        paragrahTitle=paragrahTitleTextFullArr[0];
    else:        
        paragrahTitle="" 
    
    pageNextArr=soupObj.findAll(id='pb_next',limit=1)#默认取下一分页
    if pageNextArr:
        nextPageUrl=pageNextArr[0].get('href')
    else:        
        pageNextArr=soupObj.findAll(id='pt_next',limit=1)#不存在下一页则获取下一章节的页面地址
        nextPageUrl=pageNextArr[0].get('href')


    if  pageNextArr:
        print("存在下一页地址")
    else:
        return 0#没有下一页了结束抓取
        
    nextPageUrl="https://m.xiaoshuoli.com"+nextPageUrl#组装下一页全域名地址
    
    fobj=open(savePath,'a+')
    fobj.write("\n\n"+paragrahTitle)#文件写入标题
    fobj.write("\n"+ulList[0].text)#写入内容
    fobj.close()
    print("抓取成功")
    if nextPageUrl:#存在下一页则递归抓取
        return writeNovel(nextPageUrl)
    else:#不存在下一页则结束抓取
        print("没有下一页了")
        return 0



writeNovel(novelUrl)
print("\n上传完毕")
