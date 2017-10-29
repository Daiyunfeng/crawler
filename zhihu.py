import re
import gzip
import urllib
import http.cookiejar
import time
def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

global cj
cj = http.cookiejar.CookieJar()
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    #cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]



url = 'https://www.zhihu.com/'  # 入口页面, 可以换成别的
oper = makeMyOpener()
uop = oper.open(url, timeout=1000)
data = uop.read()
_xsrf=getXSRF(data.decode())
captcha_url="https://www.zhihu.com/captcha.gif?r=%d&type=login"% (time.time() * 1000)
captchadata=oper.open(captcha_url).read()
with open("1.gif",'wb') as file:
    file.write(captchadata)
yanzhengma=input("captcha:")    #手动查看验证码
print(yanzhengma)
postDict = {
        '_xsrf':_xsrf,
        'phone_num': '13588209423',
        'password': 'Hujiacheng1997',
        'captcha':yanzhengma
        #'captcha_type': 'cn'
}
postData = urllib.parse.urlencode(postDict).encode()
uop = oper.open(url+'login/phone_num',postData)
data = uop.read()
print(data.decode())
for item in cj:
    print ('Name = '+item.name)
    print ('Value = '+item.value)