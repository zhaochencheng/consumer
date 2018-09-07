#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 18:44
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Mymail.py
# @Software: PyCharm
import email.mime.multipart
import email.mime.text
from email import encoders
from email.utils import COMMASPACE,formatdate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
class myMail():
    def send_mail(self,sender, psw, receiver, smtpserver, report_file, port):
        '''第四步：发送最新的测试报告内容 发送一个带附件的邮件'''
        # 定义邮件内容
        msg = email.mime.multipart.MIMEMultipart()
        msg['Subject'] = u"自动化测试报告"
        msg["from"] = sender
        msg["to"] = COMMASPACE.join(receiver)  # 只能字符串
        msg['Date'] = formatdate(localtime=True)
        concent = '测试邮件'
        body = email.mime.text.MIMEText(concent, 'plain', 'utf-8')
        msg.attach(body)

        # 添加附件
        att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.xlsx"'
        msg.attach(att)
        # att = MIMEApplication(open(report_file, 'rb').read())
        # att.add_header('application/octet-stream', 'attachment', filename=file)
        # msg.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver, int(port))  # 连服务器
            smtp.login(sender, psw)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, int(port))
            smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('test report email has send out !')

# if __name__ == '__main__':
#     #邮箱配置
#     sender = "18856361920@163.com" #从该邮箱发送
#     psw = "XXXX" # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
#     smtp_server = "smtp.163.com" # 163邮箱的smtp Sever地址
#     port = '25'  # 开放的端口
#     receiver = ['907779487@qq.com', 'cczhao2@iflytek.com'] #邮箱收件人
#     mail = myMail()
#     mail.send_mail(sender, psw, receiver, smtp_server, 'F:\\python_project\\Consumer_autoTest1\\Test_report\\report.xlsx', port)  # 4最后一步发送报告
