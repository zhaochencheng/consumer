#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 15:21
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Myelasticsearch.py
# @Software: PyCharm
from elasticsearch import Elasticsearch
class myElasticsearch():
    def __init__(self, host):
        self.host = host
    def match(self, index, doc_type, query):
        #仿照kibana中的写法
        es = Elasticsearch([self.host])
        #这中方式返回的结果和kibana查询结果一致，为json
        resp = es.search(index=index, doc_type=doc_type, body=query)
        return resp
    def put(self, index, doc_type, query):
        es = Elasticsearch([self.host])
        resp = es.index(index=index, body=query, doc_type=doc_type)
        return resp
    def delete_data(self, index, doc_type, query):
        es = Elasticsearch([self.host])
        resp = es.delete_by_query(index=index, body=query, doc_type=doc_type)
        return resp
# if __name__ == '__main__':
#     servers = '192.168.45.169:9200'
#     # servers = '172.16.82.142:9200'
#     index = 'dripsms2018'
#     doc_type = 'smsRecord100IME'
#     # doc_type = "test"
#     query = {"query": {"match": {'sid':'1:15356108237303550056361920999'}}}
#     query_all = {"query": {"match": {"name":"test_run"}}}
#     body = {"name":"test_run","phone":"women11","content":"我们"}
#     test_es = myElasticsearch(host=servers)
#     data = test_es.match(index=index, doc_type=doc_type, query=query)
#     # data = test_es.put(index=index, query=body, doc_type=type)
#     # data = test_es.delete_data(index=index, query=query, doc_type=type)
#     # print data
#     data1 = data['hits']['hits']
#     # # # for i in data1:
#     print data1
#     print data1[0]['_source']
#     print data1[0]['_source']['phone']
#     phone = data1[0]['_source']['phone']
#     phone = 1
#     print phone
#     print type(phone)
#     if type(phone) != int:
#         phone = phone.encode('utf-8')
#     else:
#         phone = phone
#     print phone, type(phone)

    #     print str(i).encode("utf-8")