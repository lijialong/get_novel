import get_content
import get_url
import threading
import re
# import random

url = "http://www.biquyun.com/19_19420/"    #指定小说在笔趣阁中的url
path = "D:\\资料\\scrpylearn\\爬取小说\\"   #指定小说的存放路径

title = get_url.get_url(url)
n = 0
# chinese_word = {'一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}
for up in title:
    re_str = r"(.*?)\""
    re_class = re.compile(re_str)
    replay = re.findall(re_class,up)
    novel_title = up.replace(replay[0],"").replace("\">","").replace(" ","")
    # for n in chinese_word:
    #     novel_title = novel_title.replace(n,chinese_word[n])
    novel_url = url + replay[0]
    with open(path+str(n)+novel_title+".txt","w") as f:
        f.write(get_content.get_content(novel_url))
        f.close
    n+=1
    print('>>>>>>已爬取：%s<<<<<<'%(novel_title))

# 多线程爬取
# threads=[]

# for i in range(0,10):
#     exec("temp%s = []"%(str(i)))

# for ur in title:
#     exec("temp%s.append('%s')"%(str(random.randint(0,9)),ur))

# for i in range(0,10):
#     exec("t%s = threading.Thread(target=save_novel,args=(temp%s,))"%(str(i),str(i)))
#     exec("threads.append(t%s)"%(str(i)))

# for thraed in threads:
#     thraed.start()

# for thraed in threads:
#     thraed.join()
