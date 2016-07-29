import urllib
import urllib.request
import re
import os,sys
from bs4 import BeautifulSoup
import time
import random

DESKTOP_USER_AGENTS = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        'Mozilla/5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',

        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    ]
MOBILE_USER_AGENTS = [
        'Mozilla/5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0',
        'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
   
        'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53',
        'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
        ]

def random_user_agent():
    return random.choice([random_desktop_user_agent(), random_mobile_user_agent()])

def random_desktop_user_agent():
    return random.choice(DESKTOP_USER_AGENTS) + str(random.randint(0, 10000))

def random_mobile_user_agent():
    return random.choice(MOBILE_USER_AGENTS) + str(random.randint(0, 10000))


def page(s):#获得页面信息
    Headers = {'User-Agent':random_desktop_user_agent()}
    req=urllib.request.Request(s,data=None,headers=Headers)
    a=urllib.request.urlopen(req)
   
    return a

def dl(name,suf,did,imurl):#下载图片
    Headers = {'User-Agent':random_desktop_user_agent()}
    req=urllib.request.Request(imurl,headers=Headers)
    try:
        info=urllib.request.urlopen(req).read()
    except Exception as error:
        print(error)
        print('本次下载失败')
        pass
    else:
        file=open(did+'\\'+name+'.'+suf,'wb')
        file.write(info)
        file.close()
    
url='http://jandan.net/ooxx/page-1#comments'
gdid='jdan'#总目录名称

while url:
    soup=BeautifulSoup(page(url),'html.parser',from_encoding='utf-8')#创建基本访问对象

    crtpage=soup.find_all('span','current-comment-page')[0].string[:-1][1:]#当前页码
    udid=gdid+'\第'+crtpage+'页'
    os.makedirs(udid)#按页码建立子目录

    nextpage=soup.find_all('a',title='Newer Comments')[0]['href']#下一页链接
    L=soup.find_all('a',string='[查看原图]')#当前页链接list
    
    print('开始下载第'+crtpage+'页。本页共'+str(len(L))+'张')
    s=1#文件名计数

    for i in L:#循环下载本页图片
        k=i['href']
    
        suf=k.split('.')[-1]
        dl(str(s),suf,udid,k)
        print(str(s)+'/'+str(len(L))+'  已完成')
        s=s+1
        time.sleep(1)

    url=nextpage
    
    print('OK')

