# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/15 14:27 
# ide： PyCharm

import requests
from Conf.conf import *
from common.get_excel_data import *
import pytest
import json
from common.Request import RequestsHandler
from requests import session
from common.Logs import Log
from common.Yaml_Data import HandleYaml

handleyaml = HandleYaml()
yamldict = handleyaml.get_data()

log = Log(__name__)
logger = log.Logger


def test_login_pass():
    login_url = server_ip('test') + yamldict['test_login_pass']["url"]
    # username, password = get_excel_value(1)
    # params = {
    #     "email": username,
    #     "user_pwd": password,
    #     "ajax": 1,
    #     "auto_login": 1
    # }

    login_result = RequestsHandler().post_Req(url=login_url, data=yamldict['test_login_pass']["params"])
    re_login_cookie = login_result.cookies
    content = login_result.text.encode('utf-8').decode('unicode_escape')
    statusCode = content["status"]
    print(statusCode)
    try:
        assert statusCode == 2, "登录失败"
        logger.info("statusCode返回正确-----》 %s", statusCode)
        return re_login_cookie
    except Exception:
        logger.error("statusCode返回错误-----》 %s", statusCode)
        raise


def test_login_name_error():
    login_url = server_ip('test') + yamldict['test_login_pass']['url']
    # username, name_error = get_excel_value(2)
    #
    # params = {
    #     "email": username,
    #     "user_pwd": name_error,
    #     "ajax": 1,
    #     "auto_login": 1
    #
    # }

    login_result = RequestsHandler().post_Req(url=login_url, data=yamldict['test_login_pass']["paramsErrorUsername"])
    re_login_cookie = login_result.cookies
    content = login_result.text.encode('utf-8').decode('unicode_escape')
    content = json.loads(content)
    statusCode = content["status"]
    print(statusCode)
    try:
        assert statusCode == 0, "登录异常"
        logger.info("statusCode返回正确，用户名错误无法登录逻辑正确------》 %s", statusCode)
        return re_login_cookie
    except Exception:
        logger.error("statusCode返回错误------》 %s", statusCode)
        raise


def test_login_pass_error():
    login_url = server_ip('test') + yamldict['test_login_pass']["url"]
    # username, password_error = get_excel_value(3)
    #
    # params = {
    #     "email": username,
    #     "user_pwd": password_error,
    #     "ajax": 1,
    #     "auto_login": 1
    #
    # }

    login_result = RequestsHandler().post_Req(url=login_url, data=yamldict['test_login_pass']["paramsErrorPassword"])
    re_login_cookie = login_result.cookies
    content = login_result.text.encode('utf-8').decode('unicode_escape')
    content = json.loads(content)
    statusCode = content["status"]
    print(statusCode)
    try:
        assert statusCode == 0, "登录异常"
        logger.info("statusCode返回正确，密码错误无法登录逻辑正确------》 %s", statusCode)
        return re_login_cookie
    except Exception:
        logger.error("statusCode返回错误------》 %s", statusCode)
        raise
