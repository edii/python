#! /usr/bin/env python3.4
from math import *
import sys
import os
import subprocess
#import classTest

if sys.argv[1]:
   # print(sys.argv[1])
    subprocess.call(["git","pull"])
    subprocess.call(["git","commit", "-m", '"'+ sys.argv[1] +'"'])
    subprocess.call(["git","push", "origin", "master"])
   
    if sys.argv[2] and sys.argv[2] in ("dep"):
        try:
            if sys.argv[3]:
                project = sys.argv[3];
            else:
                project = "cs-pumpic-deploy"
        except IndexError:
            project = "cs-pumpic-deploy"

        subprocess.call(["/home/sergey/WebDeploy/"+project+"", "dep", "deploy"])
else:
    print("Enter commit git!")