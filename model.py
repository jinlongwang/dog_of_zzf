# -*- coding=utf-8 -*-
"""
this is peewee model
"""
__author__ = "jinlong"
from peewee import *
db = MySQLDatabase("zzf", user="root", passwd="")

class BaseModel(Model):
    class Meta:
        database = db


class News(BaseModel):
    title = CharField()
    content = CharField(null=True)
    date = DateField(null=True)
    link = CharField(null=True)
    type = IntegerField(null=True)
    update_time = DateTimeField(null=True)

#News.create_table()
if __name__ == "__main__":
    #News.create_table()
    #a = News(title="hehe")
    #a.save()

    a =  News.filter(title="hehe")
    for i in a:
        print i.title







