#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 14:26
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Mymysql.py
# @Software: PyCharm
import pymysql
class myMysql():
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
    def select(self, database, query):
        #打开数据库连接
        db_conn = pymysql.connect(host=self.host, port=int(self.port), user=self.username, password=self.password, database=database)
        #使用cursor()方法获取操作游标
        cursor = db_conn.cursor()
        #执行的都是原生SQL语句 执行SQL语句
        cursor.execute(query)
        #提交到数据库执行
        db_conn.commit()
        #获取所有执行结果
        data = cursor.fetchall()
        cursor.close()
        db_conn.close()
        return list(data)
    def insert(self, database, query):
        db_conn = pymysql.connect(host=self.host, port=int(self.port), user=self.username, password=self.password, database=database)
        #使用cursor()方法获取操作游标
        cursor = db_conn.cursor()
        #执行的都是原生SQL语句 执行SQL语句
        cursor.execute(query=query)
        #提交到数据库执行
        db_conn.commit()
        data = cursor.fetchall()
        cursor.close()
        db_conn.close()
        return data
    def update(self, database, query):
        db_conn = pymysql.connect(host=self.host, port=int(self.port), user=self.username, password=self.password, database=database)
        cursor = db_conn.cursor()
        cursor.execute(query=query)
        db_conn.commit()
        data = cursor.fetchall()
        cursor.close()
        db_conn.close()
        return data
    def delete(self, database, query):
        #打开数据库连接
        db_conn = pymysql.connect(host=self.host, port=int(self.port), user=self.username, password=self.password, database=database)
        #使用cursor()方法获取操作游标
        cursor = db_conn.cursor()
        #执行的都是原生SQL语句 执行SQL语句
        cursor.execute(query)
        #提交到数据库执行
        db_conn.commit()
        #获取所有执行结果
        data = cursor.fetchall()
        cursor.close()
        db_conn.close()
        return data
# if __name__ == '__main__':
#     hostip = '192.168.45.104'
#     port = 3306
#     username = 'root'
#     pwd = '123456'
#     database = 'zcctest'
#     select_query = 'select name from zcctest where sex="woman"'
#     insert_data = 'insert into zcctest(NAME,age,sex)VALUES("test_run",13,"woman")'
#     update_data = "UPDATE zcctest SET AGE = AGE + 1 WHERE name = 'z455'"
#     delete_data = "DELETE FROM zcctest WHERE name='z455'"
#     test_mysql = myMysql(host=hostip, port=port, username=username, password=pwd)
#     data =test_mysql.select(database=database, query=select_query)
#     # data =test_mysql.insert(database=database, query=insert_data)
#     # data =test_mysql.update(database=database, query=update_data)
#     # data =test_mysql.delete(database=database, query=delete_data)
#     print data, type(data)
#     # print data[0]