#coding=utf-8
#今日头条
from lxml import etree
import requests
import urllib2,urllib
import json
import time
import hashlib

def get_url():
    url = 'https://www.toutiao.com/ch/news_hot/'
    global count
    try:
        headers = {
        'Host': 'www.toutiao.com',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
        'Connection': 'Keep-Alive',
        'Content-Type': 'text/plain; Charset=UTF-8',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'cookie':'__tasessionId=u690hhtp21501983729114;cp=59861769FA4FFE1'}
        response = requests.get(url,headers = headers)
        print response.status_code
        html = response.content
        #print html
        tree = etree.HTML(html)
        title = tree.xpath('//a[@class="link title"]/text()')
        source = tree.xpath('//a[@class="lbtn source"]/text()')
        comment = tree.xpath('//a[@class="lbtn comment"]/text()')
        stime = tree.xpath('//span[@class="lbtn"]/text()')
        print len(title)   #0
        print type(title)  #<type 'list'>
        for x,y,z,q in zip(title,source,comment,stime):
            count += 1
            data = {
                'title':x.text,
                'source':y.text,
                'comment':z.text,
                'stime':q.text}
            print count,'|',data

    except urllib2.URLError, e:
        print e.reason

def get_as_cp():
    zz ={}
    now = round(time.time())
    print now  #获取计算机时间
    e = hex(int(now)).upper()[2:]  #hex()转换一个整数对象为十六进制的字符串表示
    print e
    i = hashlib.md5(str(int(now))).hexdigest().upper() #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    if len(e)!=8:
        zz = {'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"}
        return zz
    n=i[:5]
    a=i[-5:]
    r = ""
    s = ""
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz = {
            'as': "A1" + s + e[-3:],
            'cp': e[0:3] + r + "E1"
        }
    print zz

url = 'http://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B5093B4F12B65&cp=59BF52DB0655DE1'
resp = requests.get(url)
print  resp.status_code

Jdata = json.loads(resp.text)
#print Jdata
news = Jdata['data']

for n in news:
    title = n['title']
    source = n['source']
    groupID = n['group_id']
    print title,'|',source,'|',groupID

if __name__ == '__main__':
    count = 0
    get_url()


