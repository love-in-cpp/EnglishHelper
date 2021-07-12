# -*- coding = utf-8 -*-
# @Time : 2021/7/4 15:50
# @Author : 刘正阳
# @File : index.py
# @Software : PyCharm

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import sys
from main import Ui_MainWindow
from dbutil import MSSQL
import random

import http.client
import hashlib
import urllib
import random
import json
import re


signal = None
wxo = None
old_wxo = None

count = 0

sqls = MSSQL()
class MainApp(QMainWindow, Ui_MainWindow):

    # 定义构造方法
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui_change()
        self.handle_buttons()
        self.show_word()
        self.show_eg()

        self.tabWidget.setCurrentIndex(0)
        # 下面这几句不放最后程序会崩，不知道为什么，妈的
        # self.show_we()
        self.upd_eg()

    # UI变化处理
    def handle_ui_change(self):
        self.tabWidget.tabBar().setVisible(False)

    # 所有Button的消息与槽的通信
    def handle_buttons(self):
        self.wordButton.clicked.connect(self.open_word_tab)
        self.egButton.clicked.connect(self.open_eg_tab)
        self.toButton.clicked.connect(self.open_to_tab)
        self.dicButton.clicked.connect(self.open_dic_tab)
        self.weButton.clicked.connect(self.open_we_tab)

        self.add_word_Button.clicked.connect(self.add_word)
        self.reset_word_Button.clicked.connect(self.reset_word_text)
        self.select_word_Button.clicked.connect(self.select_word)
        self.upd_word_Button.clicked.connect(self.update_word)
        self.del_word_Button.clicked.connect(self.del_word)

        self.add_eg_Button.clicked.connect(self.add_eg)
        self.reset_eg_Button.clicked.connect(self.reset_eg_text)
        self.upd_eg_Button.clicked.connect(self.upd_eg)

        self.upd_we_Button.clicked.connect(self.creat_we_table)
        self.reshow_we_Button.clicked.connect(self.show_we)

        self.select_wtoe_Button.clicked.connect(self.select_wtoe)
        self.tra_Button.clicked.connect(self.traslation)

        self.comeon_Button.clicked.connect(self.memo_comeon)
        self.memo_Button.clicked.connect(self.open_memo_tab)
        self.icant_Button.clicked.connect(self.memo_icant)
        self.look_look_Button.clicked.connect(self.look_look_eg)
        self.its_easy_Button.clicked.connect(self.submit_my_answer)

    '''
    选项卡联动
    '''

    # 单词选项卡
    def open_word_tab(self):
        self.tabWidget.setCurrentIndex(0)
        self.wdtabWidget.setCurrentIndex(0)

    # 例句选项卡
    def open_eg_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)

    def open_to_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_dic_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def open_we_tab(self):
        self.tabWidget.setCurrentIndex(4)

    def open_memo_tab(self):
        self.tabWidget.setCurrentIndex(5)

    '''
    数据库处理
    '''
    '''
    单词处理
    '''

    # 添加单词记录
    def add_word(self):
        # 获取连接
        # sqls = MSSQL()
        cur = sqls.GetConnect()
        sql = "insert into word(单词号,单词,音标,释义) values(%s,%s,%s,%s)"
        # sql = "insert into word(单词号) values(%s)"
        wno = self.wnolineEdit.text()
        wco = self.wcolineEdit.text()
        wpo = self.wpolineEdit.text()
        wto = self.wtolineEdit.text()

        # 执行
        cur.execute(sql, (wno, wco, wpo, wto))
        # cur.execute(sql, (wno,))
        # 提交
        sqls.conn.commit()
        # 关闭
        sqls.conn.close()
        # 状态栏显示
        self.statusbar.showMessage('单词记录添加成功！')
        self.show_word()

    # 显示已有单词，并且添加完毕后可以直接看到
    def show_word(self):
        # sqls = MSSQL()
        cur = sqls.GetConnect()
        sql = "select * from word"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.word_table.setRowCount(0)
            self.word_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.word_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.word_table.rowCount()
                self.word_table.insertRow(row_position)

        sqls.conn.close()

    # 复位
    def reset_word_text(self):
        self.wtolineEdit.setText('')
        self.wpolineEdit.setText('')
        self.wcolineEdit.setText('')
        self.wnolineEdit.setText('')
        self.show_word()

    # 修改单词
    # 查找
    def select_word(self):

        global wxo
        global old_wxo
        global signal

        # sqls = MSSQL()
        cur = sqls.GetConnect()
        readyfind = True

        print(1111)

        if self.ewnolineEdit.text() != '':
            sql = "select 单词号,单词,音标,释义 from word where 单词号 =%s"
            old_wno = self.ewnolineEdit.text()
            print(wxo, old_wxo)
            cur.execute(sql, (old_wno,))

            wxo = '单词号'
            old_wxo = old_wno
            signal = 0
        elif self.ewcolineEdit.text() != '':
            sql = "select 单词号,单词,音标,释义 from word where 单词 =%s"
            old_wco = self.ewcolineEdit.text()
            cur.execute(sql, (old_wco,))
            wxo = '单词'
            old_wxo = old_wco
            signal = 1
        elif self.ewpolineEdit.text() != '':
            sql = "select 单词号,单词,音标,释义 from word where 发音 =%s"
            old_wpo = self.ewpolineEdit.text()
            cur.execute(sql, (old_wpo,))
            signal = 2
            wxo = '音标'
            old_wxo = old_wpo
        elif self.ewtolineEdit.text() != '':
            sql = "select 单词号,单词,音标,释义 from word where 释义 =%s"
            old_wto = self.ewtolineEdit.text()
            cur.execute(sql, (old_wto,))
            signal = 3
            wxo = '释义'
            old_wxo = old_wto
        else:
            self.statusbar.showMessage('请勿查找空值!')
            readyfind = False
            signal = 4

        # sqls.conn.commit()

        # print(signal)
        data = cur.fetchone()
        print(len(data))
        if data:
            self.ewnolineEdit.setText(data[0].strip())
            self.ewcolineEdit.setText(data[1].strip())
            self.ewpolineEdit.setText(data[2].strip())
            self.ewtolineEdit.setText(data[3].strip())
            self.statusbar.showMessage('查找成功！')
        else:
            self.ewnolineEdit.setText('')
            self.ewcolineEdit.setText('')
            self.ewpolineEdit.setText('')
            self.ewtolineEdit.setText('')
            self.statusbar.showMessage('查找失败！')
        sqls.conn.close()

    # 编辑
    def update_word(self):

        # old_client_id = self.old_client_id.text()
        # client_name = self.editor_client_name.text()
        # client_phone = self.editor_client_phone.text()
        # client_id = self.editor_client_id.text()
        # regex = re.compile(r"(^0\d{2,3}-\d{7,8}$)")
        # if re.match(regex, client_phone):

        # 2、获取cursor
        cur = sqls.GetConnect()
        # 3、SQl语句
        # 这里倒数第二个%s为什么他妈怎么都有问题
        # sql = "update word set 单词号=%s, 单词=%s, 音标=%s,释义=%s " \
        #       "where %s = %s"
        if wxo == '单词号':
            sql = "update word set 单词号=%s, 单词=%s, 音标=%s,释义=%s " \
                  "where 单词号 = %s"
        elif wxo == '单词':
            sql = "update word set 单词号=%s, 单词=%s, 音标=%s,释义=%s " \
                  "where 单词 = %s"
        elif wxo == '音标':
            sql = "update word set 单词号=%s, 单词=%s, 音标=%s,释义=%s " \
                  "where 音标 = %s"
        elif wxo == '释义':
            sql = "update word set 单词号=%s, 单词=%s, 音标=%s,释义=%s " \
                  "where 释义 = %s"
        wno = self.ewnolineEdit.text()
        wco = self.ewcolineEdit.text()
        wpo = self.ewpolineEdit.text()
        wto = self.ewtolineEdit.text()
        # print(wno,wco,wpo,wto)
        # # 4、执行语句
        # print(wxo, old_wxo)
        cur.execute(sql, (wno, wco, wpo, wto, old_wxo))
        # 5、insert、update、delete必须显示提交

        sqls.conn.commit()
        # 6、关闭资源

        sqls.conn.close()

        self.statusbar.showMessage('修改成功！')

        self.show_word()

    # else:
    #     self.statusBar().showMessage("电话格式位区号-电话")

    def del_word(self):
        warning = QMessageBox.warning(self, "删除单词", "你确定删除吗?",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            cur = sqls.GetConnect()
            if wxo == '单词号':
                sql = "delete from word where 单词号 = %s"
                sql1 = "delete from we where 单词号 = %s"
            elif wxo == '单词':
                sql = "delete from word where 单词 = %s"

            elif wxo == '音标':
                sql = "delete from word where 音标 = %s"

            elif wxo == '释义':
                sql = "delete from word where 释义 = %s"

            print(old_wxo)
            # 4、执行语句
            if signal == 0:
                cur.execute(sql1, (old_wxo,))
                sqls.conn.commit()
            cur.execute(sql, (old_wxo,))
            # 5、insert、update、delete必须显示提交

            sqls.conn.close()

            self.statusbar.showMessage('删除单词成功!')
            self.show_word()

    '''
    例句处理
    '''

    def add_eg(self):
        # 获取连接
        # sqls = MSSQL()
        cur = sqls.GetConnect()
        sql = "insert into eg(例句号,例句,翻译) values(%s,%s,%s)"
        # sql = "insert into word(单词号) values(%s)"
        eno = self.enolineEdit.text()
        eco = self.ecotextEdit.toPlainText()
        eto = self.etotextEdit.toPlainText()

        print(eno, eco, eto)
        # 执行

        cur.execute(sql, (eno, eco.strip(), eto.strip()))
        # cur.execute(sql, (wno,))
        # 提交
        sqls.conn.commit()
        # 关闭
        sqls.conn.close()
        # 状态栏显示
        self.statusbar.showMessage('例句记录添加成功！')
        self.show_eg()

    # 显示已有例句，并且添加完毕后可以直接看到
    def show_eg(self):
        # sqls = MSSQL()
        cur = sqls.GetConnect()
        sql = "select * from eg"
        cur.execute(sql)
        data = cur.fetchall()

        if data:
            self.eg_table.setRowCount(0)
            self.eg_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.eg_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.eg_table.rowCount()
                self.eg_table.insertRow(row_position)

        sqls.conn.close()

    # 复位
    def reset_eg_text(self):
        self.etotextEdit.setText('')
        self.ecotextEdit.setText('')
        self.enolineEdit.setText('')
        self.show_eg()

    # 修改例句
    def upd_eg(self):
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=EnglishHelper;Uid=sa;Pwd=123")
        db.open()
        model = QSqlTableModel(None, db)
        model.setTable('eg')
        model.select()
        self.egtableView.setModel(model)
        self.egtableView.show()
        # q = QModelIndex(10)
        # self.egtableView.setCurrentIndex(q)
        self.del_eg_Button.clicked.connect(lambda: model.removeRow(self.egtableView.currentIndex().row()))

    # 维护we表
    def creat_we_table(self):
        cur = sqls.GetConnect()
        sql = "delete we"
        cur.execute(sql)
        sqls.conn.commit()
        t = self.wtoelineEdit.text()
        sql = "select 单词号,单词 from word"
        cur.execute(sql, (t,))
        data_w = cur.fetchall()
        print(data_w)
        for item in data_w:
            print(item)
            sql = "select TOP 2 例句号 from eg where 例句 like '%%%s%%' " % (str(item[1]))
            print(sql)

            cur.execute(sql)
            data_e = cur.fetchall()
            print(len(data_e))
            print(data_e)
            for i in range(0, len(data_e)):
                sql = 'insert into we values(%s,%s)'

                cur.execute(sql, (str(item[0]), str(data_e[i][0])))

                sqls.conn.commit()
                # print((str(item[0]), str(data_e[i][0])))

        sqls.conn.close()

    # 展示we表
    def show_we(self):
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=EnglishHelper;Uid=sa;Pwd=123")
        db.open()
        model = QSqlTableModel(None, db)
        model.setTable('we')
        model.select()
        self.wetableView.setModel(model)
        self.wetableView.show()

    # 词典的查询
    def select_wtoe(self):

        cur = sqls.GetConnect()

        wtoeword = self.wtoelineEdit.text()

        sql = 'select 单词,释义,音标 from word where 单词 = %s'
        cur.execute(sql, (wtoeword,))
        data = cur.fetchone()
        print(data)
        self.wtopTextEdit.setPlainText(data[1].strip())
        self.wpo_textBrowser.setText(data[2].strip())
        sql = 'select TOP 3 例句,翻译 from eg where 例句号 in (select 例句号 from we where 单词号 = (select 单词号 from word where 单词 =%s))'
        cur.execute(sql, (data[0],))
        data_e = cur.fetchall()
        print(len(data_e))
        s = ''
        for i in range(0, len(data_e)):
            s = s + '例句%s:' % (i + 1) + '\t' + data_e[i][0].strip() + '\n' + '\t' + data_e[i][1].strip() + '\n' + '\n'

        # s = data[0].strip()+'\n'+data[1].strip()
        self.wtoeTextEdit.setPlainText(s)

        sqls.conn.close()

    def traslation(self):

        # 百度appid和密钥需要通过注册百度【翻译开放平台】账号后获得
        appid = '20210705000880494'  # 填写你的appid
        secretKey = 'N8Ulz_0geVaxzpDoBbb7'  # 填写你的密钥

        httpClient = None
        myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址

        fromLang = 'auto'  # 原文语种
        toLang = 'zh'  # 译文语种
        salt = random.randint(32768, 65536)
        # 手动录入翻译内容，q存放

        q = self.src_tra_textEdit.toPlainText()
        print(q)

        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
                '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

        # 建立会话，返回结果
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            # print(result)
            s = ' '
            for item in result['trans_result']:
                s = s + item['dst']
            self.dst_tra_textEdit.setText(s)
            # r_result = result['trans_result'][0]
            # print(r_result)
            # print(r_result['dst'])
            # self.dst_tra_textEdit.setText(r_result['dst'])

        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()

    # 记忆卡片-来一个查询过的单词

    def memo_comeon(self):
        global count
        self.icant_Button.setText('不会')
        self.its_easy_Button.setText('提交')
        count = 0
        cur = sqls.GetConnect()
        sql = 'select 单词 from memory '
        sql = 'select 单词 from word where 单词号 in (select 单词号 from memory) '  # 修改
        # print(sql)
        cur.execute(sql)

        data = cur.fetchall()
        # print(data)
        seed = random.randint(0, len(data) - 1)
        # print(seed)
        # print(data[seed])
        self.memo_wd_textBrowser.setText(data[seed][0])
        sqls.conn.close()

    # 当我说我不能= =
    def memo_icant(self):
        global count
        count = count + 1

        cur = sqls.GetConnect()
        sql = 'select 释义 from word where 单词=%s '
        s = self.memo_wd_textBrowser.toPlainText()
        cur.execute(sql, (s))
        data = cur.fetchone()
        tip_wpo = ''
        st = ''
        # print(data)
        if data:
            regex_str = ".*?([\u4E00-\u9FA5]+).*?"
            match_obj = re.findall(regex_str, data[0])
            # print(match_obj)

            for i, item in enumerate(match_obj):
                if i == 0:
                    tip_wpo = item[0]
                st = st + item + ';'
            if count == 1:
                self.wto_Browser.setText(tip_wpo)
                self.icant_Button.setText('还是不会')
            else:
                self.wto_Browser.setText(st)
                self.icant_Button.setText('真的太逊了')

        else:
            self.statusbar.showMessage('这个单词在单词表竟然没有！！')
        sql = 'select 痛苦程度 from memory where 单词= %s )'
        sql = 'select 痛苦程度 from memory where 单词号 =(select 单词号 from word where 单词 = %s )'  # 修改
        cur.execute(sql, (s,))
        data = cur.fetchone()
        num = data[0]
        num = num + 1
        print(num)
        sql = 'update memory set 痛苦程度=痛苦程度+1 where 单词=%s'
        sql = 'update memory set 痛苦程度=痛苦程度+1 where 单词号 =(select 单词号 from word where 单词 = %s )'  # 修改
        cur.execute(sql, (s,))
        sqls.conn.commit()
        sqls.conn.close()

    # 看个例句
    def look_look_eg(self):
        sql = 'select TOP 3 例句,翻译 from eg where 例句号 in (select 例句号 from we where 单词号 = (select 单词号 from word where 单词 =%s))'
        cur = sqls.GetConnect()
        s = self.memo_wd_textBrowser.toPlainText()
        cur.execute(sql, (s,))
        data_e = cur.fetchall()
        print(len(data_e))
        s = ''
        for i in range(0, len(data_e)):
            s = s + '例句%s:' % (i + 1) + '\t' + data_e[i][0].strip() + '\n' + '\t' + data_e[i][1].strip() + '\n' + '\n'
        self.memo_eg_textBrowser.setText(s)
        sqls.conn.close()

    def submit_my_answer(self):
        s_e = self.memo_answer_textEdit.toPlainText()
        wd = self.memo_wd_textBrowser.toPlainText()

        print(s_e)
        print(wd)
        cur = sqls.GetConnect()

        sql = "select 单词 from word where 释义 like '%%%s%%' "% s_e
        print(sql)
        # 这里返回值为None程序就会不知道为什么退出
        cur.execute(sql,())

        data = cur.fetchall()
        print(data[0][0])
        print(s_e)

        if data[0][0] == wd:
            self.its_easy_Button.setText('恭喜答对')
        else:
            sql = 'update memory set 以为的释义=%s where 单词=%s'
            sql = 'update memory set 以为的释义=%s where 单词号 =(select 单词号 from word where 单词 = %s )'  # 修改
            print(66666666)
            cur.execute(sql, (s_e, wd))

            sqls.conn.commit()
            sqls.conn.close()


def main1():
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main1()
