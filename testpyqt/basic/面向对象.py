# -*- coding = utf-8 -*-
# @Time : 2021/5/12 19:31
# @Author : 刘正阳
# @File : 面向对象.py
# @Software : PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
'''
面向对象
'''

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 300, 220)#x,y,width,height
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)#创建应用对象，进入进程循环


    ex = Example()#创建类的实例化对象


    sys.exit(app.exec_())#销毁应用对象，退出主进程循环