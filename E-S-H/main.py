# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 612)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wordButton = QtWidgets.QPushButton(self.centralwidget)
        self.wordButton.setGeometry(QtCore.QRect(60, 20, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.wordButton.setFont(font)
        self.wordButton.setObjectName("wordButton")
        self.egButton = QtWidgets.QPushButton(self.centralwidget)
        self.egButton.setGeometry(QtCore.QRect(60, 110, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.egButton.setFont(font)
        self.egButton.setObjectName("egButton")
        self.toButton = QtWidgets.QPushButton(self.centralwidget)
        self.toButton.setGeometry(QtCore.QRect(60, 200, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.toButton.setFont(font)
        self.toButton.setObjectName("toButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(170, 10, 841, 511))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.wdtabWidget = QtWidgets.QTabWidget(self.tab_3)
        self.wdtabWidget.setGeometry(QtCore.QRect(0, 0, 841, 491))
        self.wdtabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.wdtabWidget.setObjectName("wdtabWidget")
        self.addwdTab = QtWidgets.QWidget()
        self.addwdTab.setObjectName("addwdTab")
        self.label = QtWidgets.QLabel(self.addwdTab)
        self.label.setGeometry(QtCore.QRect(40, 70, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.addwdTab)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.addwdTab)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 72, 15))
        self.label_3.setObjectName("label_3")
        self.wpolineEdit = QtWidgets.QLineEdit(self.addwdTab)
        self.wpolineEdit.setGeometry(QtCore.QRect(100, 200, 151, 41))
        self.wpolineEdit.setObjectName("wpolineEdit")
        self.label_4 = QtWidgets.QLabel(self.addwdTab)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 72, 15))
        self.label_4.setObjectName("label_4")
        self.wcolineEdit = QtWidgets.QLineEdit(self.addwdTab)
        self.wcolineEdit.setGeometry(QtCore.QRect(100, 130, 151, 41))
        self.wcolineEdit.setObjectName("wcolineEdit")
        self.label_5 = QtWidgets.QLabel(self.addwdTab)
        self.label_5.setGeometry(QtCore.QRect(370, 70, 72, 15))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.add_word_Button = QtWidgets.QPushButton(self.addwdTab)
        self.add_word_Button.setGeometry(QtCore.QRect(140, 410, 91, 31))
        self.add_word_Button.setObjectName("add_word_Button")
        self.wnolineEdit = QtWidgets.QLineEdit(self.addwdTab)
        self.wnolineEdit.setGeometry(QtCore.QRect(100, 60, 151, 41))
        self.wnolineEdit.setObjectName("wnolineEdit")
        self.word_table = QtWidgets.QTableWidget(self.addwdTab)
        self.word_table.setGeometry(QtCore.QRect(290, 60, 531, 311))
        self.word_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.word_table.setGridStyle(QtCore.Qt.SolidLine)
        self.word_table.setObjectName("word_table")
        self.word_table.setColumnCount(4)
        self.word_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(3, item)
        self.word_table.verticalHeader().setVisible(False)
        self.label_11 = QtWidgets.QLabel(self.addwdTab)
        self.label_11.setGeometry(QtCore.QRect(500, 30, 72, 15))
        self.label_11.setObjectName("label_11")
        self.wtolineEdit = QtWidgets.QLineEdit(self.addwdTab)
        self.wtolineEdit.setGeometry(QtCore.QRect(100, 270, 151, 41))
        self.wtolineEdit.setObjectName("wtolineEdit")
        self.reset_word_Button = QtWidgets.QPushButton(self.addwdTab)
        self.reset_word_Button.setGeometry(QtCore.QRect(460, 410, 91, 31))
        self.reset_word_Button.setObjectName("reset_word_Button")
        self.wdtabWidget.addTab(self.addwdTab, "")
        self.editwbTab = QtWidgets.QWidget()
        self.editwbTab.setObjectName("editwbTab")
        self.label_12 = QtWidgets.QLabel(self.editwbTab)
        self.label_12.setGeometry(QtCore.QRect(280, 160, 72, 15))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.editwbTab)
        self.label_13.setGeometry(QtCore.QRect(150, 60, 72, 15))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.editwbTab)
        self.label_14.setGeometry(QtCore.QRect(280, 230, 72, 15))
        self.label_14.setObjectName("label_14")
        self.ewnolineEdit = QtWidgets.QLineEdit(self.editwbTab)
        self.ewnolineEdit.setGeometry(QtCore.QRect(250, 50, 151, 41))
        self.ewnolineEdit.setObjectName("ewnolineEdit")
        self.ewpolineEdit = QtWidgets.QLineEdit(self.editwbTab)
        self.ewpolineEdit.setGeometry(QtCore.QRect(340, 220, 151, 41))
        self.ewpolineEdit.setObjectName("ewpolineEdit")
        self.ewtolineEdit = QtWidgets.QLineEdit(self.editwbTab)
        self.ewtolineEdit.setGeometry(QtCore.QRect(340, 290, 151, 41))
        self.ewtolineEdit.setObjectName("ewtolineEdit")
        self.ewcolineEdit = QtWidgets.QLineEdit(self.editwbTab)
        self.ewcolineEdit.setGeometry(QtCore.QRect(340, 150, 151, 41))
        self.ewcolineEdit.setObjectName("ewcolineEdit")
        self.label_15 = QtWidgets.QLabel(self.editwbTab)
        self.label_15.setGeometry(QtCore.QRect(280, 300, 72, 15))
        self.label_15.setObjectName("label_15")
        self.select_word_Button = QtWidgets.QPushButton(self.editwbTab)
        self.select_word_Button.setGeometry(QtCore.QRect(590, 50, 93, 28))
        self.select_word_Button.setObjectName("select_word_Button")
        self.del_word_Button = QtWidgets.QPushButton(self.editwbTab)
        self.del_word_Button.setGeometry(QtCore.QRect(140, 380, 93, 28))
        self.del_word_Button.setObjectName("del_word_Button")
        self.upd_word_Button = QtWidgets.QPushButton(self.editwbTab)
        self.upd_word_Button.setGeometry(QtCore.QRect(660, 380, 93, 28))
        self.upd_word_Button.setObjectName("upd_word_Button")
        self.wdtabWidget.addTab(self.editwbTab, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 841, 491))
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.label_7 = QtWidgets.QLabel(self.tab_10)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 72, 15))
        self.label_7.setObjectName("label_7")
        self.enolineEdit = QtWidgets.QLineEdit(self.tab_10)
        self.enolineEdit.setGeometry(QtCore.QRect(90, 40, 151, 21))
        self.enolineEdit.setObjectName("enolineEdit")
        self.label_8 = QtWidgets.QLabel(self.tab_10)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 72, 15))
        self.label_8.setObjectName("label_8")
        self.label_16 = QtWidgets.QLabel(self.tab_10)
        self.label_16.setGeometry(QtCore.QRect(10, 260, 72, 15))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_10)
        self.label_17.setGeometry(QtCore.QRect(580, 30, 72, 15))
        self.label_17.setObjectName("label_17")
        self.eg_table = QtWidgets.QTableWidget(self.tab_10)
        self.eg_table.setGeometry(QtCore.QRect(410, 60, 421, 401))
        self.eg_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.eg_table.setGridStyle(QtCore.Qt.SolidLine)
        self.eg_table.setColumnCount(3)
        self.eg_table.setObjectName("eg_table")
        self.eg_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.eg_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.eg_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.eg_table.setHorizontalHeaderItem(2, item)
        self.eg_table.verticalHeader().setVisible(False)
        self.add_eg_Button = QtWidgets.QPushButton(self.tab_10)
        self.add_eg_Button.setGeometry(QtCore.QRect(70, 410, 93, 28))
        self.add_eg_Button.setObjectName("add_eg_Button")
        self.ecotextEdit = QtWidgets.QTextEdit(self.tab_10)
        self.ecotextEdit.setGeometry(QtCore.QRect(70, 90, 321, 151))
        self.ecotextEdit.setObjectName("ecotextEdit")
        self.etotextEdit = QtWidgets.QTextEdit(self.tab_10)
        self.etotextEdit.setGeometry(QtCore.QRect(70, 250, 321, 151))
        self.etotextEdit.setObjectName("etotextEdit")
        self.reset_eg_Button = QtWidgets.QPushButton(self.tab_10)
        self.reset_eg_Button.setGeometry(QtCore.QRect(250, 410, 91, 31))
        self.reset_eg_Button.setObjectName("reset_eg_Button")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.egtableView = QtWidgets.QTableView(self.tab_11)
        self.egtableView.setGeometry(QtCore.QRect(0, 0, 841, 431))
        self.egtableView.setObjectName("egtableView")
        self.egtableView.horizontalHeader().setCascadingSectionResizes(False)
        self.egtableView.horizontalHeader().setDefaultSectionSize(200)
        self.egtableView.verticalHeader().setVisible(False)
        self.egtableView.verticalHeader().setDefaultSectionSize(120)
        self.del_eg_Button = QtWidgets.QPushButton(self.tab_11)
        self.del_eg_Button.setGeometry(QtCore.QRect(510, 430, 93, 28))
        self.del_eg_Button.setObjectName("del_eg_Button")
        self.upd_eg_Button = QtWidgets.QPushButton(self.tab_11)
        self.upd_eg_Button.setGeometry(QtCore.QRect(150, 430, 93, 28))
        self.upd_eg_Button.setObjectName("upd_eg_Button")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.src_tra_textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.src_tra_textEdit.setGeometry(QtCore.QRect(80, 0, 761, 201))
        self.src_tra_textEdit.setObjectName("src_tra_textEdit")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(0, 100, 72, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 72, 15))
        self.label_10.setObjectName("label_10")
        self.dst_tra_textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.dst_tra_textEdit.setGeometry(QtCore.QRect(80, 280, 761, 191))
        self.dst_tra_textEdit.setObjectName("dst_tra_textEdit")
        self.tra_Button = QtWidgets.QPushButton(self.tab_5)
        self.tra_Button.setGeometry(QtCore.QRect(400, 210, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tra_Button.setFont(font)
        self.tra_Button.setObjectName("tra_Button")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(90, 50, 72, 15))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_6)
        self.label_19.setGeometry(QtCore.QRect(90, 220, 72, 15))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_6)
        self.label_20.setGeometry(QtCore.QRect(90, 170, 72, 15))
        self.label_20.setObjectName("label_20")
        self.wtopTextEdit = QtWidgets.QPlainTextEdit(self.tab_6)
        self.wtopTextEdit.setGeometry(QtCore.QRect(150, 160, 681, 91))
        self.wtopTextEdit.setObjectName("wtopTextEdit")
        self.label_21 = QtWidgets.QLabel(self.tab_6)
        self.label_21.setGeometry(QtCore.QRect(80, 300, 72, 15))
        self.label_21.setObjectName("label_21")
        self.wtoeTextEdit = QtWidgets.QPlainTextEdit(self.tab_6)
        self.wtoeTextEdit.setGeometry(QtCore.QRect(150, 290, 681, 181))
        self.wtoeTextEdit.setObjectName("wtoeTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_6)
        self.pushButton.setGeometry(QtCore.QRect(300, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.select_wtoe_Button = QtWidgets.QPushButton(self.tab_6)
        self.select_wtoe_Button.setGeometry(QtCore.QRect(290, 30, 93, 28))
        self.select_wtoe_Button.setObjectName("select_wtoe_Button")
        self.wtoelineEdit = QtWidgets.QLineEdit(self.tab_6)
        self.wtoelineEdit.setGeometry(QtCore.QRect(150, 40, 113, 21))
        self.wtoelineEdit.setObjectName("wtoelineEdit")
        self.wpo_textBrowser = QtWidgets.QTextBrowser(self.tab_6)
        self.wpo_textBrowser.setGeometry(QtCore.QRect(150, 100, 111, 31))
        self.wpo_textBrowser.setObjectName("wpo_textBrowser")
        self.label_22 = QtWidgets.QLabel(self.tab_6)
        self.label_22.setGeometry(QtCore.QRect(90, 110, 72, 15))
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.wetableView = QtWidgets.QTableView(self.tab)
        self.wetableView.setGeometry(QtCore.QRect(0, 0, 621, 481))
        self.wetableView.setObjectName("wetableView")
        self.wetableView.horizontalHeader().setDefaultSectionSize(200)
        self.wetableView.verticalHeader().setVisible(False)
        self.wetableView.verticalHeader().setDefaultSectionSize(30)
        self.reshow_we_Button = QtWidgets.QPushButton(self.tab)
        self.reshow_we_Button.setGeometry(QtCore.QRect(680, 120, 93, 28))
        self.reshow_we_Button.setObjectName("reshow_we_Button")
        self.upd_we_Button = QtWidgets.QPushButton(self.tab)
        self.upd_we_Button.setGeometry(QtCore.QRect(680, 280, 93, 28))
        self.upd_we_Button.setObjectName("upd_we_Button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.memo_wd_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.memo_wd_textBrowser.setGeometry(QtCore.QRect(330, 100, 91, 41))
        self.memo_wd_textBrowser.setObjectName("memo_wd_textBrowser")
        self.comeon_Button = QtWidgets.QPushButton(self.tab_2)
        self.comeon_Button.setGeometry(QtCore.QRect(360, 20, 141, 61))
        self.comeon_Button.setObjectName("comeon_Button")
        self.icant_Button = QtWidgets.QPushButton(self.tab_2)
        self.icant_Button.setGeometry(QtCore.QRect(230, 440, 93, 28))
        self.icant_Button.setObjectName("icant_Button")
        self.memo_answer_textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.memo_answer_textEdit.setGeometry(QtCore.QRect(200, 340, 441, 71))
        self.memo_answer_textEdit.setObjectName("memo_answer_textEdit")
        self.its_easy_Button = QtWidgets.QPushButton(self.tab_2)
        self.its_easy_Button.setGeometry(QtCore.QRect(360, 440, 93, 28))
        self.its_easy_Button.setObjectName("its_easy_Button")
        self.memo_eg_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.memo_eg_textBrowser.setGeometry(QtCore.QRect(200, 180, 441, 111))
        self.memo_eg_textBrowser.setObjectName("memo_eg_textBrowser")
        self.look_look_Button = QtWidgets.QPushButton(self.tab_2)
        self.look_look_Button.setGeometry(QtCore.QRect(480, 440, 93, 28))
        self.look_look_Button.setObjectName("look_look_Button")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(240, 110, 72, 15))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(120, 230, 72, 15))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(101, 370, 81, 20))
        self.label_25.setObjectName("label_25")
        self.wto_Browser = QtWidgets.QTextBrowser(self.tab_2)
        self.wto_Browser.setGeometry(QtCore.QRect(420, 100, 121, 41))
        self.wto_Browser.setObjectName("wto_Browser")
        self.tabWidget.addTab(self.tab_2, "")
        self.weButton = QtWidgets.QPushButton(self.centralwidget)
        self.weButton.setGeometry(QtCore.QRect(60, 380, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.weButton.setFont(font)
        self.weButton.setObjectName("weButton")
        self.dicButton = QtWidgets.QPushButton(self.centralwidget)
        self.dicButton.setGeometry(QtCore.QRect(60, 290, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.dicButton.setFont(font)
        self.dicButton.setObjectName("dicButton")
        self.memo_Button = QtWidgets.QPushButton(self.centralwidget)
        self.memo_Button.setGeometry(QtCore.QRect(60, 470, 91, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.memo_Button.setFont(font)
        self.memo_Button.setObjectName("memo_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.wdtabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "英语学习助手"))
        self.wordButton.setText(_translate("MainWindow", "单词管理"))
        self.egButton.setText(_translate("MainWindow", "例句管理"))
        self.toButton.setText(_translate("MainWindow", "翻译"))
        self.label.setText(_translate("MainWindow", "单词号："))
        self.label_2.setText(_translate("MainWindow", "单词："))
        self.label_3.setText(_translate("MainWindow", "音标："))
        self.label_4.setText(_translate("MainWindow", "释义:"))
        self.add_word_Button.setText(_translate("MainWindow", "添加"))
        item = self.word_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "单词号"))
        item = self.word_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "单词"))
        item = self.word_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "音标"))
        item = self.word_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "释义"))
        self.label_11.setText(_translate("MainWindow", "单词表"))
        self.reset_word_Button.setText(_translate("MainWindow", "复位"))
        self.wdtabWidget.setTabText(self.wdtabWidget.indexOf(self.addwdTab), _translate("MainWindow", "添加单词"))
        self.label_12.setText(_translate("MainWindow", "单词："))
        self.label_13.setText(_translate("MainWindow", "单词号："))
        self.label_14.setText(_translate("MainWindow", "音标："))
        self.label_15.setText(_translate("MainWindow", "释义:"))
        self.select_word_Button.setText(_translate("MainWindow", "查找"))
        self.del_word_Button.setText(_translate("MainWindow", "删除"))
        self.upd_word_Button.setText(_translate("MainWindow", "修改"))
        self.wdtabWidget.setTabText(self.wdtabWidget.indexOf(self.editwbTab), _translate("MainWindow", "编辑单词"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.label_7.setText(_translate("MainWindow", "例句号："))
        self.label_8.setText(_translate("MainWindow", "例句："))
        self.label_16.setText(_translate("MainWindow", "翻译："))
        self.label_17.setText(_translate("MainWindow", "例句表"))
        item = self.eg_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "例句号"))
        item = self.eg_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "例句"))
        item = self.eg_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "翻译"))
        self.add_eg_Button.setText(_translate("MainWindow", "添加"))
        self.reset_eg_Button.setText(_translate("MainWindow", "复位"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "添加例句"))
        self.del_eg_Button.setText(_translate("MainWindow", "删除"))
        self.upd_eg_Button.setText(_translate("MainWindow", "刷新"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "编辑例句"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.label_9.setText(_translate("MainWindow", "自动检测："))
        self.label_10.setText(_translate("MainWindow", "中文："))
        self.tra_Button.setText(_translate("MainWindow", "👇"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.label_18.setText(_translate("MainWindow", "单词："))
        self.label_20.setText(_translate("MainWindow", "释义："))
        self.label_21.setText(_translate("MainWindow", "例句："))
        self.pushButton.setText(_translate("MainWindow", "🔊"))
        self.select_wtoe_Button.setText(_translate("MainWindow", "查询"))
        self.label_22.setText(_translate("MainWindow", "音标："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.reshow_we_Button.setText(_translate("MainWindow", "刷新视图"))
        self.upd_we_Button.setText(_translate("MainWindow", "更新数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page"))
        self.comeon_Button.setText(_translate("MainWindow", "试着来一个"))
        self.icant_Button.setText(_translate("MainWindow", "不会"))
        self.its_easy_Button.setText(_translate("MainWindow", "提交"))
        self.look_look_Button.setText(_translate("MainWindow", "看几个例句"))
        self.label_23.setText(_translate("MainWindow", "单词："))
        self.label_24.setText(_translate("MainWindow", "例句："))
        self.label_25.setText(_translate("MainWindow", "我的答案："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Page"))
        self.weButton.setText(_translate("MainWindow", "维护"))
        self.dicButton.setText(_translate("MainWindow", "词典"))
        self.memo_Button.setText(_translate("MainWindow", "记忆卡片"))
