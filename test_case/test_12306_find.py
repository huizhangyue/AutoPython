# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/15 13:38 
# ide： PyCharm

import requests
from common.Request import RequestsHandler
from common.Logs import Log
from Conf.conf import *

log = Log(__name__)
logger = log.Logger


def test_find12306_care():
    find_url = "https://kyfw.12306.cn/otn/leftTicket/queryT"
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 83.0.4103.97Safari / 537.36'
        ,
        'Cookie': '_uab_collina=161544183234765335496295; JSESSIONID=B90217EAC34540B11F0F2885DE3C6CA5; BIGipServerotn=133169674.38945.0000; RAIL_EXPIRATION=1615739643443; RAIL_DEVICEID=VjKjGkPV3U8fxI1yECgj-SFyiy9PP1P_NEVygkhOzV72ax0KqucIlXEQRxZb04RXMwpQK-pXGHFFF2pexNU6ZcjUMB_R6z9FVVUlAApl1nbD7sudatMGY1A_Dc_tvAO_v4wZZF-3XfRZPYhMFqN4OnJlXXoJQhkp; BIGipServerpool_passport=132383242.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2021-03-11; _jc_save_toDate=2021-03-11; _jc_save_wfdc_flag=dc'
    }
    data = {
        "cxlx": 0,
        "cz": "上海",
        "cc": "G7259",
        "czEn": '-E4-B8-8A-E6-B5-B7',
        "randCode": ''
    }

    r = RequestsHandler().post_Req(url=find_url, data=data, headers=headers)
    # r = requests.get(url= find_url, data=data,headers=headers)
    # print('_' * 50)
    # print(r.content.decode())
    # print(r)
    # print(r.text.encode('utf-8').decode('unicode_escape'))
    statusCode = r.status_code
    # c = r.status_code
    # print(c)
    # return statusCode
    print(statusCode)
    try:
        assert statusCode == 200, "返回状态码错误，接口请求失败"

        logger.info("statusCode返回正确-----》%s", statusCode)
    except Exception:
        logger.error("statusCode返回错误-----》 %s", statusCode)
        raise