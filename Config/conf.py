#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 17:18
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : conf.py
# @Software: PyCharm

# #测试环境
mongo_host = "192.168.45.104"
mongo_port = 27017

mysql_host = '192.168.45.104'
mysql_port = 3306
mysql_username = 'root'
mysql_pwd = '123456'

redis_host = '192.168.45.107'
redis_port = 6379

elasticsearch_host = '192.168.45.169:9200'

flumeIP = "192.168.45.169"
flumeport = 32000
#集成测试环境




# #
# #日志存放位置
log_filepath = '/usr/server/dripSMS/consumer/Consumer_autoTest1/Log/'
#
# #用例信息
excel_path = '/usr/server/dripSMS/consumer/Consumer_autoTest1/Config/case.xlsx'
sheelname = "Sheet5"
#
# #用例执行环境
case_name = '短信消息插件自动化调试'
case_environment = '集成测试环境'
case_version = '1.0.0'
# #报告路径
report_path = '/usr/server/dripSMS/consumer/Consumer_autoTest1/Test_report/report.xlsx'

# # 日志存放位置
# log_filepath = "F:\\python_project\\Consumer_autoTest1\\Log\\"
# # 用例信息
# excel_path = 'F:\\python_project\\Consumer_autoTest1\\Config\\case.xlsx'
# sheelname = "Sheet4"
# # 用例执行环境
# case_name = '短信消息插件自动化调试'
# case_environment = '集成测试环境'
# case_version = '1.0.1'
# # 报告路径
# report_path = 'F:\\python_project\\Consumer_autoTest1\\Test_report\\report.xlsx'

#邮箱配置
issendmail = False
sender = "18856361920@163.com" #从该邮箱发送
psw = "utt31801" # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
smtp_server = "smtp.163.com" # 163邮箱的smtp Sever地址
port = '25'  # 开放的端口
receiver = ['907779487@qq.com', 'cczhao2@iflytek.com'] #邮箱收件人