#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os

__absPath__ = os.path.dirname(__file__)

os.system("python" + __absPath__.replace('/', '\\') + "\\setup.py py2exe --include sip")