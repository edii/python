__author__ = 'sergey'

#! /usr/bin/env python3.4
from math import *
import sys
import getopt
from subprocess import call
import os
import io
import redis

from datetime import date, datetime, timedelta
import mysql.connector as _m

import urllib.request
from html.parser import HTMLParser
from html.entities import name2codepoint

from bs4 import BeautifulSoup

# =========== // CLASS DATABASES
class Database:

    host = 'localhost'
    user = 'root'
    password = '123'
    db = 'test'

    def __init__(self):
        self.connection = _m.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( _m.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
# ============ // END

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
    def setUrl(self, url_http="http://i.ua/"):
        self._parce = urllib.request.urlopen(url_http).read()
        #.decode("utf-8")

#MYSQL
class Child(Parser, parceURL):

    def _connected(self):
        self.db = _m.connect(user="root",password="password",host="localhost",database="python" )

    def _close(self):
        self.db.close()

    def saveSites(self, site):
        if(site):
            psId = 0
            cursor = self.db.cursor()

            # tomorrow = datetime.now().date() + timedelta(days=1)
            # emp_no = cursor.lastrowid

            cursor.execute("SELECT ps.id as ps_id FROM `parcer_sites` as ps WHERE domain = %(domain)s", {'domain': site})
            psOne = cursor.fetchone()
            try:
                ps_id = psOne[0]
            except:
                ps_id = 0

            if not ps_id:
                try:
                    cursor.execute("""INSERT INTO parcer_sites SET id = NULL, domain = %(domain)s""", {'domain': site})
                    self.db.commit()

                    if cursor.lastrowid:
                        print('last insert id', cursor.lastrowid)
                        psId = cursor.lastrowid
                    else:
                        print('last insert id not found')

                except:
                    self.db.rollback()
            else:
                psId = ps_id

            return psId


    def _mysqlTest(self):
        #pass
        # Open database connection
        #db = _m.connect(user="root",password="password",host="localhost",database="python" )

        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

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
        #self.db.close()

    def getResults(self):
        print('getResults')
        print(self.args, self.kwargs)
        if(self.args):
            for arg in self.args:
                print("Params init:", self.args.index(arg), arg)
        if(self.kwargs):
            for key in self.kwargs:
                print("Params init: {0}:{1}", key, self.kwargs[key])


    def getUrlValue(self):
        self.url = False
        self.verbose = False
        try:
            self.options, self.remainder = getopt.getopt(self.args[1:], 'u:v', ['url=',
                                                                                'verbose',
                                                                                'version=',
                                                                                ])
            if(self.options):
                for opt, arg in self.options:
                    if opt in ('-u', '--url'):
                        self.url = arg
                    elif opt in ('-v', '--verbose'):
                        self.verbose = True
                    elif opt == '--version':
                        self.version = arg

        except getopt.GetoptError:
            print('test.py -u <inputpath>')
            sys.exit(2)

        return self.url

        #if len(self.args) == 3 and self.args[1] == '-u':
        #    return self.args[2]


def main():
    p = False
    """----------- START LOAD MAIN --------------"""
    print("--LOAD MAIN--")

    #print(input("-- TEST SET -- >> "))

    #print(sys.argv[1],sys.argv[2], len(sys.argv))

    p = Child(*sys.argv)

    #**{'One':1,'Two':2}

    #p.__call__(*[1,2], **{'One':1,'Two':2})
    p.x = 10
    p.c = 100
    print(p.x, p.c)

    """----------- OUT PUT RESULTS --------------"""
    print("----------- OUT PUT RESULTS --------------")
    p.getResults()

    """----------- MYSQL --------------"""
    print("----------- MYSQL --------------")
    p._connected()
    p._mysqlTest()
    p._close()

    """----------- PARCE URL --------------"""
    print("----------- PARCE INIT --------------")
    url = p.getUrlValue()
    if(url):
        p.setUrl(url)
    else:
        p.setUrl()

    # =================== SAVE MYSQL ==============
    p._connected()
    if(url):
        psId = p.saveSites(url)
        print("PSID: ", psId)
    p._close()

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

    h3 = bhtml.find_all('h3')
    print("- OUTPUT <H3> (len:{0})-".format( len(h3) ))
    for _h3 in h3:
        print(_h3)

    h4 = bhtml.find_all('h4')
    print("- OUTPUT <H4> (len:{0})-".format( len(h4) ))
    for _h4 in h4:
        print(_h4)

    a = bhtml.find_all('a')
    print("- OUTPUT <a> (len:{0})-".format( len(a) ))

    i = 1
    _resA = []

    for _a in a:
        if(_a.get('href') != "#"):
            _resA.append(_a.get('href'))
            print('.', end=' ')
            if(i == len(a)):
                print('\n')
                print(_resA)
        #print(_a)
        #print(_a.get('href'))
        i+=1


    #print("----------------INIT PARCER FEAD ---------------");

    #phtml.feed(p.getUrl())
    #phtml.close()
    #p.parce()

    """----------- OK LOAD MAIN --------------"""
    print("--END LOAD MAIN--")


if __name__ == '__main__':
    main()

# r = redis.StrictRedis(host="127.0.0.1",port=6379,db=0)
# if r.set("test",10):
#     print( r.get("test") )
#
# r.set("test", 11)
# print(r.get("test"))

__version__ = '0.1'
