# -*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import re

loginUrl = 'https://accounts.douban.com/login'
formData = {
    "redir": "https://www.douban.com/people/1386103/contacts",
    "form_email": '',
    "form_password": '',
    "login": u'登录'
}
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
r = requests.post(loginUrl, data=formData, headers=headers)
page = r.text
print r.url

'''获取验证码图片'''
# 利用bs4获取captcha地址
soup = BeautifulSoup(page, "html.parser")
captchaAddr = soup.find('img', id='captcha_image')['src']
# 利用正则表达式获取captcha的ID
reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
captchaID = re.findall(reCaptchaID, page)
# print captchaID
# 保存到本地
urllib.urlretrieve(captchaAddr, "captcha.jpg")
captcha = raw_input('please input the captcha:')

formData['captcha-solution'] = captcha
formData['captcha-id'] = captchaID

r = requests.post(loginUrl, data=formData, headers=headers)
page = r.text
print r.content
