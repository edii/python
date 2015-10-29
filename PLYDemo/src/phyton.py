#! /usr/bin/env python3.4
from math import *
import sys
import os

try:
    import classTest
except ImportError:
    pass

def ask_ok(promt, resipe = 4, msg = "Yes or no, asked"):
    while True:
        ok = input(promt)
        if ok in ('y', 'yes'): return True
        if ok in ('n', 'no'): return False
        resipe -= 1
        if resipe < 0:
            raise IOError('refusenik error!')
        print(msg)

#print (sys.argv)
#print(sys.argv[1])
#print(os.system("date"))

x = classTest.worker_pay()
x.add_worker("george", 3000)
x.add_worker("frank", 2500)
x.list_all()

ask_ok('Doy want start?')