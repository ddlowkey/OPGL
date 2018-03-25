# !/usr/bin/python
# -*- coding: utf-8 -*-

import pymel.core as pm

# Name of the global variable for the Maya window
MainMayaWindow = pm.language.melGlobals['gMainWindow']

# Build a menu and parent under the Maya Window
customMenu = pm.menu('Custom Menu', parent=MainMayaWindow, tearOff=1)

# Build a menu item and parent under the 'customMenu'
firstItem = pm.menuItem(label="first level", subMenu=1, command="print 'first'", parent=customMenu)
pm.menuItem(label="Base Window", command='import generic; reload(generic); generic.baseWidget_show()', parent=firstItem)