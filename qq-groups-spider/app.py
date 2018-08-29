#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import sys
app_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(app_root, 'vendor'))
from bottle import *
import requests
from time import time, sleep
from random import random
try:
    import ujson as json
except ImportError:
    import simplejson as json
from io import BytesIO
import pyexcel as pe
import unicodecsv as csv
import re
import zipfile
from uuid import uuid4
#import sae

attachments = {}
sourceURL = 'http://find.qq.com/index.html?version=1&im_version=5533&width=910&height=610&search_target=0'


class QQGroups(object):
    """QQ Groups Spider"""

    def __init__(self):
        super(QQGroups, self).__init__()
        self.js_ver = '10226'
        self.newSession()

    def newSession(self):
        self.sess = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.59 QQ/8.9.3.21169 Safari/537.36'
        }
        self.sess.headers.update(headers)
        return

    def getQRCode(self):
        self.newSession()
        try:
            url = 'http://ui.ptlogin2.qq.com/cgi-bin/login'
            params = {
                'appid': '715030901',
                'daid': '73',
                'pt_no_auth': '1',
                's_url': sourceURL
            }
            resp = self.sess.get(url, params=params, timeout=1000)
            pattern = r'imgcache\.qq\.com/ptlogin/ver/(\d+)/js'
            try:
                self.js_ver = re.search(pattern, resp.content).group(1)
            except:
                pass
            self.sess.headers.update({'Referer': url})
            url = 'http://ptlogin2.qq.com/ptqrshow'
            params = {
                'appid': '715030901',
                'e': '2',
                'l': 'M',
                's': '3',
                'd': '72',
                'v': '4',
                't': '%.17f' % (random()),
                'daid': '73'
            }
            resp = self.sess.get(url, params=params, timeout=1000)
            response.set_header('Content-Type', 'image/png')
            response.add_header('Cache-Control', 'no-cache, no-store')
            response.add_header('Pragma', 'no-cache')
        except:
            resp = None
        return resp

    def qrLogin(self):
        login_sig = self.sess.cookies.get_dict().get('pt_login_sig', '')
        qrsig = self.sess.cookies.get_dict().get('qrsig', '')
        status = -1
        errorMsg = ''
        if all([login_sig, qrsig]):
            url = 'http://ptlogin2.qq.com/ptqrlogin'
            params = {
                'u1': sourceURL,
                'ptqrtoken': self.genqrtoken(qrsig),
                'ptredirect': '1',
                'h': '1',
                't': '1',
                'g': '1',
                'from_ui': '1',
                'ptlang': '2052',
                'action': '0-0-%d' % (time() * 1000),
                'js_ver': self.js_ver,
                'js_type': '1',
                'login_sig': login_sig,
                'pt_uistyle': '40',
                'aid': '715030901',
                'daid': '73'
            }
            try:
                resp = self.sess.get(url, params=params, timeout=1000)
                result = resp.content
                if '二维码未失效' in result:
                    status = 0
                elif '二维码认证中' in result:
                    status = 1
                elif '登录成功' in result:
                    status = 2
                elif '二维码已失效' in result:
                    status = 3
                else:
                    errorMsg = str(result.text)
            except:
                try:
                    errorMsg = str(resp.status_code)
                except:
                    pass
        loginResult = {
            'status': status,
            'time': time(),
            'errorMsg': errorMsg,
        }
        resp = json.dumps(loginResult)
        response.set_header('Content-Type', 'application/json; charset=UTF-8')
        response.add_header('Cache-Control', 'no-cache; must-revalidate')
        response.add_header('Expires', '-1')
        return resp

    def qqunSearch(self, request):
        sort = request.forms.get('sort')
        pn = int(request.forms.get('pn'))
        ft = request.forms.get('ft')
        kws = request.forms.get('kws').strip()
        if not kws:
            redirect('/qqun')
        kws = re.sub(r'[\r\n]', '\t', kws)
        kws = [k.strip() for k in kws.split('\t') if k.strip()]
        self.sess.headers.update({'Referer': sourceURL})
        skey = self.sess.cookies.get_dict().get('skey', '')
        try:
            buff = BytesIO()
            zip_archive = zipfile.ZipFile(buff, mode='w')
            temp = []
            for i in xrange(len(kws)):
                temp.append(BytesIO())
            for i, kw in enumerate(kws[:10]):
                groups = [(u'群名称', u'群号', u'群人数', u'群上限',
                           u'群主', u'地域', u'分类', u'标签', u'群简介')]
                gListRaw = []
                for page in xrange(0, pn):
                    # sort type: 0 deafult, 1 menber, 2 active
                    url = 'http://qun.qq.com/cgi-bin/group_search/pc_group_search'
                    data = {
                        'k': u'交友',
                        'n': '8',
                        'st': '1',
                        'iso': '1',
                        'src': '1',
                        'v': '4903',
                        'bkn': self.genbkn(skey),
                        'isRecommend': 'false',
                        'city_id': '0',
                        'from': '1',
                        'keyword': kw,
                        'sort': sort,
                        'wantnum': '24',
                        'page': page,
                        'ldw': self.genbkn(skey)
                    }
                    resp = self.sess.post(url, data=data, timeout=1000)
                    if resp.status_code != 200:
                        print '%s\n%s' % (resp.status_code, resp.text)
                    result = json.loads(resp.content)
                    gList = result['group_list']
                    gListRaw.extend(gList)
                    for g in gList:
                        name = self.rmWTS(g['name'])
                        code = g['code']
                        member_num = g['member_num']
                        max_member_num = g['max_member_num']
                        owner_uin = g['owner_uin']
                        qaddr = ' '.join(g['qaddr'])
                        try:
                            gcate = ' | '.join(g['gcate'])
                        except:
                            gcate = ''
                        try:
                            _labels = [l.get('label', '') for l in g['labels']]
                            labels = self.rmWTS(' | '.join(_labels))
                        except:
                            labels = ''
                        memo = self.rmWTS(g['memo'])
                        gMeta = (name, code, member_num, max_member_num,
                                 owner_uin, qaddr, gcate, labels, memo)
                        groups.append(gMeta)
                    if len(gList) == 1:
                        break
                    sleep(2.5)
                if ft == 'xls':
                    sheet = pe.Sheet(groups)
                    sheet.save_to_memory('xls', temp[i])
                elif ft == 'csv':
                    writer = csv.writer(
                        temp[i], dialect='excel', encoding='utf-8')
                    writer.writerows(groups)
                elif ft == 'json':
                    json.dump(gListRaw, temp[i], indent=4, sort_keys=True)
            for i in xrange(len(kws)):
                zip_archive.writestr(kws[i].decode(
                    'utf-8') + '.' + ft, temp[i].getvalue())
            zip_archive.close()
            resultId = uuid4().hex
            attachments.update({resultId: buff})
            response.set_header('Content-Type', 'text/html; charset=UTF-8')
            response.add_header('Cache-Control', 'no-cache; must-revalidate')
            response.add_header('Expires', '-1')
            return resultId
        except Exception, e:
            print e
            abort(500,)

    def genqrtoken(self, qrsig):
        e = 0
        for i in xrange(0, len(qrsig)):
            e += (e << 5) + ord(qrsig[i])
        qrtoken = (e & 2147483647)
        return str(qrtoken)

    def genbkn(self, skey):
        b = 5381
        for i in xrange(0, len(skey)):
            b += (b << 5) + ord(skey[i])
        bkn = (b & 2147483647)
        return str(bkn)

    def rmWTS(self, content):
        pattern = r'\[em\]e\d{4}\[/em\]|&nbsp;|<br>|[\r\n\t]'
        content = re.sub(pattern, ' ', content)
        content = content.replace('&amp;', '&').strip()
        return content


app = Bottle()
q = QQGroups()


@app.route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='static')


@app.route('/')
def home():
    redirect('/qqun')


@app.route('/qqun', method='ANY')
@view('qqun')
def qqun():
    if request.method == 'GET':
        response.set_header('Content-Type', 'text/html; charset=UTF-8')
        response.add_header('Cache-Control', 'no-cache')
        return
    elif request.method == 'POST':
        return q.qqunSearch(request)


@app.route('/getqrcode')
def getQRCode():
    return q.getQRCode()


@app.route('/qrlogin')
def qrLogin():
    return q.qrLogin()


@app.route('/download')
def download():
    resultId = request.query.rid or ''
    f = attachments.get(resultId, '')
    if f:
        response.set_header('Content-Type', 'application/zip')
        response.add_header('Content-Disposition',
                            'attachment; filename="results.zip"')
        return f.getvalue()
    else:
        abort(404)


### SAE ###
# debug(True)
# application = sae.create_wsgi_app(app)


### Local ###
if __name__ == '__main__':
    # https://bottlepy.org/docs/dev/deployment.html#switching-the-server-backend
    try:
        run(app, server='paste', host='localhost',
            port=8080, debug=True, reloader=True)
    except:
        run(app, host='localhost', port=8080, debug=True, reloader=True)
