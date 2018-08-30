#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 16:17
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Mymongo.py
# @Software: PyCharm
from pymongo import MongoClient

class myMongo():
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def find_One(self, database, collection, query):
        '''

        :param database:
        :param collection:
        :param query:
        :return: list[]
        '''
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.find_one(query)
        return result
    def find_all(self, database, collection, query):
        '''

        :param database:
        :param collection:
        :param query:
        :return: list[]
        '''
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.find(query)
        return list(result)
    def insert_One(self, database, collection, query):
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.insert_one(query)
        return result
    def insert_Many(self, database, collection, query):
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.insert_many(query)
        return result
    def remove(self, database, collection, query):
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.remove(query)
        return result
    def delete_One(self,database, collection, query):
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.delete_one(query)
        return result
    def delete_Many(self, database, collection, query):
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.delete_many(query)
        return result
    def update_Many(self, database, collection,filter, query):
        client = MongoClient(self.host, int(self.port))
        db = client[database]
        collections = db[collection]
        result = collections.update_many(filter, query)
        return result



# if __name__ == '__main__':
    # mongo_host = "192.168.45.104"
    # port = 27017
    # database = "ConsumerTest"
    # collection = "test_mongo"
    # find_query = {}
    # find_query_one = {"age":"12"}
    # insert_query = {"name": "zhangsan", "age":"12", "grade":"99", "love":"math"}
    # print insert_query,type(insert_query)
    # data = [{'name': i} for i in ["zhangsann", "lisi", "mike", "lili"]]
    # delete_query_many = {}
    # test_mongo = myMongo(host=mongo_host, port=port)
    # # result = test_mongo.insert_Many(database=database, collection=collection, query=data)
    # # result = test_mongo.insert_One(database=database, collection=collection, query=insert_query)
    # result = test_mongo.find_all(database=database, collection=collection, query=find_query_one)
    # # result = test_mongo.find_One(database=database, collection=collection, query=find_query_one)
    # # result = test_mongo.delete_One(database=database, collection=collection, query=find_query_one)
    # # result = test_mongo.update_Many(database=database, collection=collection,filter={"name": "lisi"}, query={"$inc": {"age":5}})
    # # result = test_mongo.delete_Many(database=database, collection=collection, query=delete_query_many)
    # # result = test_mongo.remove(database=database, collection=collection, query=delete_query_many)
    # print result
    # print result
    # print type(result)