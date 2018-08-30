#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 11:11
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Mylog.py
# @Software: PyCharm
import logging

class Logger:
    def __init__(self, path, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG) #设置logger日志等级
        #设置输出日志格式
        fmt = logging.Formatter(fmt='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(Flevel)
        #为handler指定输出格式
        #设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
        #解决方案1，添加removeHandler语句，每次用完之后移除Handler
        # logger.removeHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message, exc_info=True)

    def critical(self,message):
        self.logger.critical(message)



# if __name__ =='__main__':
#     log_filename = "F:\\python_project\\Consumer_autoTest\\Log\\loggint.txt"
#     log = Logger(log_filename, logging.DEBUG)
#     log.debug('一个debug信息')
#     log.info('一个info信息')
#     log.warn('一个warning信息')
#     log.error('一个error信息')
    # for i in range(4):
    #     log.cri('一个致命critical信息')