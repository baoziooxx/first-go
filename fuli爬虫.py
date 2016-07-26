import urllib
import urllib.request
import re
import os

def page(s):#获得页面信息
    a=urllib.request.urlopen(s)
    return a.read().decode('utf-8')
	
def urls(k):#匹配列表页链接
    a=r'http://www.apic.in/fuli/\d+.htm'
    ra=re.compile(a)
    urllist=re.findall(ra,k)
    return urllist

def imgurls(k):#匹配图片链接
    a=r'src=" (http://.+?\.jp\w?g)'
    ra=re.compile(a)
    urllist=re.findall(ra,k)
    return urllist

def chaurl(url):#转化URL
    a=url.split(':')[1]
    a=urllib.parse.quote(a)
    b=['http:',a]
    return ''.join(b)

def dlimg(a):#按照链接下载图片
    s=1
    os.mkdir('fuli')
    for i in a:
        i=chaurl(i)
        Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req=urllib.request.Request(i,headers=Headers)
        info=urllib.request.urlopen(req).read()
        file=open('fuli\\'+str(s)+'.jpg','wb')
        file.write(info)
        file.close()
        #urllib.request.urlretrieve(req,'%s.jpg'%s)
        print('第'+str(s)+'张下载完成')
        s=s+1

ImgList=[]
m=0#总计数器
pagenum=1

while pagenum<7:
    pagelink='http://www.apic.in/fuli/page/'+str(pagenum)
    DtlLink=list(set(urls(page(pagelink))))#详情页链接list(去重)
    #print(DtlLink)
    i=0
    while i<len(DtlLink):
        Dtl=DtlLink[i]#详情页地址链接
        #print(Dtl)
        Link=imgurls(page(Dtl))#页内图片链接list
        #print(Link)
        ImgList=ImgList+Link#加入总list
        i=i+1
        m=m+1
        print('第'+str(pagenum)+'页共'+str(m)+'个图集已爬完') 
    pagenum=pagenum+1
print(ImgList)
print('共'+str(len(ImgList))+'张')
dlimg(ImgList)
print('都好啦去撸吧！')




