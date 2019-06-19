#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from distutils.core import setup
import py2exe, sys, os

sys.path.append('py2exe')

__absPath__ = os.path.dirname(__file__)

DATA = [(   'imageformats',
        [   'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qjpeg.dll'
            'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qgif.dll'
            'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qico.dll'
            'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qtga.dll'
            'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qsvg.dll'
            'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qtiff.dll'
            'C:/Python27/Lib/site-packages/PyQt5/plugins/imageformats/qwbmp.dll'])]

setup(options={'py2exe':{"includes": ["sip"]}},
      windows=[{'script': 'main.py', 'icon_resources': [(0, './icon/main.ico')]}],
      data_files=DATA,
      zipfile=None)