# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/11/7 14:06
contact: jindaxiang@163.com
desc: 不需要控制速度, 但是需要伪装游览器, 不然会在第一次请求就被封 IP, 目前采用银保监会采用两套反扒方案
1. 20191114在周内运行
2. 20191115在周末运行
3. 已实现自动切换
"""
import requests
import pandas as pd
import execjs
from bs4 import BeautifulSoup

from akshare.bank.cons import cbirc_headers_without_cookie_2019


def bank_page_list(page=5):
    """
    想要获取多少页的内容
    http://www.cbirc.gov.cn/cn/list/9103/910305/ybjfjcf/1.html
    :param page: int 输入从第 1 页到 all_page 页的内容
    :return: pd.DataFrame 另存为 csv 文件
    """
    big_url_list = []
    big_title_list = []
    flag = True
    cbirc_headers = cbirc_headers_without_cookie_2019.copy()
    for i_page in range(1, page):
        # i_page = 1
        print(i_page)
        main_url = "http://www.cbirc.gov.cn/cn/list/9103/910305/ybjfjcf/{}.html".format(
            i_page
        )
        if flag:
            res = requests.get(main_url, headers=cbirc_headers)
            temp_cookie = res.headers["Set-Cookie"].split(";")[0]
            cbirc_headers.update({"Cookie": res.headers["Set-Cookie"].split(";")[0]})
            res = requests.get(main_url, headers=cbirc_headers)
            soup = BeautifulSoup(res.text, "lxml")
            res_html = (
                "function getClearance(){"
                + soup.find_all("script")[0].get_text()
                + "};"
            )
            res_html = res_html.replace("</script>", "")
            res_html = res_html.replace("eval", "return")
            res_html = res_html.replace("<script>", "")
            ctx = execjs.compile(res_html)
            if "firstChild.cookie" in ctx.call("getClearance"):
                over_js = (
                    "function getClearance2(){var a"
                    + ctx.call("getClearance")
                    .split("firstChild.cookie")[1]
                    .split("Path=/;'")[0]
                    + "Path=/;';return a;};"
                )
            if "document.cookie" in ctx.call("getClearance"):
                over_js = (
                    "function getClearance2(){var a"
                    + ctx.call("getClearance")
                    .split("document.cookie")[1]
                    .split("Path=/;'")[0]
                    + "Path=/;';return a;};"
                )
            over_js = over_js.replace("window.headless", "''")
            over_js = over_js.replace("window['_p'+'hantom']", "''")
            over_js = over_js.replace("window['__p'+'hantom'+'as']", "''")
            over_js = over_js.replace("window['callP'+'hantom']", "''")
            over_js = over_js.replace("return(", "eval(")
            ctx = execjs.compile(over_js)
            cookie_2 = ctx.call("getClearance2").split(";")[0]
            cbirc_headers.update({"Cookie": temp_cookie + ";" + cookie_2})
            res = requests.get(main_url, headers=cbirc_headers)
            soup = BeautifulSoup(res.text, "lxml")
            url_list = [
                item.find("a")["href"]
                for item in soup.find_all(attrs={"class": "zwbg-2"})
            ]
            title_list = [
                item.find("a").get_text()
                for item in soup.find_all(attrs={"class": "zwbg-2"})
            ]
            big_url_list.extend(url_list)
            big_title_list.extend(title_list)
            flag = 0
        else:
            res = requests.get(main_url, headers=cbirc_headers)
            soup = BeautifulSoup(res.text, "lxml")
            url_list = [
                item.find("a")["href"]
                for item in soup.find_all(attrs={"class": "zwbg-2"})
            ]
            title_list = [
                item.find("a").get_text()
                for item in soup.find_all(attrs={"class": "zwbg-2"})
            ]
            big_url_list.extend(url_list)
            big_title_list.extend(title_list)
    temp_df = pd.DataFrame([big_title_list, big_url_list]).T
    return temp_df, cbirc_headers


def bank_fjcf(page=3):
    """
    获取每个具体页面的表格内容
    :return: pandas.DataFrame 另存为 csv 文件
    """
    big_df = pd.DataFrame()
    temp_df, cbirc_headers = bank_page_list(page)
    for i in range(len(temp_df)):
        # i = 1
        print(i)
        try:
            res = requests.get(
                "http://www.cbirc.gov.cn" + temp_df.iloc[:, 1][i], headers=cbirc_headers
            )
            table_list = pd.read_html(res.text)
            table_df = table_list[6].iloc[:, 3:]
            table_df.columns = ["内容"]
            big_df = big_df.append(table_df.T)
        except:
            print(i, "是文档")
            continue
    big_df.reset_index(drop=True, inplace=True)
    big_df.columns = [
        "行政处罚决定书文号",
        "姓名",
        "单位",
        "主要负责人姓名",
        "主要违法违规事实（案由）",
        "行政处罚依据",
        "行政处罚决定",
        "作出处罚决定的机关名称",
        "作出处罚决定的日期",
    ]
    return big_df


if __name__ == "__main__":
    df = bank_fjcf(page=3)
    print(df)
