# -*- coding = utf-8 -*-
# @Time : 2021/5/12 20:42
# @Author : 刘正阳
# @File : center.py
# @Software : PyCharm
'''
窗口的居中操作，使用的函数默认为center()方法，返回一个基于当前屏幕的x,y坐标
'''

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')#
        self.show()

    def center(self):#实现对话框居中的方法

        qr = self.frameGeometry()#生成一个模拟对象，得到主窗口的大小
        #print(qr)
        #QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小
        cp = QDesktopWidget().availableGeometry().center()#获取显示器的分辨率，并得到中点位置
        qr.moveCenter(cp)#然后把自己窗口的中心点位置放到qr的中心点
        self.move(qr.topLeft())#然后把窗口的左上角坐标设置为qr的矩形左上角的坐标，完成窗口居中。
        #self.moveCenter(cp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())