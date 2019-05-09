#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from PyQt5 import uic
import os
import glob

def uicToPy(name):
    with open(str(name).replace('.ui', '.py'), 'w') as f:
        uic.compileUi(name, f)

if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.dirname(__file__))
    filepath = '{}/UI/*.ui'.format(dir_name)
    func = lambda x: uicToPy(x)
    map(func, glob.glob(filepath))
