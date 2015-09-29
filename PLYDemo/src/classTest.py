#! /usr/bin/env python3.4
from math import *
import sys
import os

class worker_pay:
    version = "1.2.4"
    
    def __init__(self):
        self.data = {}

    def add_worker(self,name,pay):
        self.data[name] = pay

    def list_worker(self,name):
        return self.data[name]

    def list_all(self):
        return self.data.keys()