#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 16:08
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Myflume.py
# @Software: PyCharm
from flumepy.flume import ThriftSourceProtocol
from flumepy.flume.ttypes import ThriftFlumeEvent
from thrift.transport import TTransport, TSocket
from thrift.protocol import TCompactProtocol
class FlumeClient(object):
    def __init__(self, thrift_host, thrift_port, timeout=None, unix_socket=None):

        self.timeout = timeout
        self._socket = TSocket.TSocket(thrift_host, int(thrift_port), unix_socket)
        self._transport_factory = TTransport.TFramedTransportFactory()
        self._transport = self._transport_factory.getTransport(self._socket)
        self._protocol = TCompactProtocol.TCompactProtocol(trans=self._transport)
        self.client = ThriftSourceProtocol.Client(iprot=self._protocol, oprot=self._protocol)
        self.connect()
    #建立thrift连接
    def connect(self):
        try:
            if self.timeout:
                self._socket.setTimeout(self.timeout)
            if not self.is_open():
                self._transport = self._transport_factory.getTransport(self._socket)
                self._transport.open()
        except Exception as e:
            print(e)
            self.close()
    #判断当前连接是否打开
    def is_open(self):
        return self._transport.isOpen()

    #发送数据
    def send(self, event):
        try:
            self.client.append(event)
        except Exception as e:
            print(e)
        finally:
            self.connect()
    #批量发送数据
    def send_batch(self, events):
        try:
            self.client.appendBatch(events)
        except Exception as e:
            print(e)
        finally:
            self.connect()
    #关闭连接
    def close(self):
        self._transport.close()
# if __name__ == '__main__':
#     header = {"thirdParty":"false", "s.n":"drip-sms-record1", "cpname":"BaseAbility", "port":"8189", "localip":"127.0.0.1", "ismonitor":"false", "currentQueueSize":"0", "isbyte":"false", "room":"hefei", "collectionName":"drip-sms-record1", "timestamp":"1532509774532","event":"smsSendRecord"}
#     print(type(header))
#     new_body = '''logtype~smsSendRecord1_0request~[{"appid":"100IME","channel":"tencent","content":"【科大讯飞test】您好，您本次操作的验证码为1444，序号为07。请在30分钟内使用，过期无效。","extra":"--","ltm":"--","phone":"18856361920","sid":"1:1234567891011","status":"--","stm":"2018-07-25 18:26:58","tid":"1"}]cpname~BaseAbilityappid~CB2W28VAlocalip~127.0.0.1event~smsSendRecordroom~hefei'''
#     # new_body = "logtype~smsSendRecord1_0"+chr(31)+'request~[{"appid":"100IME","channel":"tencent","content":"【科大讯飞test】您好，您本次操作的验证码为0725，序号为725。请在50分钟内使用，过期无效。","extra":"--","ltm":"--","phone":"18856361920","sid":"1:15325144707702320056361920999","status":"--","stm":"2018-07-25 18:26:58","tid":"1"}]'+chr(31)+"cpname~BaseAbility"+chr(31)+"appid~CB2W28VA"+chr(31)+"localip~127.0.0.1"+chr(31)+"event~smsSendRecord"+chr(31)+"room~hefei"+chr(31)
#     flume_client = FlumeClient('192.168.45.174', 32000)
#     print type(new_body)
    # event = ThriftFlumeEvent(headers=header, body=new_body.encode())
    # flume_client.send(event)
    # flume_client.close()
    # # #建立连接
    # flume_client = FlumeClient('192.168.45.174', 32000)
    # event = ThriftFlumeEvent(headers=header, body=body.encode())
    # # #header是一个字典
    # # #body是一个字符串
    # # event = ThriftFlumeEvent({'k1':'v1', 'k2':'v2'}, '这是一个event的body部分')
    # flume_client.send(event)
    # #
    # # #生成100个event一次行发送
    # # events = [ThriftFlumeEvent({'k1':'1', 'k2':'2'}, 'body部分%s' % _) for _ in range(10)]
    # # flume_client.send_batch(events)
    # flume_client.close()