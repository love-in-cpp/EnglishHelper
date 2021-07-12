# -*- coding = utf-8 -*-
# @Time : 2021/7/4 17:06
# @Author : 刘正阳
# @File : dbutil.py
# @Software : PyCharm

import pymssql

# def get_cur():
#
#     # if not self.db:
#     #     raise (NameError, '没有设置数据库信息')
#     conn = pymssql.connect(host='localhost', user='sa', pwd='123', db="Extra", charset='utf8')
#     cur = conn.cursor()
#     if not cur:
#         raise (NameError, '连接数据库失败')
#     else:
#         return cur
# def close_conn()

class MSSQL:
    def __init__(self, host="localhost", user='sa', pwd='123', db="EnglishHelper"):
        self.host = host
        print(self.host)
        self.user = user
        self.pwd = pwd
        self.db = db

    def GetConnect(self):
        if not self.db:
            raise (NameError, '没有设置数据库信息')
        self.conn = pymssql.connect(host=self.host,user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, '连接数据库失败')
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def GetData(self, sql):
        count = 0
        for i in range(len(sql)):
            for j in range(len(sql[i])):
                count += 1
                if type(sql[i][j]) is str:
                    print(sql[i][j].encode('latin1').decode('gbk'), end=',')
                else:
                    print(sql[i][j], end=',')
                if count % len(sql[i]) == 0:
                    print('\n')
#
#
def main():
    ms = MSSQL(host='localhost', user='sa', pwd='123', db="Extra")

    sql = ms.ExecQuery('SELECT top 5 * from SC')
    #print(sql)
    ms.GetData(sql)


if __name__ == '__main__':
    main()