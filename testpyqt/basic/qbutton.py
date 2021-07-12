# -*- coding = utf-8 -*-
# @Time : 2021/5/12 20:01
# @Author : 刘正阳
# @File : qbutton.py
# @Software : PyCharm
'''
按钮和事件
'''

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #创建一个继承自QPushButton的按钮。第一个参数是按钮的文本，第二个参数是
        #按钮的父级组件，这个例子中，父级组件就是我们创建的继承自Qwidget的Example类
        qbtn = QPushButton('Quit', self)#构造按钮
        #QCoreApplication 包含了事件的主循环，它能添加和删除所有的事件
        #instance()创建了它的一个实例
        #QcoreApplication是在Qapplication里创建的，点击事件 和 能终止进程并退出应用的
        #quit函数绑定在了一起，在发送者和接受者之间建立了通讯，发送者是按钮，接受者是应用对象
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())#默认大小
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)#
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())