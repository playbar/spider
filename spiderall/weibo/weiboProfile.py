# -*-coding:utf8-*-
import sys
import weibo
import random
import time
import re
from lxml import etree

reload(sys)
sys.setdefaultencoding("utf-8")


def weiboProfile(id,pages):
    filename = './profile/' + id + '.txt'
    f = open(filename, 'w')
    for page in pages:
        print page
        html = weibo.spider(page)
        selector = etree.HTML(html)
        content = selector.xpath('//span[@class="ctt"]')
        for each in content:
            text = each.xpath('string(.)')
            # print text
            f.writelines(text)
            f.writelines('\n')
        timerand = random.randint(10, 25)
        # print 'sleep time '+str(timerand)+'s'
        time.sleep(int(timerand))
    f.close()


def weiboProfileSpider(id):
    print u'ID：' + id
    url = 'http://weibo.cn/' + id + '/profile'
    pages = weibo.findpage(url)
    weiboProfile(id,pages)


if __name__ == '__main__':
    f = open('weiboIdList.txt', 'r')
    for line in f:
        weiboid = line.strip()
        weiboProfileSpider(weiboid)
    f.close()

    # id = '3191294591'
    # weiboProfileSpider(id)