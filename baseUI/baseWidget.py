# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import loadUI

ui_base, ui_form = loadUI.loadUiType(os.path.join(loadUI.current_path(), 'baseWidget_ui_v001.ui'))

class baseWidget_class(ui_base, ui_form):
    def __init__(self, parent=loadUI.getMayaWindow()):
        super(baseWidget_class, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    gui = baseWidget_class()
    gui.show()
