import get_content
import get_url
import threading
import re
import random

url = "http://www.biquyun.com/19_19420/"    #指定小说在笔趣阁中的url
path = "D:\\资料\\scrpylearn\\爬取小说\\"   #指定小说的存放路径

title = get_url.get_url(url)

def save_novel(urlpath):
    for up in urlpath:
        re_str = r"(.*?)\""
        re_class = re.compile(re_str)
        replay = re.findall(re_class,up)
        novel_title = up.replace(replay[0],"").replace("\">","")
        novel_url = url + replay[0]
        with open(path+novel_title+".txt","w") as f:
            f.write(get_content.get_content(novel_url))
            f.close

# 多线程爬取
threads=[]

for i in range(0,10):
    exec("temp%s = []"%(str(i)))

for ur in title:
    exec("temp%s.append('%s')"%(str(random.randint(0,9)),ur))

for i in range(0,10):
    exec("t%s = threading.Thread(target=save_novel,args=(temp%s,))"%(str(i),str(i)))
    exec("threads.append(t%s)"%(str(i)))

for thraed in threads:
    thraed.start()

for thraed in threads:
    thraed.join()
