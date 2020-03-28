![](https://github.com/jindaxiang/akshare/blob/master/example/images/AkShare_logo.jpg)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/akshare.svg)](https://pypi.org/project/akshare/) 
[![PyPI](https://img.shields.io/pypi/v/akshare.svg)](https://pypi.org/project/akshare/) 
[![Downloads](https://pepy.tech/badge/akshare)](https://pepy.tech/project/akshare)
[![Documentation Status](https://readthedocs.org/projects/akshare/badge/?version=latest)](https://akshare.readthedocs.io/zh_CN/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![akshare](https://img.shields.io/badge/Data%20Science-AkShare-green)](https://github.com/jindaxiang/akshare)
[![Actions Status](https://github.com/jindaxiang/akshare/workflows/build/badge.svg)](https://github.com/jindaxiang/akshare/actions)
[![MIT Licence](https://camo.githubusercontent.com/14a9abb7e83098f2949f26d2190e04fb1bd52c06/68747470733a2f2f626c61636b2e72656164746865646f63732e696f2f656e2f737461626c652f5f7374617469632f6c6963656e73652e737667)](https://github.com/jindaxiang/akshare/blob/master/LICENSE)
[![](https://img.shields.io/github/forks/jindaxiang/akshare)](https://github.com/jindaxiang/akshare)
[![](https://img.shields.io/github/stars/jindaxiang/akshare)](https://github.com/jindaxiang/akshare)
[![](https://img.shields.io/github/issues/jindaxiang/akshare)](https://github.com/jindaxiang/akshare)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

# ![](https://github.com/jindaxiang/akshare/blob/master/example/images/akshare_home.png)

## Overview

[AkShare](https://github.com/jindaxiang/akshare) support Python 3.6+, aims to make fetch financial data as convenient as possible.

**Write less, get more!**

- Documentation: [中文文档](https://akshare.readthedocs.io/zh_CN/latest/)
- Documentation: [English Forthcoming](https://akshare.readthedocs.io/zh_CN/latest/)

# ![](https://github.com/jindaxiang/akshare/blob/master/example/images/AkShare.png)

## Installation

### General

```
pip install akshare --ugrade
```

### China

```cmd
pip install akshare -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
```

### Docker

```
docker pull registry.cn-hangzhou.aliyuncs.com/akshare/akdocker
```

## Usage

Code

```python
import akshare as ak
hist_df = ak.stock_us_daily(symbol="AMZN")  # Get U.S. stock Amazon's price info
print(hist_df)
```

Output

```
               open     high      low    close   volume
date                                                   
1997-05-15    29.25    30.00    23.13    23.50  6013000
1997-05-16    23.63    23.75    20.50    20.75  1225000
1997-05-19    21.13    21.25    19.50    20.50   508900
1997-05-20    20.75    21.00    19.63    19.63   455600
1997-05-21    19.63    19.75    16.50    17.13  1571100
             ...      ...      ...      ...      ...
2020-02-24  2003.18  2039.30  1987.97  2009.29  6546997
2020-02-25  2026.42  2034.60  1958.42  1972.74  6219094
2020-02-26  1970.28  2014.67  1960.45  1979.59  5240402
2020-02-27  1934.38  1975.00  1882.76  1884.30  8143993
2020-02-28  1814.63  1889.76  1811.13  1883.75  9493797
[5731 rows x 5 columns]
```

## Communication

Pay attention to **数据科学实战** WeChat Official Accounts to get the [AkShare](https://github.com/jindaxiang/akshare) updated info:

<div align=center>
    <img src="https://github.com/jindaxiang/akshare/blob/master/example/images/ds.png">
</div>

Application to add **AkShare-官方** QQ group and talk about [AkShare](https://github.com/jindaxiang/akshare) issues, QQ group number: 326900231

<div align=center>
    <a target="_blank" href="https://shang.qq.com/wpa/qunwpa?idkey=aacb87089dd5ecb8c6620ce391de15b92310cfb65e3b37f37eb465769e3fc1a3">
        <img border="0" src="https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/qq/akshare_md_fold_1569925684166.png" alt="AkShare官方" title="AkShare官方" align="center">
    </a>
</div>

## Features

- **Easy**: Just one line to fetch the data;
- **Fast**: Just copy and paste;
- **Extensible**: Easy to customize your own code;
- **Powerful**: Python ecosystem.

## Tutorials

1. [Overview](https://akshare.readthedocs.io/zh_CN/latest/akshare/ak-introduction.html)
2. [Installation](https://akshare.readthedocs.io/zh_CN/latest/akshare/ak-installation.html)
3. [Tutorial](https://akshare.readthedocs.io/zh_CN/latest/akshare/ak-tutorial.html)
4. [Data Dict](https://akshare.readthedocs.io/zh_CN/latest/README.html)
5. [Subjects](https://akshare.readthedocs.io/zh_CN/latest/subjects/index.html)

## Contribution

[AkShare](https://github.com/jindaxiang/akshare) is still under developing, feel free to open issues and pull requests:

- Report or fix bugs
- Require or publish interface
- Write or fix documentation
- Add test cases

> Notice: We use [Black](https://black.readthedocs.io/en/stable/) to format the code

## Statement

1. The data provided by [AkShare](https://github.com/jindaxiang/akshare) is for reference only and does not constitute any investment proposal;

2. Any investor based on [AkShare](https://github.com/jindaxiang/akshare) research should pay more attention to data risk;

3. [AkShare](https://github.com/jindaxiang/akshare) will insist on providing open-source financial data;

4. Based on some uncontrollable factors, some data interfaces in [AkShare](https://github.com/jindaxiang/akshare) may be removed;

5. Please follow the relevant open-source protocol used by [AkShare](https://github.com/jindaxiang/akshare)

## Show your style

Use the badge in your project's README.md:

```markdown
[![Data: akshare](https://img.shields.io/badge/Data%20Science-AkShare-green)](https://github.com/jindaxiang/akshare)
```

Using the badge in README.rst:

```
.. image:: https://img.shields.io/badge/Data%20Science-AkShare-green
    :target: https://github.com/jindaxiang/akshare
```

Looks like this:

[![Data: akshare](https://img.shields.io/badge/Data%20Science-AkShare-green)](https://github.com/jindaxiang/akshare)

## Citation

Please use this **bibtex** if you want to cite this repository in your publications:

```
@misc{akshare,
    author = {Albert King},
    title = {AkShare},
    year = {2019},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/jindaxiang/akshare}},
}
```

## Acknowledgement

Special thanks [FuShare](https://github.com/LowinLi/fushare) for the opportunity of learning from the project;

Special thanks [TuShare](https://github.com/waditu/tushare) for the opportunity of learning from the project;

Thanks for the data provided by [生意社网站](http://www.100ppi.com/);

Thanks for the data provided by [奇货可查网站](https://qhkch.com/);

Thanks for the data provided by [智道智科网站](https://www.ziasset.com/);

Thanks for the data provided by [中国银行间市场交易商协会网站](http://www.nafmii.org.cn/);

Thanks for the data provided by [99期货网站](http://www.99qh.com/);

Thanks for the data provided by [英为财情网站](https://cn.investing.com/);

Thanks for the data provided by [中国外汇交易中心暨全国银行间同业拆借中心网站](http://www.chinamoney.com.cn/chinese/);

Thanks for the data provided by [金十数据网站](https://www.jin10.com/);

Thanks for the data provided by [交易法门网站](https://www.jiaoyifamen.com/);

Thanks for the data provided by [和讯财经网站](http://www.hexun.com/);

Thanks for the data provided by [新浪财经网站](https://finance.sina.com.cn/);

Thanks for the data provided by [Oxford-Man Institute 网站](https://realized.oxford-man.ox.ac.uk/);

Thanks for the data provided by [DACHENG-XIU 网站](https://dachxiu.chicagobooth.edu/);

Thanks for the data provided by [上海证券交易所网站](http://www.sse.com.cn/assortment/options/price/);

Thanks for the data provided by [深证证券交易所网站](http://www.szse.cn/);

Thanks for the data provided by [中国金融期货交易所网站](http://www.cffex.com.cn/);

Thanks for the data provided by [上海期货交易所网站](http://www.shfe.com.cn/);

Thanks for the data provided by [大连商品交易所网站](http://www.dce.com.cn/);

Thanks for the data provided by [郑州商品交易所网站](http://www.czce.com.cn/);

Thanks for the data provided by [上海国际能源交易中心网站](http://www.ine.com.cn/);

Thanks for the data provided by [Timeanddate 网站](https://www.timeanddate.com/);

Thanks for the data provided by [河北省空气质量预报信息发布系统网站](http://110.249.223.67/publish/);

Thanks for the data provided by [南华期货网站](http://www.nanhua.net/nhzc/varietytrend.html);

Thanks for the data provided by [Economic Policy Uncertainty 网站](http://www.nanhua.net/nhzc/varietytrend.html);

Thanks for the data provided by [微博指数网站](https://data.weibo.com/index/newindex);

Thanks for the data provided by [百度指数网站](http://index.baidu.com/v2/main/index.html);

Thanks for the data provided by [谷歌指数网站](https://trends.google.com/trends/?geo=US);

Thanks for the data provided by [申万指数网站](http://www.swsindex.com/idx0120.aspx?columnid=8832);

Thanks for the data provided by [真气网网站](https://www.aqistudy.cn/);

Thanks for the data provided by [财富网站](http://www.fortunechina.com/);

Thanks for the data provided by [中国证券投资基金业协会网站](http://gs.amac.org.cn/);

Thanks for the data provided by [猫眼电影网站](https://maoyan.com/board/1);

Thanks for the data provided by [Expatistan 网站](https://www.expatistan.com/cost-of-living);

Thanks for the data provided by [北京市碳排放权电子交易平台网站](https://www.bjets.com.cn/article/jyxx/);

Thanks for the data provided by [国家金融与发展实验室网站](http://www.nifd.cn/);

Thanks for the data provided by [IT桔子网站](https://www.itjuzi.com);

Thanks for the data provided by [东方财富网站](http://data.eastmoney.com/jgdy/);

Thanks for the data provided by [义乌小商品指数网站](http://www.ywindex.com/Home/Product/index/);

Thanks for the data provided by [中国国家发展和改革委员会网站](http://jgjc.ndrc.gov.cn/dmzs.aspx?clmId=741);

Thanks for the data provided by [163网站](https://news.163.com/special/epidemic/);

Thanks for the data provided by [丁香园网站](http://3g.dxy.cn/newh5/view/pneumonia?scene=2&clicktime=1579615030&enterid=1579615030&from=groupmessage&isappinstalled=0);

Thanks for the data provided by [百度新型肺炎网站](https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1);

Thanks for the data provided by [百度迁徙网站](https://qianxi.baidu.com/?from=shoubai#city=0);

Thanks for the data provided by [新型肺炎-相同行程查询工具网站](https://rl.inews.qq.com/h5/trip?from=newsapp&ADTAG=tgi.wx.share.message);

Thanks for the data provided by [新型肺炎-小区查询网站](https://ncov.html5.qq.com/community?channelid=1&from=singlemessage&isappinstalled=0);

Thanks for the data provided by [商业特许经营信息管理网站](http://txjy.syggs.mofcom.gov.cn/);

Thanks for the data provided by [慈善中国网站](http://cishan.chinanpo.gov.cn/platform/login.html);

Thanks for the data provided by [思知网站](https://www.ownthink.com/);

Thanks for the data provided by [Currencyscoop网站](https://currencyscoop.com/);

Thanks for the data provided by [新加坡交易所网站](https://www.sgx.com/zh-hans/research-education/derivatives);

Thanks for the tutorial provided by [微信公众号: Python大咖谈](https://upload-images.jianshu.io/upload_images/3240514-61004f2c71be4a0b.png).
