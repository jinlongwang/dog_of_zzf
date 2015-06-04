# -*- coding=utf-8 -*-
"""
*****maildill sever******
for send email
"""
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

__author__ = 'jinlong'

HOST = "smtp.mandrillapp.com"
PORT = 587
USERNAME = "superrz@163.com"
PASSWORD = "LFJRn8_3hJnq--2w75mEZw"


def send_message_mandrillcc(to,title,body,cc=None):
    """

    :param to:
    :param title:
    :param body:
    :param cc:
    :return:
    """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(title,"utf-8")
    msg['From'] = "JINLONG <notifications@jinlong.com>" # Your from name and email address
    msg['to'] = to
    msg['Cc'] = cc

    emaillist = []
    if cc:
        emaillist = [ c for c in cc.split(",") ]
    emaillist.append(msg['to'])

    part2 = MIMEText(body, 'html','utf-8')
    msg.attach(part2)
    s = smtplib.SMTP(HOST, 587)
    s.login(USERNAME, PASSWORD)
    s.sendmail(msg['From'], emaillist, msg.as_string())
    s.quit()

if __name__ == '__main__':
    send_message_mandrillcc("wangjl@vilstart.com", "hehe", "this is test msg")

