# -*- coding = utf-8 -*-
# @Time : 2021/7/3 18:57
# @Author : 刘正阳
# @File : note.py
# @Software : PyCharm
'''
信号和槽机制学习
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

# 主界面
class MainWindow(QMainWindow):

    def closeEvent(self,e)->None:
        # 如果文档没有修改
        if not text.document().isModified():
            return
        answer = QMessageBox.question(window,'警告','关闭之前是否保存文件',QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel)
        if  QMessageBox.Save:
            save()
        elif QMessageBox.Cancel:
            e.ignore()

app =QApplication([])
app.setApplicationName('文本编辑器')
text = QPlainTextEdit()
window = MainWindow()
window.setMinimumSize(800,600)
window.setCentralWidget(text)

#菜单项的添加
menu = window.menuBar().addMenu('文件')

#文件路径变量
file_path = None
#打开
open_action = QAction('打开')
def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window,"open")[0]
    if path:
        text.setPlainText('123')
        file_path = path

open_action.setShortcut(QKeySequence.Open)
open_action.triggered.connect(open_file)
menu.addAction(open_action)

#保存
save_action = QAction('保存')

def save():
    if file_path is None:
        pass
    else:
        with open (file_path,'w') as f:
            f.write(text.toPlainText())
            text.document().setModified(False)

save_action.setShortcut(QKeySequence.Save)
save_action.triggered.connect(save)
menu.addAction(save_action)

save_as_action = QAction('另存为')

#另存为
def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window,'另存为')[0]
    if path:
        file_path = path
        save()

save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)
#分隔线
menu.addSeparator()

#退出
exit_action = QAction("退出")
exit_action.setShortcut(QKeySequence.Close)
exit_action.triggered.connect(window.close)
menu.addAction(exit_action)

#帮助
help = window.menuBar().addMenu('帮助')
helpaction = QAction('关于')
def show_action():
    about_text = '这是一个简易的文本编辑器 \n版本1.0'
    QMessageBox.about(window,'说明',about_text)

helpaction.triggered.connect(show_action)
help.addAction(helpaction)

#点击叉号

window.show()
app.exec_()