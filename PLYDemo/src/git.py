#! /usr/bin/env python3.4
from math import *
import sys
import os
import subprocess
#import classTest

if sys.argv[1]:
    subprocess.call(["git","pull"])
    subprocess.call(["git","commit", "-m", '"'+ sys.argv[1] +'"'])
    subprocess.call(["git","push", "origin", "master"])
else:
    print("Enter commit git!")