from login import *
from show import *
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
import resource_rc
import os
from PIL import Image

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import argparse
import time
from pathlib import Path
import shutil
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

# pyuic5 show.ui -o show.py
# pyrcc5 resourse.qrc -o resource_rc.py

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi((self))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.win = InterfaceWindow()
        self.win.hide()
        self.ui.pushButton.clicked.connect(self._goto_inte)
        self.show()

    def _goto_inte(self):
        account=self.ui.lineEdit.text()
        password=self.ui.lineEdit_2.text()
        if account == "ysj" and  password=="123":
            # self.win = InterfaceWindow()
            self.win.show()
            self.close()
        else:
            pass

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class InterfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InterfaceWindow()
        self.ui.setupUi((self))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.getfile)
        self.ui.pushButton_3.clicked.connect(self.getVideo)
        self.show()

    def getVideo(self):
        self.fname, _ = QFileDialog.getOpenFileName(self, 'Open file',r'Y:\Git_Clone\YOLOP\inference\videos',"Image files (*.mp4)")
        print(self.fname)
        self.fname = self.fname.replace('\\', '/')
        str = (r'python tools/demo.py --source ' + self.fname + ' --device 0')  # + '--exist-ok '
        os.system(str)

        path = os.listdir(r'runs\detect\exp')
        s = path[0]
        pathend = r'runs\detect\exp' + '\\' + s
        #I = Image.open(pathend)
        #I.show()

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(None, 'Open file',r'Y:\Git_Clone\YOLOP\inference\images',"image files(*.jpg *.png)", None, QFileDialog.DontUseNativeDialog)
        print(fname)
        self._fname=fname.replace('\\','/')
        str = (r'python tools/demo.py --source '+self._fname) #+ '--exist-ok '
        os.system(str)

        # path = os.listdir(r'runs\detect\exp')
        # s = path[0]
        # pathend = r'runs\detect\exp' + '\\' + s
        #I = Image.open(pathend)
        #I.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # win = InterfaceWindow()
    win = LoginWindow()
    sys.exit(app.exec_())