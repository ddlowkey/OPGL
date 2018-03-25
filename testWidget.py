# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import baseUI.loadUI as loadUI
from OpenGL.GL import *
try:
    from PySide import QtGui, QtCore, QtOpenGL
    import pysideuic
    import shiboken
except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets, QtOpenGL
    import pyside2uic
    import shiboken2

ui_base, ui_form = loadUI.loadUiType(os.path.join(loadUI.current_path(), 'baseWidget_ui_v001.ui'))

class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.xsize = 512
        self.ysize = 512

    def initializeGL():
        glClearColor()

    def printGL():
        glClearColor

    def resizeGL():
        glClearColor

class baseWidget_class(ui_base, ui_form):
    def __init__(self, parent=loadUI.getMayaWindow()):
        super(baseWidget_class, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    gui = baseWidget_class()
    gui.show()