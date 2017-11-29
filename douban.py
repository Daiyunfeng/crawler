#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import re
from bs4 import BeautifulSoup
'''
试着爬豆瓣
'''

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

if __name__ == '__main__':
    url = 'https://movie.douban.com/subject/26378579/'

    page = getHtmlCode(url)

    print(page)

'''
 <a href="/subject/26378579/discussion/" rel="nofollow"> 去这部影片的讨论区（全部337条）论坛
 https://movie.douban.com/subject/26378579/reviews 影评   获取评分
 https://movie.douban.com/subject/26378579/comments?status=P 短评 获取评分
 <div class="recommendations-bd"> 中寻找a标签get href 获得 推荐电影
 https://movie.douban.com/subject/26378579/celebrities 影人
 
 html.find_all("span", attrs={"property": "v:xxx"})[x].get_text()
 <div class="indent" id="link-report">            
        <span property="v:summary" class="">
            　　时光飞逝，一转眼，艾格西（塔伦·埃格顿 Taron Egerton 饰）已经成长为了一名出色而又可靠的特工，他和蒂尔德公主（汉娜·阿尔斯托姆 Hanna Alström 饰）之间的感情也愈演愈浓，两人眼看着就要携手步入婚姻的殿堂。就在这个节骨眼上，前特工查理（爱德华·霍尔克罗夫特 Edward Holcroft 饰）杀了回来，如今的他效力于一个名为“黄金圈”的贩毒组织，组织头目波比（朱丽安·摩尔 Julianne Moore 饰）是一个邪恶而又野心勃勃的女人。
                <br />
            　　查理查出了金士曼的所有据点，用导弹将它们全部摧毁。幸存的艾格西和梅林（马克·斯特朗 Mark Strong 饰）千里迢迢远赴美国，向潜伏在那里的联邦特工寻求帮助。波比种植了一种含有毒素的大麻，将它们输送往世界各地，当瘾君子们体内的毒素渐渐发作后，波比以此为筹码，正式向政府宣战。
        </span>
 </div>
 <strong class="ll rating_num" property="v:average">7.2</strong>
 <span property="v:votes">91184</span>人评价</a>
    
  <div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1031852/" rel="v:directedBy">马修·沃恩</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1018114/">简·古德曼</a> / <a href="/celebrity/1031852/">马修·沃恩</a> / <a href="/celebrity/1014154/">马克·米勒</a> / <a href="/celebrity/1001198/">戴夫·吉布森</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1340497/" rel="v:starring">塔伦·埃格顿</a> / <a href="/celebrity/1031223/" rel="v:starring">科林·费尔斯</a> / <a href="/celebrity/1274374/" rel="v:starring">马克·斯特朗</a> / <a href="/celebrity/1054519/" rel="v:starring">朱丽安·摩尔</a> / <a href="/celebrity/1000193/" rel="v:starring">埃尔顿·约翰</a> / <a href="/celebrity/1348118/" rel="v:starring">爱德华·霍尔克罗夫特</a> / <a href="/celebrity/1054415/" rel="v:starring">哈莉·贝瑞</a> / <a href="/celebrity/1329628/" rel="v:starring">佩德罗·帕斯卡</a> / <a href="/celebrity/1031224/" rel="v:starring">查宁·塔图姆</a> / <a href="/celebrity/1036313/" rel="v:starring">杰夫·布里吉斯</a> / <a href="/celebrity/1027154/" rel="v:starring">迈克尔·刚本</a> / <a href="/celebrity/1343282/" rel="v:starring">索菲·库克森</a> / <a href="/celebrity/1057177/" rel="v:starring">汉娜·奥斯特罗姆</a> / <a href="/celebrity/1091838/" rel="v:starring">比约恩·格拉纳特</a> / <a href="/celebrity/1009453/" rel="v:starring">莱娜·恩卓</a> / <a href="/celebrity/1341158/" rel="v:starring">波比·迪瓦伊</a> / <a href="/celebrity/1366871/" rel="v:starring">汤姆·本尼迪克·奈特</a> / <a href="/celebrity/1274770/" rel="v:starring">托马斯·图尔格斯</a> / <a href="/celebrity/1019138/" rel="v:starring">基思·艾伦</a> / <a href="/celebrity/1013814/" rel="v:starring">艾米丽·沃森</a> / <a href="/celebrity/1025206/" rel="v:starring">布鲁斯·格林伍德</a> / <a href="/celebrity/1346399/" rel="v:starring">戈登·亚历山大</a> / <a href="/celebrity/1371909/" rel="v:starring">马丁·福特</a> / <a href="/celebrity/1329877/" rel="v:starring">明格斯·约翰斯顿</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">喜剧</span> / <span property="v:genre">动作</span> / <span property="v:genre">冒险</span><br/>
        
        <span class="pl">制片国家/地区:</span> 英国 / 美国<br/>
        <span class="pl">语言:</span> 英语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2017-10-20(中国大陆)">2017-10-20(中国大陆)</span> / <span property="v:initialReleaseDate" content="2017-09-20(英国)">2017-09-20(英国)</span> / <span property="v:initialReleaseDate" content="2017-09-22(美国)">2017-09-22(美国)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="141">141分钟</span> / 139分钟(中国大陆)<br/>
        <span class="pl">又名:</span> 王牌特工2 / 皇家特工：金圈子(港) / 金牌特务：机密对决(台) / 王牌特工2：黄金圆环 / 王牌特工：黄金圈 / Kingsman 2<br/>
        <span class="pl">IMDb链接:</span> <a href="http://www.imdb.com/title/tt4649466" target="_blank" rel="nofollow">tt4649466</a><br>

</div>  
    
    <div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:22px"></div>
        <span class="rating_per">14.2%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">41.2%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:59px"></div>
        <span class="rating_per">38.1%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:8px"></div>
        <span class="rating_per">5.6%</span>
        <br />
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:1px"></div>
        <span class="rating_per">0.9%</span>
        <br />
        </div>
</div>
'''