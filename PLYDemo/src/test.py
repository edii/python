import os
from math import *
import sys
import subprocess

class Parent(dict):
    # def __init__(self, par):
    #      print( par + 1 )

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]

    # def getParent(self, par):
    #     return par + 10

# class Child(Parent):
#     def __init__(self, cpar):
#       Parent.__init__(self, cpar)
#
#     def getChild(self,cpar):
#         return cpar + 11
#
# x = Child(1)
# print(x.getParent(2))
# print(x.getChild(3))

x = Parent()
x.test = 10
print(x.test)