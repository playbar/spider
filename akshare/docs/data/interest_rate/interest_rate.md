## [AkShare](https://github.com/jindaxiang/akshare) 利率数据

### 主要央行利率

#### 美联储利率决议报告

接口: macro_bank_usa_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_usa_interest_rate_decision

描述: 获取美联储利率决议报告, 数据区间从19820927-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_usa_interest_rate_se = ak.macro_bank_usa_interest_rate()
print(macro_bank_usa_interest_rate_se)
print(macro_bank_usa_interest_rate_se.name)
```

数据示例

macro_bank_usa_interest_rate_se.name

```usa_interest_rate```

macro_bank_usa_interest_rate_se: pandas.Series

```
1982-09-27    10.25
1982-10-01       10
1982-10-07      9.5
1982-11-19        9
1982-12-14      8.5
              ...
2019-06-20      2.5
2019-08-01     2.25
2019-09-19        2
2019-10-31        0
2019-12-12        0
```

#### 欧洲央行决议报告

接口: macro_bank_euro_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_interest_rate_decision

描述: 获取欧洲央行决议报告, 数据区间从19990101-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_euro_interest_rate_se = ak.macro_bank_euro_interest_rate()
print(macro_bank_euro_interest_rate_se)
print(macro_bank_euro_interest_rate_se.name)
```

数据示例

macro_bank_euro_interest_rate_se.name

```euro_interest_rate```

macro_bank_euro_interest_rate_se: pandas.Series

```
1999-01-01      3
1999-02-01      3
1999-03-01      3
1999-04-01      3
1999-05-01    2.5
             ... 
2019-07-25      0
2019-09-12      0
2019-10-24      0
2019-12-12      0
2020-01-23      0
```

#### 新西兰联储决议报告

接口: macro_bank_newzealand_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_newzealand_interest_rate_decision

描述: 新西兰联储决议报告, 数据区间从19990401-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_newzealand_interest_rate_se = ak.macro_bank_newzealand_interest_rate()
print(macro_bank_newzealand_interest_rate_se)
print(macro_bank_newzealand_interest_rate_se.name)
```

数据示例

macro_bank_newzealand_interest_rate_se.name

```newzealand_interest_rate```

macro_bank_newzealand_interest_rate_se: pandas.Series

```
1999-04-01    4.5
1999-05-01    4.5
1999-06-01    4.5
1999-07-01    4.5
1999-08-01    4.5
             ... 
2019-06-26    1.5
2019-08-07      1
2019-09-25      1
2019-11-13      1
2020-02-12      0
```

#### 中国人民银行利率报告

接口: macro_bank_china_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_china_interest_rate_decision

描述: 中国人民银行利率报告, 数据区间从19910501-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_china_interest_rate_se = ak.macro_bank_china_interest_rate()
print(macro_bank_china_interest_rate_se)
print(macro_bank_china_interest_rate_se.name)
```

数据示例

macro_bank_china_interest_rate_se.name

```china_interest_rate```

macro_bank_china_interest_rate_se: pandas.Series

```
1991-05-01    8.64
1991-06-01    8.64
1991-07-01    8.64
1991-08-01    8.64
1991-09-01    8.64
              ... 
2015-10-23    4.35
2019-09-20     4.2
2019-10-21     4.2
2019-11-20       0
2019-12-20       0
```

#### 瑞士央行利率决议报告

接口: macro_bank_switzerland_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_switzerland_interest_rate_decision

描述: 瑞士央行利率决议报告, 数据区间从20080313-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_switzerland_interest_rate_se = ak.macro_bank_switzerland_interest_rate()
print(macro_bank_switzerland_interest_rate_se)
print(macro_bank_switzerland_interest_rate_se.name)
```

数据示例

macro_bank_switzerland_interest_rate_se.name

```switzerland_interest_rate```

macro_bank_switzerland_interest_rate_se: pandas.Series

```
2008-03-13     2.75
2008-06-19     2.75
2008-09-18     2.75
2008-10-08        1
2008-12-11      0.5
2009-03-12     0.25
2009-06-18     0.25
2009-09-17     0.25
2009-12-10     0.25
2010-03-11     0.25
2010-06-17     0.25
2010-09-16     0.25
2010-12-16     0.25
2011-03-17     0.25
2011-06-16     0.25
2011-08-03        0
2011-09-15        0
2011-12-15        0
2012-03-15        0
2012-06-14        0
2012-09-13        0
2012-12-13        0
2013-03-14        0
2013-06-20        0
2013-09-19        0
2013-12-12        0
2014-03-20        0
2014-06-19        0
2014-09-18        0
2014-12-11        0
2014-12-18    -0.25
2015-01-15    -0.75
2015-03-19    -0.75
2015-06-18    -0.75
2015-09-17    -0.75
2015-12-10    -0.75
2016-03-17    -0.75
2016-06-16    -0.75
2016-09-15    -0.75
2016-12-15    -0.75
2017-03-16    -0.75
2017-06-15    -0.75
2017-09-14    -0.75
2017-12-14    -0.75
2018-03-15    -0.75
2018-06-21    -0.75
2018-09-20    -0.75
2018-12-13    -0.75
2019-03-21    -0.75
2019-06-13    -0.75
2019-09-19    -0.75
2019-12-12    -0.75
```

#### 英国央行决议报告

接口: macro_bank_english_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_english_interest_rate_decision

描述: 英国央行决议报告, 数据区间从19700101-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_english_interest_rate_se = ak.macro_bank_english_interest_rate()
print(macro_bank_english_interest_rate_se)
print(macro_bank_english_interest_rate_se.name)
```

数据示例

macro_bank_english_interest_rate_se.name

```english_interest_rate```

macro_bank_english_interest_rate_se: pandas.Series

```
1970-01-01       8
1970-02-01       8
1970-03-01       8
1970-04-01     7.5
1970-05-01       7
              ... 
2019-08-01    0.75
2019-09-19    0.75
2019-11-07    0.75
2019-12-19    0.75
2020-01-30       0
```

#### 澳洲联储决议报告

接口: macro_bank_australia_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_australia_interest_rate_decision

描述: 澳洲联储决议报告, 数据区间从19800201-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_australia_interest_rate_se = ak.macro_bank_australia_interest_rate()
print(macro_bank_australia_interest_rate_se)
print(macro_bank_australia_interest_rate_se.name)
```

数据示例

macro_bank_australia_interest_rate_se.name

```australia_interest_rate```

macro_bank_australia_interest_rate_se: pandas.Series

```
1980-02-01     7.92
1980-03-01      8.2
1980-04-01     9.25
1980-05-01     8.98
1980-06-01    10.74
              ...  
2019-08-06        1
2019-09-03        1
2019-10-01     0.75
2019-11-05     0.75
2019-12-03     0.75
```

#### 日本利率决议报告

接口: macro_bank_japan_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_japan_interest_rate_decision

描述: 日本利率决议报告, 数据区间从20080214-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_japan_interest_rate_se = ak.macro_bank_japan_interest_rate()
print(macro_bank_japan_interest_rate_se)
print(macro_bank_japan_interest_rate_se.name)
```

数据示例

macro_bank_japan_interest_rate_se.name

```japan_interest_rate```

macro_bank_japan_interest_rate_se: pandas.Series

```
2008-02-14     0.5
2008-03-07     0.5
2008-04-09     0.5
2008-04-30     0.5
2008-06-13     0.5
              ... 
2019-06-20    -0.1
2019-07-30    -0.1
2019-09-19    -0.1
2019-10-31    -0.1
2019-12-19    -0.1
```

#### 俄罗斯利率决议报告

接口: macro_bank_russia_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_russia_interest_rate_decision

描述: 俄罗斯利率决议报告, 数据区间从20030601-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_russia_interest_rate_se = ak.macro_bank_russia_interest_rate()
print(macro_bank_russia_interest_rate_se)
print(macro_bank_russia_interest_rate_se.name)
```

数据示例

macro_bank_russia_interest_rate_se.name

```russia_interest_rate```

macro_bank_russia_interest_rate_se: pandas.Series

```
2003-06-01     6.5
2003-07-01     6.5
2003-08-01     6.5
2003-09-01     6.5
2003-10-01     6.5
              ... 
2019-07-26    7.25
2019-09-06       7
2019-10-25     6.5
2019-12-13    6.25
2020-02-07       0
```

#### 印度利率决议报告

接口: macro_bank_india_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_india_interest_rate_decision

描述: 印度利率决议报告, 数据区间从20000801-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_india_interest_rate_se = ak.macro_bank_india_interest_rate()
print(macro_bank_india_interest_rate_se)
print(macro_bank_india_interest_rate_se.name)
```

数据示例

macro_bank_india_interest_rate_se.name

```india_interest_rate```

macro_bank_india_interest_rate_se: pandas.Series

```
2000-08-01     7.375
2000-09-01    13.348
2000-10-01    10.524
2000-11-01     8.614
2000-12-01         8
               ...  
2019-04-04         6
2019-06-06      5.75
2019-08-07       5.4
2019-10-04      5.15
2019-12-05      5.15
```

#### 巴西利率决议报告

接口: macro_bank_brazil_interest_rate

目标地址: https://datacenter.jin10.com/reportType/dc_brazil_interest_rate_decision

描述: 巴西利率决议报告, 数据区间从20080201-至今

限量: 单次返回所有历史数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| 无 | 无 | 无 | 无 |

输出参数

| 名称          | 类型 | 默认显示 | 描述           |
| --------------- | ----- | -------- | ---------------- |
| 日期      | str   | Y        | 日期-索引  |
| 今值(%)     | float   | Y        | 今值(%)   |

接口示例

```python
import akshare as ak
macro_bank_brazil_interest_rate_se = ak.macro_bank_brazil_interest_rate()
print(macro_bank_brazil_interest_rate_se)
print(macro_bank_brazil_interest_rate_se.name)
```

数据示例

macro_bank_brazil_interest_rate_se.name

```brazil_interest_rate```

macro_bank_brazil_interest_rate_se: pandas.Series

```
2008-02-01    11.25
2008-04-01    11.25
2008-05-01    11.75
2008-07-01    12.25
2008-08-01       13
              ...  
2019-06-20      6.5
2019-08-01        6
2019-09-19      5.5
2019-10-31        5
2019-12-12      4.5
```

### 银行间拆借利率

接口: rate_interbank

目标地址: http://data.eastmoney.com/shibor/shibor.aspx?m=sg&t=88&d=99333&cu=sgd&type=009065&p=79

描述: 获取指定具体市场具体品种具体指标的拆借利率数据

输入参数

| 名称   | 类型 | 必选 | 描述                                                                              |
| -------- | ---- | ---- | --- |
| market | str  | Y    |   market="上海银行同业拆借市场"; 参见 **市场-品种-指标一览表**|
| symbol | str  | Y    |   symbol="Shibor人民币"; 参见 **市场-品种-指标一览表**|
| indicator | str  | Y    |   indicator="隔夜"; 参见 **市场-品种-指标一览表**|

市场-品种-指标一览表

| market                 | symbol       | indicator |
|------------------------|--------------|-----------|
| 上海银行同业拆借市场   | Shibor人民币 | 隔夜      |
| 上海银行同业拆借市场   | Shibor人民币 | 1周       |
| 上海银行同业拆借市场   | Shibor人民币 | 2周       |
| 上海银行同业拆借市场   | Shibor人民币 | 1月       |
| 上海银行同业拆借市场   | Shibor人民币 | 3月       |
| 上海银行同业拆借市场   | Shibor人民币 | 6月       |
| 上海银行同业拆借市场   | Shibor人民币 | 9月       |
| 上海银行同业拆借市场   | Shibor人民币 | 1年       |
| 中国银行同业拆借市场   | Chibor人民币 | 隔夜      |
| 中国银行同业拆借市场   | Chibor人民币 | 1周       |
| 中国银行同业拆借市场   | Chibor人民币 | 2周       |
| 中国银行同业拆借市场   | Chibor人民币 | 3周       |
| 中国银行同业拆借市场   | Chibor人民币 | 1月       |
| 中国银行同业拆借市场   | Chibor人民币 | 2月       |
| 中国银行同业拆借市场   | Chibor人民币 | 3月       |
| 中国银行同业拆借市场   | Chibor人民币 | 4月       |
| 中国银行同业拆借市场   | Chibor人民币 | 6月       |
| 中国银行同业拆借市场   | Chibor人民币 | 9月       |
| 中国银行同业拆借市场   | Chibor人民币 | 1年       |
| 伦敦银行同业拆借市场   | Libor英镑    | 隔夜      |
| 伦敦银行同业拆借市场   | Libor英镑    | 1周       |
| 伦敦银行同业拆借市场   | Libor英镑    | 1月       |
| 伦敦银行同业拆借市场   | Libor英镑    | 2月       |
| 伦敦银行同业拆借市场   | Libor英镑    | 3月       |
| 伦敦银行同业拆借市场   | Libor英镑    | 8月       |
| 伦敦银行同业拆借市场   | Libor美元    | 隔夜      |
| 伦敦银行同业拆借市场   | Libor美元    | 1周       |
| 伦敦银行同业拆借市场   | Libor美元    | 1月       |
| 伦敦银行同业拆借市场   | Libor美元    | 2月       |
| 伦敦银行同业拆借市场   | Libor美元    | 3月       |
| 伦敦银行同业拆借市场   | Libor美元    | 8月       |
| 伦敦银行同业拆借市场   | Libor欧元    | 隔夜      |
| 伦敦银行同业拆借市场   | Libor欧元    | 1周       |
| 伦敦银行同业拆借市场   | Libor欧元    | 1月       |
| 伦敦银行同业拆借市场   | Libor欧元    | 2月       |
| 伦敦银行同业拆借市场   | Libor欧元    | 3月       |
| 伦敦银行同业拆借市场   | Libor欧元    | 8月       |
| 伦敦银行同业拆借市场   | Libor日元    | 隔夜      |
| 伦敦银行同业拆借市场   | Libor日元    | 1周       |
| 伦敦银行同业拆借市场   | Libor日元    | 1月       |
| 伦敦银行同业拆借市场   | Libor日元    | 2月       |
| 伦敦银行同业拆借市场   | Libor日元    | 3月       |
| 伦敦银行同业拆借市场   | Libor日元    | 8月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 1周       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 2周       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 3周       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 1月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 2月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 3月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 4月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 5月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 6月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 7月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 8月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 9月       |
| 欧洲银行同业拆借市场   | Euribor欧元  | 10月      |
| 欧洲银行同业拆借市场   | Euribor欧元  | 11月      |
| 欧洲银行同业拆借市场   | Euribor欧元  | 1年       |
| 香港银行同业拆借市场   | Hibor港元    | 隔夜      |
| 香港银行同业拆借市场   | Hibor港元    | 1周       |
| 香港银行同业拆借市场   | Hibor港元    | 2周       |
| 香港银行同业拆借市场   | Hibor港元    | 1月       |
| 香港银行同业拆借市场   | Hibor港元    | 2月       |
| 香港银行同业拆借市场   | Hibor港元    | 3月       |
| 香港银行同业拆借市场   | Hibor港元    | 4月       |
| 香港银行同业拆借市场   | Hibor港元    | 5月       |
| 香港银行同业拆借市场   | Hibor港元    | 6月       |
| 香港银行同业拆借市场   | Hibor港元    | 7月       |
| 香港银行同业拆借市场   | Hibor港元    | 8月       |
| 香港银行同业拆借市场   | Hibor港元    | 9月       |
| 香港银行同业拆借市场   | Hibor港元    | 10月      |
| 香港银行同业拆借市场   | Hibor港元    | 11月      |
| 香港银行同业拆借市场   | Hibor港元    | 1年       |
| 香港银行同业拆借市场   | Hibor美元    | 隔夜      |
| 香港银行同业拆借市场   | Hibor美元    | 1周       |
| 香港银行同业拆借市场   | Hibor美元    | 2周       |
| 香港银行同业拆借市场   | Hibor美元    | 1月       |
| 香港银行同业拆借市场   | Hibor美元    | 2月       |
| 香港银行同业拆借市场   | Hibor美元    | 3月       |
| 香港银行同业拆借市场   | Hibor美元    | 4月       |
| 香港银行同业拆借市场   | Hibor美元    | 5月       |
| 香港银行同业拆借市场   | Hibor美元    | 6月       |
| 香港银行同业拆借市场   | Hibor美元    | 7月       |
| 香港银行同业拆借市场   | Hibor美元    | 8月       |
| 香港银行同业拆借市场   | Hibor美元    | 9月       |
| 香港银行同业拆借市场   | Hibor美元    | 10月      |
| 香港银行同业拆借市场   | Hibor美元    | 11月      |
| 香港银行同业拆借市场   | Hibor美元    | 1年       |
| 香港银行同业拆借市场   | Hibor人民币  | 隔夜      |
| 香港银行同业拆借市场   | Hibor人民币  | 1周       |
| 香港银行同业拆借市场   | Hibor人民币  | 2周       |
| 香港银行同业拆借市场   | Hibor人民币  | 1月       |
| 香港银行同业拆借市场   | Hibor人民币  | 2月       |
| 香港银行同业拆借市场   | Hibor人民币  | 3月       |
| 香港银行同业拆借市场   | Hibor人民币  | 6月       |
| 香港银行同业拆借市场   | Hibor人民币  | 1年       |
| 新加坡银行同业拆借市场 | Sibor星元    | 1月       |
| 新加坡银行同业拆借市场 | Sibor星元    | 2月       |
| 新加坡银行同业拆借市场 | Sibor星元    | 3月       |
| 新加坡银行同业拆借市场 | Sibor星元    | 6月       |
| 新加坡银行同业拆借市场 | Sibor星元    | 9月       |
| 新加坡银行同业拆借市场 | Sibor星元    | 1年       |
| 新加坡银行同业拆借市场 | Sibor美元    | 1月       |
| 新加坡银行同业拆借市场 | Sibor美元    | 2月       |
| 新加坡银行同业拆借市场 | Sibor美元    | 3月       |
| 新加坡银行同业拆借市场 | Sibor美元    | 6月       |
| 新加坡银行同业拆借市场 | Sibor美元    | 9月       |
| 新加坡银行同业拆借市场 | Sibor美元    | 1年       |

```python
import akshare as ak
rate_interbank_df = ak.rate_interbank(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="3月")
print(rate_interbank_df)
```

数据示例

```
           日期   利率(%)  涨跌(BP)
0     2019-06-12  2.0019   0.000
1     2019-06-11  2.0019  -0.025
2     2019-06-10  2.0022  -0.025
3     2019-06-07  2.0024  -0.191
4     2019-06-05  2.0043   0.000
          ...     ...     ...
1577  2012-06-05  0.4167  -0.166
1578  2012-06-04  0.4183  -0.334
1579  2012-06-01  0.4217   0.000
1580  2012-05-31  0.4217   0.000
1581  2012-05-30  0.4217   0.000
```
