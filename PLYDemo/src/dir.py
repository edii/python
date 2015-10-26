#! /usr/bin/env python3.4
from math import *
import sys
from subprocess import call 
import os
import io

class ParceError(Exception):
    def _call_(self):
        print(self)
        return True

DIR_PATH = './test/'
FILE_NAME = 'test.txt'

f = False

if os.path.isdir(DIR_PATH) == False:
    call(['mkdir','test'])

if os.path.exists(DIR_PATH+FILE_NAME) == False:
    f = open(DIR_PATH+FILE_NAME, mode = 'w+', encoding='utf-8')
else:
    f = open(DIR_PATH+FILE_NAME, mode = 'r', encoding='utf-8')
    
f.seek(0,2)

if f.readable():
    raise ParceError
else:
    f.write('0. Blaaaaaaaaaaa,\n')
    f.write('1. Blaaaaaaaaaaa,\n')
    f.write('2. Blaaaaaaaaaaa,\n')

try:
    print('Writeble only...')
except ParceError:
    print('Read only..\n')

#if mode == 'r':
#    raise NotImplementedError

#try:
#    f.write('0. Blaaaaaaaaaaa,\n')
#    f.write('1. Blaaaaaaaaaaa,\n')
#    f.write('2. Blaaaaaaaaaaa,\n')
#except IOError:
#    print('Read only..\n')
    
print('Init...\n')
if f:
    print('File '+FILE_NAME+'::READ\n')
    f.seek(0,0)
    print(f.read())

f.close()
print('End..')
#call(['ls','-al'])

