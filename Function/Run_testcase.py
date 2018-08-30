#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 15:27
# @Author  : zhaochencheng
# @Email   : 907779487@qq.com
# @File    : Run_testcase.py
# @Software: PyCharm
import ast
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
# #用于linux环境下 增加导包路径
python_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(python_path)
import time
import logging
# ## window 环境下使用该方式导包
# from Consumer_autoTest1.Function.creat_excel_Report import create_excel_report
# from Consumer_autoTest1.Function.Myexcel import myexcel
# from Consumer_autoTest1.Config.conf import *
# from Consumer_autoTest1.Function.Mymongo import myMongo
# from Consumer_autoTest1.Function.Mymysql import myMysql
# from Consumer_autoTest1.Function.Myredis import myRedis
# from Consumer_autoTest1.Function.Myelasticsearch import myElasticsearch
# from Consumer_autoTest1.Function.Myflume import FlumeClient
# from flumepy.flume.ttypes import ThriftFlumeEvent
# from Consumer_autoTest1.Function.Mylog import Logger
# from Consumer_autoTest1.Function.Mymail import myMail

# #linux 环境下使用该方式导包 sys.path增加路径
from creat_excel_Report import create_excel_report
from Myexcel import myexcel
from Config.conf import *
from Mymongo import myMongo
from Mymysql import myMysql
from Myredis import myRedis
from Myelasticsearch import myElasticsearch
from Myflume import FlumeClient
from flumepy.flume.ttypes import ThriftFlumeEvent
from Mylog import Logger
from Mymail import myMail

def get_excelcase(excel_path,sheelname):
    '''
    获取用例信息

    :param excel_path:

    :param sheelname:
    :return: allcase_into [] 返回excel 里sheelname中所有用例的信息
    '''
    execl = myexcel(excel_path=excel_path, sheelname=sheelname)
    data = execl.read_myexcel()
    #用例个数
    TotalcaseNum = int(data[len(data)-1]['testNum'][4:])
    allcase_info = []
    for caseNum in range(1, TotalcaseNum+1):
        testList = []
        for caseinfo in data:
            if caseinfo["testNum"] == ("test"+str(caseNum)):
                testList.append(caseinfo)
        if testList != []:
            allcase_info.append(testList)
    return allcase_info
def get_pycase(py_path):
    pass
def handler_Body(body):
    '''
    将body格式转换为要求的格式

    :param body:
    :return:
    '''
    str = ''
    for i in body:
        str = str+i+"~"+body[i]+chr(31)
    return str
def mongo_run(method, database, table, query):
    run_mongo = myMongo(host=mongo_host, port=mongo_port)
    if method == "insert":
        result = run_mongo.insert_One(database=database, collection=table, query=query)
        return result
    if method == "find":
        result = run_mongo.find_all(database=database, collection=table, query=query)
        return result
    if method == "find_count":
        result = run_mongo.find_all(database=database, collection=table, query=query)
        return len(result)
    if method == "delete":
        result = run_mongo.delete_Many(database=database, collection=table, query=query)
        return result
def mysql_run(method, database, query):
    run_mysql = myMysql(host=mysql_host, port=mysql_port, username=mysql_username, password=mysql_pwd)
    if method == "insert":
        result = run_mysql.insert(database=database, query=query)
        return result
    if method == "select":
        result = run_mysql.select(database=database, query=query)
        return result
    if method == "delete":
        result = run_mysql.delete(database=database, query=query)
        return result
def elasticsearch_run(method, database, table, query):
    run_elasticsearch = myElasticsearch(host=elasticsearch_host)
    if method == "put":
        result = run_elasticsearch.put(index=database, doc_type=table, query=query)
        return result
    if method == "match":
        result = run_elasticsearch.match(index=database, doc_type=table, query=query)
        return result
    if method == "delete":
        result = run_elasticsearch.delete_data(index=database, doc_type=table, query=query)
        return result
def redis_run(method, database, key, **kwargs):
    run_redis = myRedis(host=redis_host, port=redis_port)
    if method == "set_redis":
        result = run_redis.set_redis(database=database, key=key, value=kwargs['value'], TTL=kwargs['TTL'])
        return result
    if method == "get_redis":
        result = run_redis.get_redis(database=database, key=key)
        return result
    if method == "delete_redis":
        result = run_redis.delete_redis(database=database, key=key)
        return result

def get_check_variable(str):
    result = str.split('.')
    if len(result) > 1:
        return result[1]
    else:
        return ""
def bijiao(relation, check_content, Expected_results):
    if relation == "=":
        try:
            if type(check_content) != int:
                check_content = check_content.encode('utf-8')
            assert check_content == Expected_results
            return True
        except BaseException as E:
            print '查询结果：%s != 期望结果：%s'%(check_content,Expected_results)
            print "查询结果",check_content, type(check_content)
            print "期望结果",Expected_results, type(Expected_results)
            return False
    if relation == ">":
        try:
            assert check_content > Expected_results
            return True
        except BaseException as E:
            print '%s不大于%s'%(check_content,Expected_results)
            return False
    if relation == "<":
        try:
            assert check_content < Expected_results
            return True
        except BaseException as E:
            print '%s不小于%s'%(check_content,Expected_results)
            return False
def Analysis_rundata(data):
    test_sum = len(data["info"])
    test_failed = 0
    result = {}
    if test_sum != 0:
        for item in data["info"]:
            if item['test_checkresult'] == '不通过':
                test_failed += 1
        pass_rate = "%.2f" % ((1.0-(float(test_failed)/float(test_sum))))
    else:
        test_failed = 0
        pass_rate = "0.0%"
    result["test_name"] = case_name
    result['test_version'] = case_version
    result["test_language"] = 'python'
    result['test_environment'] = case_environment
    result['test_sum'] = int(test_sum)
    result['test_success'] = int(test_sum-test_failed)
    result['test_failed'] = int(test_failed)
    result['test_date'] = time.strftime('%Y-%m-%d %H:%M')
    result['pass_rate'] = pass_rate
    return result
class Run_case():
    def __init__(self):
        pass
    def run_case(self, excel_path, sheelname):
        localtime =time.strftime('%Y%m%d%H')
        #实例化 log
        log = Logger(log_filepath+localtime+".logging.txt", logging.DEBUG)
        #遍历 执行测试用例
        Totalcasemessage = get_excelcase(excel_path=excel_path, sheelname=sheelname)
        #用例个数
        case_totalnum = len(Totalcasemessage)
        print "用例个数：",case_totalnum
        Total_result = []

        for casemessage in Totalcasemessage:
            case_mess = {}
            test_parma = []
            test_hope = []
            test_actual = []
            test_result = []
            check_testresult = []
            log.info('\n')
            log.info('*'*10+casemessage[0]["testNum"]+'*'*10)
            log.info('\n')
            for casestep in casemessage:
                if casestep["condition"] == "init":
                    method = str(casestep["method"])
                    database = str(casestep["database"])
                    table = str(casestep["table"])
                    query = str(casestep["content"])
                    headers = str(casestep["headers"])
                    body = str(casestep["body"])
                    if casestep["assembly"] == "mongo":
                        log.info("####执行mongo初始化####")
                        try:
                            mongo_result = mongo_run(method=method, database=database, table=table, query=ast.literal_eval(query))
                            test_parma.append("{'mongo':"+"{'database':"+database+",'table':"+table+",'query':"+query+'}}')
                            log.info("{'mongo':"+"{'database':"+database+",'table':"+table+",'query':"+query+'}}')
                            log.info("####执行mongo初始化-完成####")
                        except Exception as mongo_init_error:
                            log.error(mongo_init_error)

                    if casestep["assembly"] == "mysql":
                        log.info("####执行mysql初始化####")
                        try:
                            mysql_result = mysql_run(method=method, database=database, query=query)
                            test_parma.append("{'mysql':"+"{'database':"+database+",'table':"+table+",'query':"+query+'}}')
                            log.info("{'mysql':"+"{'database':"+database+",'table':"+table+",'query':"+query+'}}')
                            log.info("####执行mysql初始化--完成####")
                        except Exception as mysql_init_error:
                            log.error(mysql_init_error)

                    if casestep["assembly"] == "elasticsearch":
                        log.info("##执行elasticsearch初始化####")
                        try:
                            elasticsearch_result = elasticsearch_run(method=method, database=database, table=table, query=query)
                            test_parma.append("{'elasticsearch':"+"{'index':"+database+",'type':"+table+",'query':"+query+'}}')
                            log.info("{'elasticsearch':"+"{'index':"+database+",'type':"+table+",'query':"+query+'}}')
                            log.info("##执行elasticsearch初始化--完成####")
                        except Exception as es_init_error:
                            log.error(es_init_error)

                    if casestep["assembly"] == "redis":
                        log.info("####执行redis初始化####")
                        try:
                            #获取需要在redis中缓存的数据，key value TTL
                            content = ast.literal_eval( casestep["content"])
                            key = content.keys()[0]
                            value = content[key]
                            TTL = content.keys()[1]
                            TTL_value = content["TTL"]
                            redis_result = redis_run(method=method, database=database, key=key, value=value, TTL=TTL_value)
                            test_parma.append("{'redis':"+"{'database':"+database+",'key':"+key+",'value':"+value+",'TTL':"+TTL_value+"}}")
                            log.info("{'redis':"+"{'database':"+database+",'key':"+key+",'value':"+value+",'TTL':"+TTL_value+"}}")
                            log.info("####执行redis初始化--完成####")
                        except Exception as redis_init_error:
                            log.error(redis_init_error)

                    if casestep["assembly"] == "flume":
                        log.info("####执行flume初始化####")
                        try:
                            flume_client = FlumeClient(flumeIP, flumeport)
                            # print body, type(body)
                            new_body = handler_Body(ast.literal_eval(body))
                            # print new_body
                            event = ThriftFlumeEvent(headers=ast.literal_eval(headers), body=new_body)
                            flume_client.send(event)
                            flume_client.close()
                            test_parma.append("flume"+"_"+"init")
                            log.info("headers:"+headers+'\n'+"body:"+new_body)
                            log.info("####执行flume初始化--完成####")
                        except Exception as flume_init_error:
                            log.error(flume_init_error)

                elif casestep["condition"] == "execute":
                    time_strategy = casestep["time_strategy"]
                    if time_strategy == "":
                        log.info("####未有时间策略####")
                    else:
                        log.info("####执行时间测试 休眠%ss ####" % time_strategy)
                        time.sleep(int(float(time_strategy)))

                elif casestep["condition"] == "check":
                    database = str(casestep["database"])
                    table = str(casestep["table"])
                    check_method = str(casestep['check_method'])
                    check_condition = str(casestep['check_condition'])
                    check_content = str(casestep['check_content'])
                    relation = str(casestep['relation'])
                    Expected_results = casestep['Expected_results']
                    if casestep["assembly"] == "mongo":
                        log.info("####执行mongo校验####")
                        try:
                            mongo_findresult = mongo_run(method=check_method, database=database, table=table, query=ast.literal_eval(check_condition))
                            log.info("mongo查询结果：%s" % mongo_findresult)
                            test_actual.append("mongo:"+check_content+relation+str(mongo_findresult[0][check_content]))
                            test_hope.append("mongo:"+check_content+relation+str(Expected_results))
                            mongo_checkresult = bijiao(relation=relation, check_content=mongo_findresult[0][check_content], Expected_results=Expected_results)
                            test_result.append("mongo:"+check_content+relation+str(Expected_results)+" is "+str(mongo_checkresult))
                            check_testresult.append(mongo_checkresult)
                        except Exception as mongo_check_error:
                            log.error(mongo_check_error)
                            check_testresult.append(False)
                    if casestep["assembly"] == "mysql":
                        log.info("####执行mysql校验####")
                        try:
                            mysql_findresult = mysql_run(method=check_method, database=database, query=check_condition)
                            log.info('查询结果：%s' % mysql_findresult)
                            test_actual.append("mysql:"+check_content+relation+str(mysql_findresult[0][0]))
                            test_hope.append("mysql:"+check_content+relation+str(Expected_results))
                            mysql_checkresult = bijiao(relation=relation, check_content=mysql_findresult[0][0], Expected_results=Expected_results)

                            test_result.append("mysql:"+check_content+relation+str(Expected_results)+" is "+str(mysql_checkresult))
                            check_testresult.append(mysql_checkresult)
                        except Exception as mysql_check_error:
                            log.error(mysql_check_error)
                            check_testresult.append(False)
                    if casestep["assembly"] == "elasticsearch":
                        log.info("####执行elasticsearch校验####")
                        try:
                            es_findresult = elasticsearch_run(method=check_method, database=database, table=table, query=check_condition)
                            log.info("ES查询结果：%s" % es_findresult['hits']['hits'][0]['_source'][check_content])
                            test_actual.append("elasticsearch:"+check_content+relation+str(es_findresult['hits']['hits'][0]['_source'][check_content]))
                            test_hope.append("elasticsearch:"+check_content+relation+str(Expected_results))
                            es_checkresult = bijiao(relation=relation, check_content=es_findresult['hits']['hits'][0]['_source'][check_content], Expected_results=Expected_results)
                            test_result.append("elasticsearch:"+check_content+relation+str(Expected_results)+" is "+str(es_checkresult))
                            check_testresult.append(es_checkresult)
                        except Exception as es_check_error:
                            log.error(es_check_error)
                            check_testresult.append(False)
                    if casestep["assembly"] == "redis":
                        log.info("####执行redis校验####")
                        try:
                            redis_findresult = redis_run(method=check_method, database=database, key=check_condition)
                            log.info("redis查询结果为：%s" % redis_findresult)
                            test_actual.append("redis:"+check_content+relation+str(redis_findresult[0]))
                            test_hope.append("redis:"+check_content+relation+str(Expected_results))
                            redis_checkresult = bijiao(relation=relation, check_content=ast.literal_eval(redis_findresult[0])[check_content], Expected_results=Expected_results)
                            test_result.append("redis:"+check_content+relation+str(Expected_results)+" is "+str(redis_checkresult))
                            check_testresult.append(redis_checkresult)
                        except Exception as redis_check_error:
                            log.error(redis_check_error)
                            check_testresult.append(False)

                elif casestep["condition"] == "clean":
                    database = str(casestep["database"])
                    table = str(casestep["table"])
                    method = str(casestep['method'])
                    content = str(casestep['content'])
                    if casestep["assembly"] == "mongo":
                        log.info("####执行mongo数据清除####")
                        try:
                            mongo_clean_result = mongo_run(method=method, database=database, table=table, query=ast.literal_eval(content))
                            log.info("####执行mongo数据清除--完成####")
                        except Exception as mongo_clean_error:
                            log.error(mongo_clean_error)
                    if casestep["assembly"] == "mysql":
                        log.info("####执行mysql数据清除####")
                        try:
                            mysql_clean_result = mysql_run(method=method, database=database, query=content)
                            log.info('####执行mysql数据清除--完成####')
                        except Exception as mysql_clean_error:
                            log.error(mysql_clean_error)
                    if casestep["assembly"] == "elasticsearch":
                        log.info("####执行elasticsearch数据清除####")
                        try:
                            es_clean_result = elasticsearch_run(method=method, database=database, table=table, query=content)
                            log.info('####执行elasticsearch数据清除--完成####')
                        except Exception as es_clean_error:
                            log.error(es_clean_error)
                    if casestep["assembly"] == "redis":
                        log.info("####执行redis数据清除####")
                        try:
                            redis_clean_result = redis_run(method=method, database=database, key=content)
                            log.info('####执行redis数据清除--完成####')
                        except Exception as redis_clean_error:
                            log.error(redis_clean_error)
                case_mess['test_parma'] = test_parma
                case_mess['test_actual'] = test_actual
                case_mess['test_hope'] = test_hope
                case_mess['test_result'] = test_result
            try:
                num = 0
                for check_result in check_testresult:
                    if check_result == True:
                        num += 1
                if len(check_testresult) == num:
                    test_checkresult = "通过"
                else:
                    test_checkresult = "不通过"
            except Exception as e:
                log.error(e)
                test_checkresult = ''
            try:
                test_Num = casestep["testNum"]
                test_Name = casestep["testName"]
                test_desc = casestep["desc"]
                case_mess['test_num'] = test_Num
                case_mess['test_name'] = test_Name
                case_mess['test_desc'] = test_desc
                case_mess['test_checkresult'] = test_checkresult
                Total_result.append(case_mess)
            except Exception as e:
                log.error(e)
        # print Total_result
        data = {}
        data["info"] = Total_result
        print data
        return data


if __name__ == '__main__':
    # # #
    test_runcase = Run_case()
    casedata = test_runcase.run_case(excel_path=excel_path, sheelname=sheelname)
    test_excel = create_excel_report(report_path)
    worksheet = test_excel._add_worksheet("测试总览")
    worksheet2 = test_excel._add_worksheet("测试详情")
    result = Analysis_rundata(casedata)
    try:
        test_excel.create_testinstruction(worksheet=worksheet, data=result)
    except Exception as E:
        print E
    try:
        test_excel.create_testinformation(worksheet=worksheet2, testsum=len(casedata["info"]), data=casedata)
    except Exception as E:
        print E
    #判断是否需要发送邮件
    if issendmail == True:
        mail = myMail()
        mail.send_mail(sender, psw, receiver, smtp_server, report_path, port)
    else:
        pass
