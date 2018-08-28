# -*-coding:utf8-*-
import re
import sys
import weibo
import random
import time
import xml

reload(sys)
sys.setdefaultencoding("utf-8")



def weiboInfoSpider(id):
    url = 'http://weibo.cn/' + id + '/info'
    html = weibo.spider(url)

    #     html = '''
    # <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Cache-Control" content="no-cache"/><meta id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0, maximum-scale=2.0" /><link rel="icon" sizes="any" mask href="http://h5.sinaimg.cn/upload/2015/05/15/28/WeiboLogoCh.svg" color="black"><meta name="MobileOptimized" content="240"/><title>曲檀_的资料</title><style type="text/css" id="internalStyle">html,body,p,form,div,table,textarea,input,span,select{font-size:12px;word-wrap:break-word;}body{background:#F8F9F9;color:#000;padding:1px;margin:1px;}table,tr,td{border-width:0px;margin:0px;padding:0px;}form{margin:0px;padding:0px;border:0px;}textarea{border:1px solid #96c1e6}textarea{width:95%;}a,.tl{color:#2a5492;text-decoration:underline;}/*a:link {color:#023298}*/.k{color:#2a5492;text-decoration:underline;}.kt{color:#F00;}.ib{border:1px solid #C1C1C1;}.pm,.pmy{clear:both;background:#ffffff;color:#676566;border:1px solid #b1cee7;padding:3px;margin:2px 1px;overflow:hidden;}.pms{clear:both;background:#c8d9f3;color:#666666;padding:3px;margin:0 1px;overflow:hidden;}.pmst{margin-top: 5px;}.pmsl{clear:both;padding:3px;margin:0 1px;overflow:hidden;}.pmy{background:#DADADA;border:1px solid #F8F8F8;}.t{padding:0px;margin:0px;height:35px;}.b{background:#e3efff;text-align:center;color:#2a5492;clear:both;padding:4px;}.bl{color:#2a5492;}.n{clear:both;background:#436193;color:#FFF;padding:4px; margin: 1px;}.nt{color:#b9e7ff;}.nl{color:#FFF;text-decoration:none;}.nfw{clear:both;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.s{border-bottom:1px dotted #666666;margin:3px;clear:both;}.tip{clear:both; background:#c8d9f3;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tip2{color:#000000;padding:2px 3px;clear:both;}.ps{clear:both;background:#FFF;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tm{background:#feffe5;border:1px solid #e6de8d;padding:4px;}.tm a{color:#ba8300;}.tmn{color:#f00}.tk{color:#ffffff}.tc{color:#63676A;}.c{padding:2px 5px;}.c div a img{border:1px solid #C1C1C1;}.ct{color:#9d9d9d;font-style:italic;}.cmt{color:#9d9d9d;}.ctt{color:#000;}.cc{color:#2a5492;}.nk{color:#2a5492;}.por {border: 1px solid #CCCCCC;height:50px;width:50px;}.me{color:#000000;background:#FEDFDF;padding:2px 5px;}.pa{padding:2px 4px;}.nm{margin:10px 5px;padding:2px;}.hm{padding:5px;background:#FFF;color:#63676A;}.u{margin:2px 1px;background:#ffffff;border:1px solid #b1cee7;}.ut{padding:2px 3px;}.cd{text-align:center;}.r{color:#F00;}.g{color:#0F0;}.bn{background: transparent;border: 0 none;text-align: left;padding-left: 0;}</style><script>if(top != self){top.location = self.location;}</script></head><body><div class="n" style="padding: 6px 4px;"><a href="http://weibo.cn/?tf=5_009&amp;vt=4" class="nl">首页</a>|<a href="http://weibo.cn/msg/?tf=5_010&amp;vt=4" class="nl">消息</a>|<a href="http://huati.weibo.cn?vt=4" class="nl">话题</a>|<a href="http://weibo.cn/search/?tf=5_012&amp;vt=4" class="nl">搜索</a>|<a href="/2807748433/info?from=home&amp;rand=4876&amp;p=r&amp;vt=4" class="nl">刷新</a></div><div class="c"><img src="http://tp2.sinaimg.cn/2807748433/180/5643020173/1" alt="头像" /></div><div class="c">会员等级：未开通&nbsp;<a href="/member/present/comfirmTime?uid=2807748433&amp;vt=4">送Ta会员</a><br/><img src="http://img.t.sinajs.cn/t4/style/images/medal/533_s.gif?version=" alt="一级会员" />&nbsp;<img src="http://img.t.sinajs.cn/t4/style/images/medal/1348_s.gif?version=" alt="浪小淘" />&nbsp;<img src="http://img.t.sinajs.cn/t4/style/images/medal/1163_s.gif?version=" alt="扬V耀5" />&nbsp;<img src="http://img.t.sinajs.cn/t4/style/images/medal/299_s.gif?version=" alt="一言九顶" />&nbsp;<img src="http://img.t.sinajs.cn/t4/style/images/medal/107_s.gif?version=" alt="斗酒百篇" />&nbsp;<a href="/medal/owned?uid=2807748433&amp;vt=4">更多勋章</a></div><div class="tip">基本信息</div><div class="c">昵称:曲檀_<br/>达人:美食 电影 音乐 <br/>性别:男<br/>地区:北京 海淀区<br/>生日:金牛座<br/>性取向：女<br/>感情状况：恋爱中<br/>简介:标签：无法标签。<br/>标签:<a href="/search/?keyword=%E5%BE%AE%E5%8D%9A%E5%A5%87%E8%91%A9&amp;stag=1&amp;vt=4">微博奇葩</a>&nbsp;<a href="/search/?keyword=%E5%AE%A4%E5%86%85%E8%AE%BE%E8%AE%A1&amp;stag=1&amp;vt=4">室内设计</a>&nbsp;<a href="/account/privacy/tags/?uid=2807748433&amp;vt=4&amp;st=6134b0">更多&gt;&gt;</a><br/></div><div class="tip">学习经历</div><div class="c">·中国人民大学&nbsp;15级<br/>·郑州大学&nbsp;11级<br/></div><div class="tip">工作经历</div><div class="c">·中国人民大学&nbsp;2015年-2016年<br/></div><div class="tip">其他信息</div><div class="c">互联网:http://weibo.com/chnqutan<br/>手机版:http://weibo.cn/chnqutan<br/><a href="/album/albumlist?fuid=2807748433&amp;vt=4">他的相册&gt;&gt;</a></div><div class="cd"><a href="#top"><img src="http://u1.sinaimg.cn/3g/image/upload/0/62/203/18979/5e990ec2.gif" alt="TOP"/></a></div><div class="pms"> <a href="http://weibo.cn?vt=4">首页</a>.<a href="http://weibo.cn/topic/240489?vt=4">反馈</a>.<a href="http://weibo.cn/page/91?vt=4">帮助</a>.<a  href="http://down.sina.cn/weibo/default/index/soft_id/1/mid/0?vt=4"  >客户端</a>.<a href="http://weibo.cn/spam/?rl=1&amp;type=3&amp;fuid=2807748433&amp;vt=4" class="kt">举报</a>.<a href="http://passport.sina.cn/sso/logout?r=http%3A%2F%2Fweibo.cn%2Fpub%2F%3Fvt%3D4&amp;entry=mweibo&amp;vt=4">退出</a></div><div class="c">设置:<a href="http://weibo.cn/account/customize/skin?tf=7_005&amp;vt=4&amp;st=6134b0">皮肤</a>.<a href="http://weibo.cn/account/customize/pic?tf=7_006&amp;vt=4&amp;st=6134b0">图片</a>.<a href="http://weibo.cn/account/customize/pagesize?tf=7_007&amp;vt=4&amp;st=6134b0">条数</a>.<a href="http://weibo.cn/account/privacy/?tf=7_008&amp;vt=4&amp;st=6134b0">隐私</a></div><div class="c">彩版|<a href="http://m.weibo.cn/?tf=7_010&amp;vt=4">触屏</a>|<a href="http://weibo.cn/page/521?tf=7_011&amp;vt=4">语音</a></div><div class="b">weibo.cn[01-12 09:58]</div></body></html>'''

    filename = './info/' + id + '.txt'
    f = open(filename, 'w')

    print u'ID：' + id
    f.writelines(u'ID：' + id + '\n')
    try:
        nicheng = re.search(r'>昵称:(.*?)<br/>', html, re.S).group(1)
        print u'昵称：' + nicheng
        f.writelines(u'昵称：' + nicheng + '\n')
    except AttributeError:
        print u'账号被封......'
        print u'目前ID:' + id

    try:
        xingbie = re.search(r'性别:(.*?)<br/>', html, re.S).group(1)
        print u'性别：' + xingbie
        f.writelines(u'性别：' + xingbie + '\n')
    except AttributeError:
        pass

    try:
        diqu = re.search(r'<br/>地区:(.*?)<br/>', html, re.S).group(1)
        print u'地区：' + diqu
        f.writelines(u'地区：' + diqu + '\n')
    except AttributeError:
        pass
    try:
        shengri = re.search(r'生日:(.*?)<br/>', html, re.S).group(1)
        print u'生日：' + shengri
        f.writelines(u'生日：' + shengri + '\n')
    except AttributeError:
        pass

    try:
        xingquxiang = re.search(r'<br/>性取向：(.*?)<br/>', html, re.S).group(1)
        print u'性取向：' + xingquxiang
        f.writelines(u'性取向：' + xingquxiang + '\n')
    except AttributeError:
        pass

    try:
        ganqingzhuangkuang = re.search(r'<br/>感情状况：(.*?)<br/>', html, re.S).group(1)
        print u'感情状况：' + ganqingzhuangkuang
        f.writelines(u'感情状况：' + ganqingzhuangkuang + '\n')
    except AttributeError:
        pass

    try:
        jianjie = re.search(r'<br/>简介:(.*?)<br/>', html, re.S).group(1)
        print u'简介：' + jianjie
        f.writelines(u'简介：' + jianjie + '\n')
    except AttributeError:
        pass

    try:
        biaoqian = re.search(r'<br/>标签:(.*?)<br/>', html, re.S).group(1)
        biaoqians = re.findall(r'>(.*?)</a>&nbsp', biaoqian, re.S)
        biaoqian = ''
        for each in biaoqians:
            biaoqian = biaoqian + each + ' '
        print u'标签：' + biaoqian.strip()
        f.writelines(u'标签：' + biaoqian + '\n')
    except AttributeError:
        pass

    try:
        daren = re.search(r'达人:(.*?)<br/>', html, re.S).group(1)
        print u'达人：' + daren
        f.writelines(u'达人：' + daren + '\n')
    except AttributeError:
        pass

    try:
        xuexi = re.search(r'学习经历</div><div class="c">·(.*?)<br/></div><div class="tip">', html, re.S).group(1)
        xuexi = re.sub('&nbsp;', ' ', xuexi)
        xuexi = re.sub('<br/>·', ' ; ', xuexi)
        print u'学习经历：' + xuexi
        f.writelines(u'学习经历：' + xuexi + '\n')
    except AttributeError:
        pass

    try:
        gongzuo = re.search(r'工作经历</div><div class="c">·(.*?)<br/></div><div class="tip">', html, re.S).group(1)
        gongzuo = re.sub('&nbsp;', ' ', gongzuo)
        gongzuo = re.sub('<br/>·', ' ; ', gongzuo)
        print u'工作经历：' + gongzuo
        f.writelines(u'工作经历：' + gongzuo + '\n')
    except AttributeError:
        pass
    f.close()


if __name__ == '__main__':
    # f = open('weiboIdList.txt', 'r')
    # for line in f:
    #     weiboid = line.strip()
    #     weiboInfoSpider(weiboid)
    #     timerand = random.randint(10, 25)
    #     # print 'sleep time '+str(timerand)+'s'
    #     time.sleep(int(timerand))
    # f.close()

    weiboid = '1249159055'
    weiboInfoSpider(weiboid)