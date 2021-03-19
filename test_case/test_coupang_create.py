# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/17 17:54 
# ide： PyCharm
import json

import requests

from common.Logs import Log
from common.Request import RequestsHandler

log = Log(__name__)
logger = log.Logger


def test_coupon_create():
    create_url = "https://www.cantonfair.org.cn/api/exhibitsSreach/getSearchGoods"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36 '
    }
    data = {"area": {"china": 0, "other": 0}, "busType": {"isProduct": 0, "isExport": 0, "other": 0},
            "companyType": {"isBrand": 0, "isGreen": 0, "isInvite": 0, "isAeo": 0, "isCf": 0, "isPoorSpecial": 0},
            "history": {"isFirst": 0, "isSecond": 0}, "productType": {"isNew": 0, "isCf": 0, "domesticSales": 0},
            "tradeType": {"isOem": 0, "isOBM": 0, "isCDM": 0}, "lang": "cn", "order": {"relevant": 1},
            "pageIndex": 1, "searchType": "keyword", "pageSize": 60,
            "sessionId": "50ad2647-c75e-4e66-b05c-3d5f106ab1af", "keyword": "", "category": id, "isRecommend": 0}

    # r = RequestsHandler().post_Req(url=create_url, data=data, headers=headers)
    r = RequestsHandler().post_Req(url=create_url)
    statusCode = r.status_code

    print(statusCode)

    try:
        assert statusCode == 200, "返回状态码错误，接口请求失败"

        logger.info("statusCode返回正确-----> %s", statusCode)
    except Exception:
        logger.error("statusCode返回错误-----》 %s", statusCode)
        raise
