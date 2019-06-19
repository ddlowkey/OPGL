#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'Frank.Ding'
#import hou
from stylesheet import qss
from UI import spBuilder_ui
import sys
import os
# if __name__ == '__main__':
#     pass
# else:
#     pass
#     print '1111'
#     sys.path.append('C:/Python27/Lib/site-packages')

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

if hasattr(sys, 'frozen'):
    basis = sys.executable
else:
    basis = sys.argv[0]

root_folder = os.path.split(basis)[0]

class MainWin(QMainWindow, spBuilder_ui.Ui_MainWindow):
    def __init__(self, parent=QApplication.activeWindow()):
        super(MainWin, self).__init__(parent)
        self.setup_UI(self)

        # self.stylesheet_string = ''
        # with open('%s/stylesheet/dark.txt' % root_folder.replace('\\', '/')) as stylesheet:
        #     for line in stylesheet:
        #         line.strip()
        #         self.stylesheet_string = self.stylesheet_string + line
        # self.setStyleSheet(self.stylesheet_string.replace('STYLESHEETPOSITION', root_folder.replace('\\', '/')))

        #self.setStyleSheet(qss.stylesheet)


    def setup_UI(self, parent=None):
        self.pt = parent or QMainWindow
        self.win = spBuilder_ui.Ui_MainWindow()
        self.win.setupUi(self.pt)
        size_window = self.pt.size()
        self.resize(size_window.width(), size_window.height())
        self.setCentralWidget(self.pt)
        icon = QIcon('.../logo.ico')
        self.setWindowIcon(icon)
        self.win_name = 'window name'
        self.setWindowTitle(self.win_name)


    def __init__UI__(self):
        self.lineEdit.installEventFilter(QLineEditDropHandler(self.lineEdit))
        pass

    def signal_connect(self):
        pass

class QLineEditDropHandler(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.DragEnter:
            event.accept()
        if event.type() == QEvent.Drop:
            md = event.mineData()
            if md.hasUrls():
                for url in md.urls():
                    obj.setText(url.toLocalFile())
                    break
            event.accept()
        return QObject.eventFilter(self, obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()
    app.exec_()

