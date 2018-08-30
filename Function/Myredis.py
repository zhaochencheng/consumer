#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 15:01
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Myredis.py
# @Software: PyCharm
import redis
import ast
class myRedis():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def set_redis(self, database, key, value, TTL=1000):
        '''

        :param database:
        :param key:
        :param value:
        :param TTL:
        :return: if success return True
        '''
        pool = redis.ConnectionPool(host=self.host, port=int(self.port), db=database, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if r.exists(key):
            #键存在 则更新
            result = r.set(key, value)
            r.expire(key, TTL)
        else:
            #键不存在，则新增
            result = r.set(key, value)
            r.expire(key, TTL)
        return result
    def get_redis(self, database, key):
        '''

        :param database:
        :param key:
        :return: dict {}
        '''
        pool = redis.ConnectionPool(host=self.host, port=int(self.port), db=database, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        result = r.get(key)
        L = []
        L.append(result)
        return L
        # return ast.literal_eval(result)
    def delete_redis(self, database, key):
        '''

        :param database:
        :param key:
        :return: if key is exit ,return 1
                else retutn 0
        '''
        pool = redis.ConnectionPool(host=self.host, port=int(self.port), db=database, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        result = r.delete(key)
        return result

# if __name__ == '__main__':
#     redis_host = '192.168.45.107'
#     port = 6379
#     database = 12
#     key = "test_run"
#     value = '{"phone":"13956397863","appid":"100IME","channel":"tencent","index":"dripsms2018","type":"smsRecord100IME","stm":"2018-07-22 08:56:01","tid":"10197","chargedCountPre":1}'
#     # value = '{"phone":"13956397863"}'
#     test_redis = myRedis(host=redis_host, port=port)
#     # a = {{"test_run": {"phone": "13956397863"}}, {"TTl": 10000}}
#     data = test_redis.set_redis(database=database, key=key, value=value, TTL=10000)
#     # data = test_redis.get_redis(database=database, key=key)
#     # data = test_redis.delete_redis(database=database, key=key)
#     print data, type(data)
#     # print data[0]
#     # print data["index"]
#     a = {"test_run": {"phone": "13956397863"}}