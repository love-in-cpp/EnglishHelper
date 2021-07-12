# -*- coding = utf-8 -*-
# @Time : 2021/5/12 19:44
# @Author : 刘正阳
# @File : tooltip.py
# @Software : PyCharm


import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont
'''
面向对象编程最重要的三个部分是类(class)、数据和方法。我们创建了一个类的调用，这个类继承自QWidget。
这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。
super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法。
'''

'''
鼠标静止的静态消息展示
'''
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #是否作用在所有提示框上？
        QToolTip.setFont(QFont('SansSerif', 10))#为应用创建的提示框，以字体对象创建提示框

        self.setToolTip('This is a <b>QWidget</b> widget')#<b>加粗字体，可以使用富文本格式的内容

        btn = QPushButton('Button', self)#传入self,传入按钮名，构造按钮
        btn.setToolTip('This is a <b>QPushButton</b> widget')#初始化提示框内容
        btn.resize(btn.sizeHint())#默认的按钮大小由sizeHint()方法返回
        btn.move(50, 50)#设置按钮初始化位置

        self.setGeometry(300, 300, 300, 200)#设置窗口位置
        self.setWindowTitle('Tooltips')#标题
        self.show()#展示


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())