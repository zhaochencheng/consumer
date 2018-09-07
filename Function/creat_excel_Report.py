#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 17:10
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : creat_excel_Report.py
# @Software: PyCharm
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class create_excel_report():
    def __init__(self, workbook_path):
        self.workbook = xlsxwriter.Workbook(workbook_path)
    def _add_worksheet(self, worksheet):
        return self.workbook.add_worksheet(worksheet)
    def get_format(self, wd, option={}):
        return wd.add_format(option)
    def get_format_center(self,wd,style=1):
        return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': style})
    def set_border_(self, wd, style=1):
        return wd.add_format({}).set_border(style=style)
    def write_center(self, worksheet, cl, data, wd):
        return worksheet.write(cl, data, self.get_format_center(wd))
    def create_pie(self, workbook, worksheet):
        chart = workbook.add_chart({'type': 'pie'})
        chart.add_series({
            'name': "测试情况统计",
            'categories': '=测试总览!$D$4:$D$5',
            'values': '=测试总览!$E$4:$E$5'
        })
        chart.set_title({'name': '测试情况统计'})
        chart.set_style(10)
        worksheet.insert_chart('A9', chart, {'x_offset': 25, 'y_offset': 10})
    def create_testinstruction(self, worksheet, data):
        # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        # worksheet.set_row(0, 200)

        define_format_H1 = self.get_format(self.workbook, {'bold': True, 'font_size': 18})
        define_format_H2 = self.get_format(self.workbook, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")
        # Create a new Chart object.

        worksheet.merge_range('A1:F1', '测试报告概况', define_format_H1)
        worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
        worksheet.merge_range('A3:A6', '这里放图片', self.get_format_center(self.workbook))

        self.write_center(worksheet, "B3", '项目名称', self.workbook)
        self.write_center(worksheet, "B4", '接口版本', self.workbook)
        self.write_center(worksheet, "B5", '脚本语言', self.workbook)
        self.write_center(worksheet, "B6", '测试环境', self.workbook)
        self.write_center(worksheet, "C3", data['test_name'], self.workbook)
        self.write_center(worksheet, "C4", data['test_version'], self.workbook)
        self.write_center(worksheet, "C5", data['test_language'], self.workbook)
        self.write_center(worksheet, "C6", data['test_environment'], self.workbook)

        self.write_center(worksheet, "D3", "用例总数", self.workbook)
        self.write_center(worksheet, "D4", "通过总数", self.workbook)
        self.write_center(worksheet, "D5", "失败总数", self.workbook)
        self.write_center(worksheet, "D6", "测试日期", self.workbook)

        self.write_center(worksheet, "E3", data['test_sum'], self.workbook)
        self.write_center(worksheet, "E4", data['test_success'], self.workbook)
        self.write_center(worksheet, "E5", data['test_failed'], self.workbook)
        self.write_center(worksheet, "E6", data['test_date'], self.workbook)

        self.write_center(worksheet, "F3", "分数", self.workbook)
        worksheet.merge_range('F4:F6', data['pass_rate'], self.get_format_center(self.workbook))
        self.create_pie(workbook=self.workbook, worksheet=worksheet)
        # self.workbook.close()
    def create_testinformation(self, worksheet, testsum, data):
        # 设置列行的宽高
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)

        worksheet.merge_range('A1:H1', '测试详情', self.get_format(self.workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
        self.write_center(worksheet, "A2", '用例编号', self.workbook)
        self.write_center(worksheet, "B2", '用例名称', self.workbook)
        self.write_center(worksheet, "C2", '描述信息', self.workbook)
        self.write_center(worksheet, "D2", '初始化', self.workbook)
        self.write_center(worksheet, "E2", '预期值', self.workbook)
        self.write_center(worksheet, "F2", '实际值', self.workbook)
        self.write_center(worksheet, "G2", '校验结果', self.workbook)
        self.write_center(worksheet, "H2", '测试结果', self.workbook)
        # for i in range(3, testsum+4):
        for item in data["info"]:
            self.write_center(worksheet, "A"+str(testsum+2), str(item["test_num"]), self.workbook)
            self.write_center(worksheet, "B"+str(testsum+2), str(item["test_name"]), self.workbook)
            self.write_center(worksheet, "C"+str(testsum+2), str(item["test_desc"]), self.workbook)
            self.write_center(worksheet, "D"+str(testsum+2), str(item["test_parma"]), self.workbook)
            self.write_center(worksheet, "E"+str(testsum+2), str(item["test_hope"]), self.workbook)
            self.write_center(worksheet, "F"+str(testsum+2), str(item["test_actual"]), self.workbook)
            self.write_center(worksheet, "G"+str(testsum+2), str(item["test_result"]), self.workbook)
            self.write_center(worksheet, "H"+str(testsum+2), str(item["test_checkresult"]), self.workbook)
            testsum = testsum -1
        self.workbook.close()
# if __name__ == '__main__':
#     report_path = "F:\\python_project\\Consumer_autoTest1\\Test_report\\report.xlsx"
#     test_excel = create_excel_report(report_path)
#     worksheet = test_excel._add_worksheet("测试总览")
#     worksheet2 = test_excel._add_worksheet("测试详情")
#     result = {'test_name': '213', 'test_version': '1.0.1', 'test_language': 'python', 'test_environment': '', 'test_sum': "", 'test_success': '', 'test_failed': '', 'test_date': '', 'pass_rate': ""   }
#     casedata = {"info": [{"test_num": " ", "test_name": ' ', "test_desc": " ", "test_parma": " ", "test_hope": " ","test_actual": " ", "test_result": " ", "test_checkresult": " "}]}
#     test_excel.create_testinstruction(worksheet=worksheet, data=result)
#     test_excel.create_testinformation(worksheet=worksheet2, testsum=int(12), data=casedata)
    # try:
    #     test_excel.create_testinstruction(worksheet=worksheet, data=result)
    # except Exception as E:
    #     print E
    # try:
    #     test_excel.create_testinformation(worksheet=worksheet2, testsum=12, data=casedata)
    # except Exception as E:
    #     print E