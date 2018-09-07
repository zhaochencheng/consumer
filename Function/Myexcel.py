#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 15:01
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Myexcel.py
# @Software: PyCharm
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class myexcel():
    def __init__(self, excel_path, sheelname):
        '''
        初始化
        :param excel_path: excel store path
        :param sheelname: execl sheelname
        :return:
        '''
        self.excel_path = excel_path
        self.sheelname = sheelname
    def read_myexcel(self, **kwargs):
        '''
        获取excel_path中sheelname中的信息
        :param kwargs:
        :return: List [];
        '''
        workbook = xlrd.open_workbook(self.excel_path)
        # 所有sheet 名称
        allsheelName = workbook.sheet_names()
        if self.sheelname in allsheelName:
            worksheet = workbook.sheet_by_name(self.sheelname)
            #该sheet 行数
            num_rows = worksheet.nrows
            #该sheet 列数
            num_cols = worksheet.ncols
            L = []
            for curr_row in range(1, num_rows):
                dic = {}
                for curr_col in range(num_cols):
                    #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error
                    ctype = worksheet.cell(curr_row, curr_col).ctype
                    row = worksheet.row_values(curr_row)
                    col = worksheet.col_values(curr_col)[0]
                    no = row[curr_col]
                    # 如果值本身为int，python读取excel将int读为float, 在此判断后先转化为int,再转化为str
                    if ctype == 2 and no % 1 == 0.0:
                        no = str(int(row[curr_col]))
                    # 如果值本身为float, python将其直接转化为str
                    dic[col] = str(no)
                #将读取的信息 添加至列表中
                L.append(dic)
            return L
        else:
            L = []
            print("输入sheel名称 与真实execl中的名称不符！")
            return L
# if __name__ == '__main__':
#     excel_path = 'F:\\python_project\\Consumer_autoTest1\\Config\\case.xlsx'
#     sheelname = "Sheet8"
#     excel =myexcel(excel_path=excel_path,sheelname=sheelname)
#     data = excel.read_myexcel()
#     print data
