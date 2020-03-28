# 字段信息：
#
# code：代码
# name：名称
# industry：所属行业
# area：地区
# pev市盈率
# outstanding：流通股本(亿)
# totals：总股本(亿)
# totalAssets：总资产(万)
# liquidAssets：流动资产
# fixedAssets：固定资产
# reserved：公积金
# reservedPerShare：每股公积金
# esp：每股收益
# bvps：每股净资
# pb：市净率
# timeToMarket：上市日期
# undp：未分利润
# perundp：每股未分配
# rev：收入同比(%)
# profit：利润同比(%)
# gpr：毛利率(%)
# npr：净利润率(%)
# holders：股东人数


import tushare as ts


# data = ts.get_stock_basics()
# # print(data)
#
# # data.to_csv('basic.csv')
# data_600000 = data.ix['600000']
#
# print(data_600000)
#
# data_600000.to_csv('basic_600000.csv')


# df = ts.get_tick_data('600000', date='2020-03-23',src='tt')
#
# print(df)

df = ts.get_realtime_quotes('000581') #Single stock symbol

print(df[['code','name','price','bid','ask','volume','amount','time']])

