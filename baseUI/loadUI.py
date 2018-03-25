# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import maya.OpenMayaUI as OpenMayaUI
import xml.etree.ElementTree as xml
from cStringIO import StringIO

try:
    from PySide import QtGui, QtCore
    import pysideuic
    import shiboken
except:
    from PySide2 import QtGui, QtCore, QtWidgets
    import pyside2uic
    import shiboken2

def current_path():
    return os.path.dirname(os.path.realpath(__file__))

def wrapInstance(widget):
    '''
    Convert maya UI to Qt object
    :param widget:
    :return:
    '''
    if isinstance(widget, basestring):
        widget = OpenMayaUI.MQtUtil.findWindow(widget)
    try:
        output = shiboken.wrapInstance(long(widget), QtGui.QWidget)
    except:
        output = shiboken2.wrapInstance(long(widget), QtWidgets.QWidget)

    return output

def getMayaWindow():
    maya_window = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(maya_window)

def loadUiType(uiFile):
    """
    Pyside "loadUiType" command like PyQt4 has one, so we have to convert the
    ui file to py code in-memory first and then execute it in a special frame
    to retrieve the form_class.
    """
    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}
        try:
            pysideuic.compileUi(f, o, indent=0)
        except:
            pyside2uic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        # Fetch the base_class and form class based on their type
        # in the xml from designer
        form_class = frame['Ui_%s' % form_class]
        try:
            base_class = eval('QtGui.%s' % widget_class)
        except:
            base_class = eval('QtWidgets.%s' % widget_class)

    return form_class, base_class