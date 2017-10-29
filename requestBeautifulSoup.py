#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import re
from bs4 import BeautifulSoup


def getHtmlCode(url):  # 该方法传入url，返回url的html的源码
    '''headers = {
        'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'
    }'''
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'UTF-8'
    page = r.text
    return page


def getImg(page, localPath):  # 该方法传入html的源码，经过截取其中的img标签，将图片保存到本机
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    soup = BeautifulSoup(page, 'html.parser')  # 按照html格式解析页面
    imgList = soup.find_all('img')  # 返回包含所有img标签的列表
    x = 10
    for imgUrl in imgList:  # 列表循环
        print('正在下载：%s' % imgUrl.get('src'))
        ir = requests.get(imgUrl.get('src'))
        print(imgUrl.get('src'))
        # open().write()方法原始且有效
        # open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
        # x += 1

def getVideo(page):
    soup = BeautifulSoup(page, 'html.parser')  # 按照html格式解析页面
    videoList = soup.find_all('div',class_="thumb")
    for videoUrl in videoList:
        cer = re.compile('<a href="(.*?)"', flags=0)
        strlist = cer.findall(videoUrl.string)
        print(strlist[0])

if __name__ == '__main__':
    url = 'http://www.zhangzishi.cc/20160712mz.html'
    # url = 'https://www.xvideos.com'
    # url = 'http://c.csdnimg.cn/public/common/libs/jquery/jquery-1.9.1.min.js'
    localPath = 'd:/PyProjects/images/'
    page = getHtmlCode(url)
    # with open("1.txt", 'wb') as file:
    #     file.write(page.encode('utf-8'))
    # print(page)
    getImg(page, localPath)
    # getVideo(page)