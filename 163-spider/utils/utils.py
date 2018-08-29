#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
#=============================================================================
# FileName:     utils.py
# Desc:         通用程序库
# Author:       leyle
# Email:        leyle@leyle.com
# HomePage:     http://www.leyle.com/
# Git_page:     https://github.com/leyle
# Version:      0.0.1
# LastChange:   2014-12-08 10:12:51
# History:      
#=============================================================================
'''

"""
    通用程序
"""
import torndb
import _mysql_exceptions
import sys
import requests

from mylogger import get_logger

ulog = get_logger("utils")
applog = get_logger("app")

reload(sys)
sys.setdefaultencoding('utf-8')

db = torndb.Connection(host="localhost", database="WANGYI", user="user", password="passwd")

# 数据库执行
def insert_mysql(sql):
    try:
        db.insert(sql)
        return True

    except _mysql_exceptions.IntegrityError, e:
        """ 主键冲突，此处不算错误 """
        ulog.info("主键冲突: %s" % e)
        return True

    except Exception as e:
        ulog.info("其他数据库错误: %s | %s" % (sql, e))
        return False

def update_mysql(sql):
    try:
        db.update(sql)
        return True

    except Exception as e:
        ulog.info("update 时，其他错误: %s | %s" % (sql, e))
        return False

# 数据库查询
def query_mysql(sql):
    ret = []
    try:
        ret = db.query(sql)

    except Exception as e:
        ulog.info("查询数据库错误: %s | %s" % (sql, e))

    finally:
        return ret

# 执行 requests 的数据下载
def download_page(url, ret_json=False):
    if not url:
        applog.info("url 不合法: %s" % url)
        return ''

    try:
        applog.info("当前下载的 url: %s " % url)
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            if ret_json:
                return r.json()
            return r.content
        else:
            applog.info("下载失败，status_code: %s" % r.status_code)
            return ''

    except Exception as e:
        applog.info("下载失败, %s %s" % (url, e))
        return ''

def test():
    pass

if __name__ == "__main__":
    test()

