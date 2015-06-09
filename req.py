# -*- coding=utf-8 -*-
import datetime
import requests
from bs4 import *
from mailService import *

#ess_ctr10041_ListC_Info_LstC_Info
#
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


def analysis(*args, **kwargs):
    pass

def timer(func, param):
    while True:
        try:
            minute = datetime.datetime.now().second
            if minute == 0:
                result = func(param)
                for res in result:
                    title = res.get('title')
                    if title.find("中海") > 0:
                        content = "详情请点击:" + res.get('href') + "<br>"
                        content += res.get("time")
                        send_message_mandrillcc(['superrz@163.com', 'yulu0511@126.com'], title, content)
        except Exception,e:
            print e
            continue

if __name__ == "__main__":
    timer(analysis, 'http://www.bjjs.gov.cn/publish/portal0/tab4021/')

