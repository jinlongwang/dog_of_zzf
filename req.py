# -*- coding=utf-8 -*-
import requests
from bs4 import *

#ess_ctr10041_ListC_Info_LstC_Info
#
def get_content_from_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        content = res.content
        #print content
        bsContent = BeautifulSoup(content)
        news = bsContent.find(attrs={'id': "ess_ctr10041_ListC_Info_LstC_Info"})
        infos = news.find_all("table")
        for info in infos:
            detail = info.find_all("td")
            title = detail[1].find("a").attrs.get("title")
            href = detail[1].find("a").attrs.get("href")
            time = detail[2].text
            print title, href, time

def analysis(*args, **kwargs):
    pass


get_content_from_url("http://www.bjjs.gov.cn/publish/portal0/tab4021/")


