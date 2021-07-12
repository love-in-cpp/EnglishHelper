# -*- coding = utf-8 -*-
# @Time : 2021/5/12 20:41
# @Author : 刘正阳
# @File : messagebox.py
# @Software : PyCharm
'''
事件触发的确认操作，MessageBox,不能改变事件本身内容
'''
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):#继承自event，父级组件为self
    #关闭QWidget会产生一个QCloseEvent，改变控件的默认行为，就是替换掉默认事件的处理
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
    #创建一个消息框，上面有俩按钮：Yes 和 No 第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框
    #第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。
    #返回值在变量reply里

    #判断返回值，如果点击的是yes，就关闭组件和应用，否则就忽略关闭事件。
        if reply == QMessageBox.Yes:
            event.accept() #执行点击接受的操作，和原窗口的事件相互独立,默认为忽略。
        else:
            event.ignore()
    #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())