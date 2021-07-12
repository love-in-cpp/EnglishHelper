# -*- coding = utf-8 -*-
# @Time : 2021/6/1 23:50
# @Author : 刘正阳
# @File : who is sender.py
# @Software : PyCharm
'''
重写事件以及追寻事件源
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        text = QLineEdit('abc',self)
        text.move(30, 100)

        btn1.clicked.connect(
            )
        '''
        按钮点击后实现文本框更新效果
        
        '''
        btn2.clicked.connect(self.buttonClicked)

        # self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        #self.statusBar().showMessage(sender.text() + ' was pressed')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
