import urllib
import urllib.request
import re
import os
from bs4 import BeautifulSoup
import time

def page(s):#获得页面信息
    #Headers = {
    #    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    Headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    req=urllib.request.Request(s,data=None,headers=Headers)
    #print(req,'请求组装完毕')
    a=urllib.request.urlopen(req)
    #print(a,'发送请求完毕')
    return a.read()#.decode()

def ww(s):#将页面bytes写入文件
    f=open('url.html','wb')
    f.write(s)
    f.close()

def dl(name,did,imurl):#下载图片
    Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req=urllib.request.Request(imurl,headers=Headers)
    try:
        info=urllib.request.urlopen(req).read()
    except:
        print(Exception)
        print('下载出错')
        pass
    else:
        file=open(did+'\\'+name+'.jpg','wb')
        file.write(info)
        file.close()

def getalbumurl(u):#获取本列表页所有合集地址。参数u为列表页地址.tag
    ww(page(u))#写本地缓存
    soup=BeautifulSoup(open('url.html'),'html.parser')
    div=BeautifulSoup(str(soup.find_all('div','mode_box')[0]),'html.parser')
    i=0
    urllist=[]
    while i<len(div.find_all('dt')):
        url=div.find_all('dt')[i].a['href']
        urllist.append(url)
        i=i+1
    os.remove('url.html')#清除缓存
    return urllist

def getccalbumurl(u):#获取本列表页所有合集地址。参数u为列表页地址.cc
    ww(page(u))#写本地缓存
    soup=BeautifulSoup(open('url.html'),'html.parser')
    div=BeautifulSoup(str(soup.find_all('div','lb_box')[0]),'html.parser')
    i=0
    urllist=[]
    while i<len(div.find_all('dt')):
        url=div.find_all('dt')[i].a['href']
        urllist.append(url)
        i=i+1
    os.remove('url.html')#清除缓存
    return urllist

def getpagenum(u):#获取当前页码
    ww(page(u))#写本地缓存
    soup=BeautifulSoup(open('url.html'),'html.parser')
    div=BeautifulSoup(str(soup.find_all('div','flym')[0]),'html.parser')
    pagen=int(div.span.string)
    os.remove('url.html')
    return pagen#当前页码
    
def getnextpage(u):#获取下一列表页地址
    ww(page(u))#写本地缓存
    soup=BeautifulSoup(open('url.html'),'html.parser')
    div=BeautifulSoup(str(soup.find_all('div','flym')[0]),'html.parser')
    pagen=int(div.span.string)#当前页码
    try:
        nexturl='http://pic.yesky.com'+div.find_all('a',string=str(pagen+1))[0]['href']
    except:
        print('最后一页已经跑完了')
    else:
        pass
        return nexturl
    finally:
        os.remove('url.html')#清除缓存
     
    
def dlalbum(url,ddid,did):#下载一个图片合集
    ImgList=[]
    i=1
    os.makedirs(ddid+'/'+did)
    pagenum=1
    while len(ImgList)<pagenum:
        a=page(url)#调用page，读取本页内信息
        ww(a)#调用ww，写本地缓存文件
        soup=BeautifulSoup(open('url.html'),'html.parser')
        
        pagenum=BeautifulSoup(str(soup.find_all('li','bottom_show')[0]),'html.parser').span.string.split('/')[1]
        pagenum=int(pagenum)#本合集图片数量
        #print(pagenum)

        div=BeautifulSoup(str(soup.find_all('div',class_='l_effect_img_mid')[0]),'html.parser')
        nexturl=div.a['href']#获取下一页地址
        imgurl=div.img['src']#获取本页图片链接
        #print(imgurl)

        os.remove('url.html')#清除缓存
        ImgList.append(imgurl)
        url=nexturl

        #time.sleep(1)
        #print('3')
        #time.sleep(1)
        #print('2')
        #time.sleep(1)
        #print('1')#倒计时

        name=str(i)
        dl(name,ddid+'/'+did,imgurl)#调用dl，下载本页图片
        print('第'+str(i)+'张下载完成')
        i=i+1
        #print('OK')

ww(page('http://pic.yesky.com/tag/'))
soup=BeautifulSoup(open('url.html'),'lxml')

ff=re.compile('http://pic.yesky.com/tag/'+r'.+')
cc=re.compile('http://pic.yesky.com/c/'+r'.+')

fzong=soup.find_all('a',href=ff)
tags=[i.string for i in fzong]

czong=soup.find_all('a',href=cc)
ccs=[i.string for i in czong]
os.remove('url.html')
print('标签列表如下：\n')
print(tags)
print('\n')
print('分类列表如下：\n')
print(ccs)
print('\n\n')


kik=input('来来来，挑一个标签名称,输入后，猛击回车：')
mulu=input('现在，给文件夹起一个名字，确认好后，猛击回车：')
startpage=input('从第几页开始？（输入一个数字，建议为1，猛击回车）')
url='http://pic.yesky.com/tag/meinv/'+startpage+'/'+urllib.parse.quote(kik)+'/'
p=getpagenum(url)

while p:
    try:
        L=getalbumurl(url)
        p=getpagenum(url)
    except:
        print(Exception)
        break
    else:
        print('当前页码:'+str(p))
        s=1
        for i in L:
            dlalbum(i,mulu,'第'+str(p)+'页第'+str(s)+'个合集')
            s=s+1
            
        url=getnextpage(url)

print('OK,拿去撸')
time.sleep(10)
