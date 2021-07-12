# -*- coding = utf-8 -*-
# @Time : 2021/7/3 17:39
# @Author : 刘正阳
# @File : qt5demo.py
# @Software : PyCharm
import sys
from PyQt5.QtWidgets import *
import login
import test
if __name__ == '__main__':
    app=QApplication(sys.argv)

    dialog = QDialog()
    ui = login.Ui_LoginDialog()
    ui.setupUi(dialog)

    testDialog = QDialog()
    testui = test.Ui_Dialog()
    testui.setupUi(testDialog)

    dialog.show()
    testDialog.show()

    sys.exit(app.exec_())