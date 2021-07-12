# -*- coding = utf-8 -*-
# @Time : 2021/5/12 19:15
# @Author : 刘正阳
# @File : 面向过程.py
# @Software : PyCharm

'''
面向过程
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
#QtWidgets 模块包含了最基本的组件

if __name__ == '__main__':
    app = QApplication(sys.argv)# 每个PyQt5应用都必须创建一个应用对象
    w = QWidget()#默认情况下构造器是没有父级的，没有父级的构造器被称为窗口
    w.resize(250, 150)#resize()方法能改变控件大小
    w.move(300, 300)#move()是修改控件位置的方法。原点左上角
    w.setWindowTitle('Simple')#标题
    w.show()#能让控件在桌面上显示出来

    sys.exit(app.exec_())#监听的主循环结束，传入的是应用对象