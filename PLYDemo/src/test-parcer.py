__author__ = 'sergey'

#! /usr/bin/env python3.4
from math import *
import sys
from subprocess import call
import os
import io
import redis
import mysql.connector as _m
import urllib.request
from html.parser import HTMLParser
from html.entities import name2codepoint

from bs4 import BeautifulSoup

# MAGIC METHODS
class Parser:
    data = {}

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        #print(args)
        #print(kwargs)

    def __setattr__(self, key, value):
        #print("setattr: key: {0}, value={1}", key, value)
        if not key in ['data']:
            self.data[key]=value

    def __getattr__(self, item):
        if self.data[item]:
            return self.data[item]

    def __delattr__(self, item):
        if self.data[item]:
            del self.data[item]

# PRCER
#class MyHTMLParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
     #   if tag == 'h2':
     #       print("Start tag:", tag)
     #       print('See h2 >>')
     #       print(attrs)

    #def handle_endtag(self, tag):
    #    print("End tag  :", tag)

    #def handle_data(self, data):
    #    print("Data     :", data)

    #def handle_comment(self, data):
    #    print("Comment  :", data)

    #def handle_entityref(self, name):
    #    c = chr(name2codepoint[name])
    #    print("Named ent:", c)

    #def handle_charref(self, name):
    #    if name.startswith('x'):
    #        c = chr(int(name[1:], 16))
    #    else:
    #        c = chr(int(name))
    #    print("Num ent  :", c)

   # def handle_decl(self, data):
    #    print("Decl     :", data)


class parceURL():
    def setUrl(self, url_http="http://google.com/"):
       self._parce = urllib.request.urlopen(url_http).read().decode("utf-8")

#MYSQL
class Child(Parser, parceURL):
    def _mysqlTest(self):
        #pass
        # Open database connection
        db = _m.connect(user="root",password="password",host="localhost",database="python" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()

        print ("Database version : %s ", data)

        cursor.execute("SELECT n.fio as `n_fio`, p.price as `p_price` FROM `names` as n LEFT JOIN `prices` AS p ON p.user_id = n.id")
        result = cursor.fetchall()

        print(result)

        for (n_fio, p_price) in result:
            print(n_fio)
            print(p_price)

        # disconnect from server
        db.close()

    def getResults(self):
        print('getResults')
        print(self.args, self.kwargs)
        for arg in self.args:
            print("Params init: {0}", arg)
        for key in self.kwargs:
            print("Params init: {0}:{1}", key, self.kwargs[key])


def main():
    p = False
    """----------- START LOAD MAIN --------------"""
    print("--LOAD MAIN--")
    p = Child(*[1,2], **{'One':1,'Two':2})
    #p.__call__(*[1,2], **{'One':1,'Two':2})
    p.x = 10
    p.c = 100
    print(p.x, p.c)
    p.getResults()

    """----------- MYSQL --------------"""
    p._mysqlTest()

    """----------- PARCE URL --------------"""
    p.setUrl("http://college-writers.com/")

    print("-------------HTML READ INIT ----------------")
    #phtml = MyHTMLParser()
    #phtml.feed(p._parce)
    #phtml.close()

    """----------- PARCE URL v2--------------"""
    bhtml = BeautifulSoup(p._parce, 'html.parser')
    h1 = bhtml.find_all('h1')
    print ("- OUTPUT <H1> (len:{0}) -".format( len(h1) ))
    for _h1 in h1:
        print(_h1)

    h2 = bhtml.find_all('h2')
    print("- OUTPUT <H2> (len:{0})-".format( len(h2) ))
    for _h2 in h2:
        print(_h2)

    print("----------------INIT PARCER FEAD ---------------");

    #phtml.feed(p.getUrl())
    #phtml.close()
    #p.parce()

    """----------- OK LOAD MAIN --------------"""
    print("--END LOAD MAIN--")

main()

# r = redis.StrictRedis(host="127.0.0.1",port=6379,db=0)
# if r.set("test",10):
#     print( r.get("test") )
#
# r.set("test", 11)
# print(r.get("test"))
