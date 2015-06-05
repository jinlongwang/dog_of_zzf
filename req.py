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
        news = news.find_all()


get_content_from_url("http://www.bjjs.gov.cn/publish/portal0/tab4021/")


