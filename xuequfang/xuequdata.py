#coding=utf-8
import urllib2
import re
from bs4 import BeautifulSoup
import sys
import time

middleSchoolAreaDataUrl="http://www.xxjy.gov.cn/Document/Details/2418"
primarySchoolAreaDataUrlList=[
"http://www.xxjy.gov.cn/Document/Details/2509",
"http://www.xxjy.gov.cn/Document/Details/2508",
"http://www.xxjy.gov.cn/Document/Details/2507",
"http://www.xxjy.gov.cn/Document/Details/2506",
"http://www.xxjy.gov.cn/Document/Details/2505",
"http://www.xxjy.gov.cn/Document/Details/2504"
]
import sys
reload(sys) 
sys.