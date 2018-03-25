# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import shutil
import maya.utils as mutils

sys.path.append(r'D:\pipeline\tools\maya\baseUI')

def import_mainMenu():
    import mainMenu

mutils.executeDeferred(import_mainMenu)
shutil.copyfile(r'D:\pipeline\tools\maya\baseUI\userSetup.py', r'C:\Users\Ding\Documents\maya\2017\scripts\userSetup.py')