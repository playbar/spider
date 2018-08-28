# -*-coding:utf8-*-
from lxml import etree
import requests
import re
import sys
import weibo_cookie
import random
import time

reload(sys)
sys.setdefaultencoding("utf-8")


# URL to HTML
def spider(url):
    rand = random.randint(0, 99)
    # print rand % 3
    html = requests.get(url, cookies=weibo_cookie.weiboCookies[2]).content
    return html


# count the pages, return a page list
def findpage(url):
    pages = [url]

    html = spider(url)
    selector = etree.HTML(html)

    try:
        total_page = int(re.search(u'/(.*?)页', selector.xpath
        ('//*[@id="pagelist"]/form/div/text()')[1]).group(1))
    except IndexError:
        print 'IndexError'
        return pages

    print 'total_page = ' + str(total_page)

    for i in range(2, total_page + 1):
        newpage = url + '?page=' + str(i)
        pages.append(newpage)
    print pages
    return pages


# find this page id, write to 'weiboIdList.txt'
def weiboIdSpider(pages):
    for page in pages:
        print page
        html = spider(page)
        content = re.findall(r'<td valign="top">(.*?)</a>', html, re.S)
        # print len(content)
        for each in content:
            # print each
            url = re.search(r'<a href="(.*?)">', each, re.S).group(1)
            # print url
            if weiboURLtoID(url) != 'self':
                f = open('weiboIdList.txt', 'a+')
                former = []
                for line in f:
                    former.append(line.strip())
                try:
                    if weiboURLtoID(url) not in former:
                        print weiboURLtoID(url)
                        f.writelines(weiboURLtoID(url))
                        f.writelines('\n')
                    else:
                        print weiboURLtoID(url),'已经存在'
                except TypeError:
                    print 'TypeError'
                    pass

                f.close()

        timerand = random.randint(20, 25)
        # timerand = 10
        # print 'sleep time '+str(timerand)+'s'
        time.sleep(int(timerand))


# weiboURL to weiboID
def weiboURLtoID(url):
    html = spider(url)
    try:
        id = re.search(r'私信</a>&nbsp;\<a href="/(.*?)/info"\>资料</a>', html, re.S).group(1)
        # print id
    except AttributeError:
        print 'AttributeError'
        return
    return id


# main function
# in : id
# out: write to file
def weiboIdList(id):
    print 'ID = ' + id + ' follow'
    weiboURL = 'http://weibo.cn/' + id + '/'

    url = weiboURL + 'follow'
    # print spider(url)
    pages = findpage(url)
    weiboIdSpider(pages)


if __name__ == '__main__':
    id = '5658759079'
