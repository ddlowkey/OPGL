#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'Frank.Ding'

#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import sys
import os
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from UI import spBuilder_ui
reload(spBuilder_ui)

class mainWin(QMainWindow):
    def __init__(self, parent=None, **kwargs):
        super(mainWin, self).__init__(parent, **kwargs)
        self.setup_ui(parent)


    def setup_ui(self, parent=None):
        self.pt = parent or QMainWindow()
        self.win = spBuilder_ui.Ui_MainWindow()
        self.win.setupUi(self.pt)
        size_ = self.pt.size()
        self.resize(size_)
        self.setCentralWidget(self.pt)
        self.setWindowTitle('test')

class myThread(QThread):
    def __init__(self, *args):
        super(myThread, self).__init__()
        if args:
            self.a = args[0]
            self.b = args[1]

    def run(self):
        print self.a
        print self.b

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = myThread('111', '222')
    m.run()
    w = mainWin()
    w.show()
    sys.exit(app.exec_())