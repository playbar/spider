#-*-coding:utf8-*-
# from lxml import etree
from multiprocessing.dummy import Pool
import requests
import re
import sys
# from spider import spider

reload(sys)
sys.setdefaultencoding("utf-8")


def modifyConstant():
    global COOKIES
    return


def spider(url):
    html = requests.get(url, cookies=COOKIES).content
    return html


def weiboIdSpider(html):
    f = open('weiboIdList.txt', 'w')
    content = re.findall(r'<td valign="top">(.*?)</a>', html, re.S)
    for each in content:
        # print each
        url = re.search(r'<a href="(.*?)">', each, re.S).group(1)
        # print url
        f.writelines(weiboIdToUrl(url))
        f.writelines('\n')
    f.close()


def weiboIdToUrl(url):
    html = spider(url)
    return re.search(r'私信</a>&nbsp;\<a href="/(.*?)/info"\>资料</a>', html, re.S).group(1)


def weiboInfoSpider(html):
    f = open('weiboInfo.txt', 'w')
    # print html
    nicheng = re.search(r'>昵称:(.*?)<br/>', html, re.S).group(1)
    print u'昵称：' + nicheng
    f.writelines(u'昵称：' + nicheng + '\n')
    daren = re.search(r'达人:(.*?)<br/>', html, re.S).group(1)
    print u'达人：' + daren
    f.writelines(u'达人：' + daren + '\n')
    xingbie = re.search(r'性别:(.*?)<br/>', html, re.S).group(1)
    print u'性别：' + xingbie
    f.writelines(u'性别：' + xingbie + '\n')
    diqu = re.search(r'<br/>地区:(.*?)<br/>', html, re.S).group(1)
    print u'地区：' + diqu
    f.writelines(u'地区：' + diqu + '\n')


def zhihuIdSpider(html):
    f = open('zhihuIdList.txt', 'w')
    content = re.findall(r'<a data-tip="(.*?)class=', html, re.S)
    for each in content:
        # print each
        url = re.search(r'people/(.*?)"', each, re.S).group(1)
        print url
        f.writelines(url)
        f.writelines('\n')
    f.close()

if __name__ == '__main__':
    modifyConstant()

    weiboCookies = {"Cookie": " _T_WM=6ca0e0cdc0cd1879c6c1801f98a9d6c5; " +
                    "SUB=_2A257Fm3YDeTxGeNJ6lUZ8CfKwziIHXVY-XOQr" +
                    "DV6PUJbrdANLULTkW14RMt5DmgJHhr-ZbD--rpg09JQCA..;" +
                    "gsid_CTandWM=4uvUc7a31IyJbium8aRERnZsJb2; " +
                    "M_WEIBOCN_PARAMS=luicode%3D20000174"}
    weiboURL = 'http://weibo.cn/5717809684/'

    # COOKIES = weiboCookies
    # url = weiboURL
    # weiboIdSpider(spider(url + 'follow'))

    zhihuCookies = {"Cookie": "_ga=GA1.2.200227533.1448713358; " +
                    "q_c1=3c8a6952ff6b451186e548a78e07e5f3|1448717055000|1448717055000; " +
                    "_za=c4856f7e-2b10-4c6f-ac1c-7120243828b1; _xsrf=53de1f0fc43b2118b48cfe714e889872; __utmt=1; " +
                    'cap_id="NmJkYTc0OWUzZTQ4NGQyY2E3MjQ2ZmI0NWU0Mzk1MzM=|1448868103|a22b3ff3843b0e08bf078ff3cabd69c590ffe399"; ' +
                    "__utma=51854390.200227533.1448713358.1448868015.1448868015.1; " +
                    "__utmb=51854390.16.9.1448868181265; __utmc=51854390;" +
                    "__utmz=51854390.1448868015.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; " +
                    "__utmv=51854390.000--|2=registration_date=20130912=1^3=entry_date=20151128=1; "
                    'z_c0="QUFBQXZRc2VBQUFYQUFBQVlRSlZUWGVHZzFhbTcyREhCeDYwdWRFRUx2RlZvemFOWm14ck9BPT0=|1448868215|cce7afe611ff3806d63d8d8b943b36af4c40302d"; ' +
                    'unlock_ticket="QUFBQXZRc2VBQUFYQUFBQVlRSlZUWDhBWEZiRXBVVTZxdFA0bTluOEVHMWFIY3pNU2dvWWVBPT0=|1448868215|f0ede700d045c55277c0f34f20a00f332f6be485"'}
    zhihuURL = 'http://www.zhihu.com/people/xie-ke-41/followees'

    # url = zhihuURL
    # COOKIES = zhihuCookies
    # zhihuIdSpider(spider(url))

    COOKIES = weiboCookies
    url = 'http://weibo.cn/2807748433/info'
    weiboInfoSpider(spider(url))
