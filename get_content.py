# 用于获取小说内容
from requests_html import HTMLSession
import re
import asyncio

def get_content(url):
    asyncio.set_event_loop(asyncio.new_event_loop())
    doCode ='''
        (function(){
            var bp = document.createElement('script');
            bp.src = '//push.zhanzhang.baidu.com/push.js';
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    '''
    session = HTMLSession()
    rep = session.get(url=url)
    temp = rep.html
    temp.render(script=doCode)
    temp.encoding = 'utf-8'
    re_str = r"<div id=\"content\">(.*?)</div>"
    re_class = re.compile(re_str)
    replay = re.findall(re_class,str(temp.html).replace("\n",""))
    # print(temp.html)
    return replay[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;","   ").replace("<br><br>","\n")

# print(get_content("http://www.biquyun.com/19_19420/9010087.html"))