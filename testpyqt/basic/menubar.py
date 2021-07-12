# -*- coding = utf-8 -*-
# @Time : 2021/6/1 16:29
# @Author : 刘正阳
# @File : menubar.py
# @Software : PyCharm

import sys
from PyQt5.QtWidgets import QWidget, QAction, qApp, QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class Example(QMainWindow,QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        #exitAction.setToolTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        exitAction1 = QAction(QIcon('exit.png'), 'Exit', self)
        self.statusBar()

        menubar = self.menuBar()
        menubar.setToolTip('123')
        fileMenu = menubar.addMenu('File')
        #fileMenu.setToolTip('123')

        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction1)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())