# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/15 14:49 
# ide： PyCharm

from test_case.test_login import *
from common.Logs import Log

log = Log(__name__)
logger = log.Logger


def test_login():
    """
    定义一个全局变量，用来返回登录后的cookies，避免在pytest框架中重复操作
    :return:
    """

    global re_login_cookie
    login_url = server_ip('test') + "/fanwe/index.php?ctl=user&act=dologin&fhash" \
                                    "=IzHHyOyDiNsiYYYbamPlHqPQuWrWsCPGUKafBrbgqEymWQcfUP "
    username, password = get_excel_value(1)

    params = {
        "email": username,
        "user_pwd": password,
        "ajax": 1,
        "auto_login": 1
    }

    log = requests.post(url=login_url, data=params)
    re_login_cookie = log.cookies

def test_add_address():
    """
    登录后向个人信息中添加收获地址
    :return:
    """

    c_url = server_ip('test') + yamldict['test_add_address']["url"]
    #
    # data = {
    #     "consignee": "dr",
    #     "address": "drdrdr",
    #     "mobile": "13212345678",
    #     "ajax": 1,
    #     "id": ""
    # }
    re_login_cookie = test_login_pass()
    r_a = requests.post(url=c_url, data=yamldict['test_add_address']["data"], cookies=re_login_cookie)
    content = r_a.text.encode('utf-8').decode('unicode_escape')
    content = json.loads(content)
    logger.info("接口返回内容-----》 %s", content)
    statusCode = content["status"]
    print(statusCode)

    try:
        assert statusCode == 1, "添加地址失败！"
        logger.info("statusCode返回正确-----> %s", statusCode)

    except Exception:
        logger.info("statusCode返回错误-----》 %s", statusCode)
        raise
