#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Frank.Ding"

style_dict = {'DARKEST_COLOR': 'rgb(55, 55, 55)',
              'GRAY_COLOR': 'rgb(70, 70, 70)',
              'BUTTON_COLOR': 'rgb(100, 100, 100)',
              'BORDER_COLOR': 'rgb(85, 85, 85)',
              'BRIGHT_COLOR': 'rgb(110, 110, 110)',
              'LIGHT_COLOR': 'rgb(150, 150, 150)',
              'FONT_COLOR': 'rgb(200, 200, 200)',
              'BORDER_WIDTH': '0.5px',
              'BORDER_RADIUS': '3px',
              }

style = """
QMainWindow{
    background-color: GRAY_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;   
}

QLineEdit{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QListWidget{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QPushButton{
    color: DARKEST_COLOR;
    background-color: BUTTON_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BRIGHT_COLOR;
}

QPushButton:hover{
    color: FONT_COLOR;
    background-color: BRIGHT_COLOR;
}

QPushButton:pressed{
    color: FONT_COLOR;
    background-color: BUTTON_COLOR;
}

QTextEdit{
    color: FONT_COLOR;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QLabel{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
}

QLabel#label_image{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QScrollBar{
    background: GRAY_COLOR;
    margin: 20.5px 0 20.5px 0;
}

QScrollBar::handle{
    background: GRAY_COLOR;
    min-height: 20px;
}

QScrollBar::add-line{
    background: GRAY_COLOR;
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line{
    background: GRAY_COLOR;
    height: 20px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow, QScrollBar::down-arrow{
    width: 0px;
    height: 0px;
    background: BRIGHT_COLOR;
}

QScrollBar::add-page, QScrollBar::sub-page{
    background: BORDER_COLOR;
}

QScrollBar::handle:hover, QScrollBar::add-line:hover, QScrollBar::sub-line:hover{
    background: BRIGHT_COLOR;
}

QScrollBar::handle:pressed, QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed{
    background: GRAY_COLOR;
}

"""

def get_stylesheet(text=style):
    for key in style_dict:
        text = text.replace(key, style_dict.get(key))
    return text
