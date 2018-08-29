前段时间安装了一个慕课网app,发现不用注册就可以在线看其中的视频,就有了想爬取其中的视频，用来在电脑上学习。
决定花两天时间用学了一段时间的python做一做。
### 我的新书[《Python爬虫开发与项目实战》](https://item.jd.com/12206762.html)出版了,喜欢的话可以看一下[样章](http://pan.baidu.com/s/1hrWEOYg)
我使用的是pycharm进行开发,使用BeautifulSoup模块解析html,整个代码进行了比较详细的注释。
整个工程结构:

----entity

--------__init__.py

--------fileinfor.py用来描述视频文件信息

----filedeal

--------__init__.py

--------file_downloader.py用于视频文件的下载

----spider 爬虫的核心内容

--------__init__.py

--------html_downloader.py html下载器

--------html_parser.py  html解析器

--------spiderman.py  爬虫核心逻辑

----test test文件夹主要是用来测试一些用例,不参与整个程序运行

----conf.py 一些全局变量

----index.py 程序启动入口


运行环境:
python 2.7.X
<br/>
需要安装的支持模块:
<br/>
BeautifulSoup (pip install或者下载源代码包setup.py)
<br/>
下载链接:https://pypi.python.org/pypi/beautifulsoup4/4.3.2
<br/>
<br/>
运行:在windows上直接双击start.bat,linux上没试
<br/>
我的微信公众号:qiye_python
<br/>
![](qiye2.jpg)
<br/>
博客：http://blog.csdn.net/qiye_/ 和 http://www.cnblogs.com/qiyeboy/
<br/>
使用效果图：
<br/>
![](yanshi1.png)
<br/>
![](yanshi2.png)
<br/>
![](yanshi3.png)
<br/>
-----------------------2016年10月31号更新------------------------
<br/>
修改为新的解析方式，突破慕课网的封锁，添加使用说明截图
