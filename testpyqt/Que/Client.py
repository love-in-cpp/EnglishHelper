# -*- coding = utf-8 -*-
# @Time : 2021/6/2 0:38
# @Author : 刘正阳
# @File : Client.py
# @Software : PyCharm


import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
if __name__=='__main__':
    app = QApplication(sys.argv)
    sock = QTcpSocket()
    sock.connectToHost(QHostAddress("127.0.0.1"), 10000)
    datagram = "ABC".encode()
    sock.write(datagram)

    sock.close()

    sys.exit(app.exec_())

