#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
#=============================================================================
# FileName:     general_run.py
# Desc:         调用程序
# Author:       leyle
# Email:        leyle@leyle.com
# HomePage:     http://www.leyle.com/
# Git_page:     https://github.com/leyle
# Version:      0.0.1
# LastChange:   2014-12-08 10:15:23
# History:      
#=============================================================================
'''

"""
    调用网易的各个栏目进行内容爬取
"""

from wangyi import  WANGYI

import time

def qingsongyike():
    qsyk = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1350383429665/", list_docid="T1350383429665", item_type="qingsongyike", title_key=["每日轻松一刻"])
    qsyk.run()

def pangbianguaitan():
    pbgt = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1396928667862/", list_docid="T1396928667862", item_type="pangbianguaitan", title_key=["胖编怪谈"])
    pbgt.run()

def huanqiukanke():
    hqkk = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1381482353221/", list_docid="T1381482353221", item_type="huanqiukanke", title_key=["今日环球侃客", "无德无信外国人"])
    hqkk.run()

def wangyizuigengtie():
    wygt = WANGYI(list_url="http://c.m.163.com/nc/article/list/T1411719652285/", list_docid="T1411719652285", item_type="wangyigengtie", title_key=["网易新闻有态度"], key="adTitle")
    wygt.run()

def run_forever():
    while True:
        qingsongyike()
        pangbianguaitan()
        huanqiukanke()
        wangyizuigengtie()

        time.sleep(600)

def test():
    wangyizuigengtie()

if __name__ == "__main__":
    run_forever()
    #test()

