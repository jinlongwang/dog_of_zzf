# -*- coding=utf-8 -*-
import datetime
import requests
from bs4 import *
from mailService import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

PREFIX = "http://www.bjjs.gov.cn"

class netWorkException(Exception):
    pass

def get_content_from_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        content = res.content
        bsContent = BeautifulSoup(content)
        news = bsContent.find(attrs={'id': "ess_ctr10041_ListC_Info_LstC_Info"})
        infos = news.find_all("table")
        msg = []
        for info in infos:
            detail = info.find_all("td")
            title = detail[1].find("a").attrs.get("title")
            href = detail[1].find("a").attrs.get("href")
            time = detail[2].text
            print title, href, time
            tempInfo = {
                'title': title,
                'href': href,
                'time': time
            }
            msg.append(tempInfo)
        return msg
    raise netWorkException("open url error")



def analysis(*args, **kwargs):
    pass

def timer(func, *args):
    while True:
        try:
            minute = datetime.datetime.now().second
            if minute%10 == 0:
                result = func(args[0])
                for res in result:
                    title = res.get('title')
                    type(title)
                    if title.find(args[1]) >= 0:
                        content = "详情请点击:" + PREFIX+res.get('href') + "<br>"
                        content += res.get("time")
                        print 'send mail'
                        send_message_mandrillcc(['superrz@163.com', 'yulu0511@126.com'], title, content)
        except Exception,e:
            print e
            continue

def test(func, param):
    result = func(param)
    for res in result:
        title = res.get('title')
        type(title)
        if title.find("恒大") > 0:
            content = "详情请点击:" + res.get('href') + "<br>"
            content += res.get("time")
            send_message_mandrillcc(['superrz@163.com', 'yulu0511@126.com'], title, content)

if __name__ == "__main__":
    print '--------------loop started-----------------'
    timer(get_content_from_url, 'http://www.bjjs.gov.cn/publish/portal0/tab4021/', '中海')

