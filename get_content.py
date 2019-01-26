# 用于获取小说内容
from requests_html import HTMLSession
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# import time

def get_content(url):
    # doCode ='''
    #     (function(){
    #         var bp = document.createElement('script');
    #         bp.src = '//push.zhanzhang.baidu.com/push.js';
    #         var s = document.getElementsByTagName("script")[0];
    #         s.parentNode.insertBefore(bp, s);
    #     })();
    # '''
    # session = HTMLSession()
    # rep = session.get(url=url)
    # temp = rep.html
    # temp.render(script=doCode)
    # temp.encoding = 'utf-8'

    driver = webdriver.PhantomJS(executable_path="./phantomjs.exe",service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@id="content"]')))
    html = driver.page_source

    re_str = r"<div id=\"content\">(.*?)</div>"
    re_class = re.compile(re_str)
    replay = re.findall(re_class,str(html).replace("\n",""))
    return replay[0].replace("&nbsp;&nbsp;&nbsp;&nbsp;","   ").replace("<br><br>","\n")

# print(get_content("http://www.biquyun.com/19_19420/9010087.html"))