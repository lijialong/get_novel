# 获取小说url
from requests_html import HTMLSession
import re

def get_url(url):
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
    session.close
    # print(temp.html)
    # return str(temp.html)
    re_str = r"<a href=\""+str(url).replace("http://www.biquyun.com","")+r"(.*?)</a>"
    re_class = re.compile(re_str)
    content = re.findall(re_class,str(temp.html))
    return content
# url = 'http://www.biquyun.com/19_19420/'
# print(get_url(url))