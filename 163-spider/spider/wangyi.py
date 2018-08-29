#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
    列表 url: http://c.m.163.com/nc/article/list/T1396928667862/150-10.html
    胖编怪谈: http://c.m.163.com/nc/article/AC5QK4K400964JJM/full.html
"""
import sys
import simplejson as json
import MySQLdb
import time

sys.path.append("..")

from utils import utils

reload(sys)
sys.setdefaultencoding('utf-8')

class WANGYI(object):
    def __init__(self, list_url, list_docid, item_type, title_key, key="title", start=0, end=10):
        self._start = start
        self._end = end
        self._data = ''
        self._list_url = list_url
        self._list_docid = list_docid
        self._item_type = item_type
        self._title_key = title_key
        self._key = key
        self._docid = []
        self._need_init = True

    def run(self):
        if self._need_init:
            self.init_qsyk()

        self.download_and_insert()

    def clean_all(self):
        """ 目的是清理掉全局变量的值，方便循环调用 """
        self._data = ''
        self._docid = []


    def get_docid_from_json(self):
        """ 根据指定的起始、结束区间，提取这个区间的每日轻松一刻的 url 关键元素 """
        url = self._list_url + str(self._start) + "-" + str(self._end) + ".html"
        self._data = utils.download_page(url)
        if self._data:
            self._data = json.loads(self._data)
            if self._data.has_key(self._list_docid):
                self._data = self._data[self._list_docid]
                self.extract_docid()

    def extract_docid(self):
        if self._data:
            for d in self._data:
                for title in self._title_key:
                    if str(d.get(self._key, 1)).find(title) != -1:
                        tmp = {}
                        tmp["docid"] = d['docid']
                        tmp["cover_img"] = d['imgsrc'] if d.has_key('imgsrc') else ''

                        self._docid.append(tmp)

    def download_and_insert(self):
        if not self._docid:
            self.get_docid_from_json()

        if self._docid:
            for docid in self._docid:
                self.get_qsyk_and_insert(docid)

        self.clean_all()

    def get_qsyk_and_insert(self, docid):
        cover_img = MySQLdb.escape_string(docid['cover_img'])
        docid = docid['docid']

        if self.db_has_exist(docid):
            return

        url = "http://c.3g.163.com/nc/article/%s/full.html" % str(docid)
        data = utils.download_page(url, True)

        if data:
            data = data[docid]
            if data:
                ptime = data['ptime']
                today = ptime.split(' ')[0]
                imgs = data['img']
                body = data['body'].encode('utf-8')

                title = data['title'].replace(' ', '').replace('（', '-').replace('(', '-').replace(')', '').replace('）', '')

                for img in imgs:
                    body = body.replace(img['ref'], "<img src=\"" + img['src'] + "\"/><hr>")

                body = body.replace('%', '%%')
                body = MySQLdb.escape_string(body)
                sql = "insert into wangyi(item_type, title, url, docid, cover_img, ptime, today, body) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self._item_type, title, url, docid, cover_img, ptime, today, body)
                utils.insert_mysql(sql)

    def db_has_exist(self, docid):
        sql = "select * from wangyi where docid='%s' and item_type='%s'" % (str(docid), self._item_type)
        if utils.query_mysql(sql):
            return True
        else:
            return False

    def init_qsyk(self):
        """ 检查 run_control 表中 total 数据是否是0，如果不是，就运行程序，直到满足了 total 为止，并将 total 置为 0 """
        if self._need_init:
            sql = "select total, one_page from run_control where item='%s'" % (self._item_type)
            ret = utils.query_mysql(sql)

            total = 0
            one_page = 0
            if ret:
                total = int(ret[0]['total'])
                one_page = int(ret[0]['one_page'])

            if total > 0:
                for i in range(0, total, one_page):
                    self._start = i
                    self.download_and_insert()

                sql = "update run_control set total=0 where item='%s'" % (self._item_type)
                utils.update_mysql(sql)

            self._need_init = False

def test():
    #def __init__(self, list_url, list_docid, item_type, title_key, start=0, end=10):
    #qsyk = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1396928667862/", list_docid="T1396928667862", item_type="pangbianguaitan", title_key=["胖编怪谈"])
    #qsyk = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1350383429665/", list_docid="T1350383429665", item_type="qingsongyike", title_key=["每日轻松一刻"])
    qsyk = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1381482353221/", list_docid="T1381482353221", item_type="huanqiukanke", title_key=["今日环球侃客", "无德无信外国人"])
    qsyk.run()

if __name__ == "__main__":
    test()

