# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/16 15:21 
# ide： PyCharm
import json
import time

import requests
import pandas as pd

url = "https://www.cantonfair.org.cn/api/exhibitsSreach/getSearchGoods"
catied = ['411002']
products = pd.DataFrame(
    columns=['productId', 'companyId', 'isBrand', 'companyNameEN', 'companyNameCN', 'productNamePinyin',
             'productNameCN', 'productNameEN', 'productHrefCN', 'productHrefEN', 'productH5HrefCN', 'productH5HrefEN',
             'companyHrefCN', 'companyHrefEN', 'companyH5HrefCN', 'companyH5HrefEN', 'threeDVR', 'descriptionCN',
             'descriptionEN', 'minPrice', 'maxPrice', 'moq', 'currency', 'isCf', 'isCfWinner', 'cfLevel', 'upTime',
             'upStatus', 'isExport', 'isOpen', 'companyLogo', 'categoryList', 'countryArea', 'logoList', 'imageList',
             'productTrait', 'domesticTrade', 'isNew', 'isSave', 'productKeyWordEN', 'productKeyWordCN', 'scopes',
             'tagNameCN', 'tagNameEN', 'page'])
for id in catied:
    # data为请求参数，模拟请求返回含有商品信息的json文件
    data = {"area": {"china": 0, "other": 0}, "busType": {"isProduct": 0, "isExport": 0, "other": 0},
            "companyType": {"isBrand": 0, "isGreen": 0, "isInvite": 0, "isAeo": 0, "isCf": 0, "isPoorSpecial": 0},
            "history": {"isFirst": 0, "isSecond": 0}, "productType": {"isNew": 0, "isCf": 0, "domesticSales": 0},
            "tradeType": {"isOem": 0, "isOBM": 0, "isCDM": 0}, "lang": "cn", "order": {"relevant": 1}, "pageIndex": 0,
            "searchType": "keyword", "pageSize": 60, "sessionId": "50ad2647-c75e-4e66-b05c-3d5f106ab1af", "keyword": "",
            "category": id, "isRecommend": 0}
    jumpJsonData = json.dumps(data)
    print(50 * '-')
    timeOut = 25
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        "Content-Type": "application/json"
    }
    res = requests.post(url, data=jumpJsonData, headers=headers, timeout=timeOut, allow_redirects=True)
    totalpage = json.loads(res.text)['data']['page']['totalPage']
    totalpage = min(totalpage, 50)
    # print(totalpage)
for i in range(0, totalpage):
    data = {"area": {"china": 0, "other": 0}, "busType": {"isProduct": 0, "isExport": 0, "other": 0},
            "companyType": {"isBrand": 0, "isGreen": 0, "isInvite": 0, "isAeo": 0, "isCf": 0, "isPoorSpecial": 0},
            "history": {"isFirst": 0, "isSecond": 0}, "productType": {"isNew": 0, "isCf": 0, "domesticSales": 0},
            "tradeType": {"isOem": 0, "isOBM": 0, "isCDM": 0}, "lang": "cn", "order": {"relevant": 1},
            "pageIndex": i, "searchType": "keyword", "pageSize": 60,
            "sessionId": "50ad2647-c75e-4e66-b05c-3d5f106ab1af", "keyword": "", "category": id, "isRecommend": 0}
    if i % 10 == 0:
        time.sleep(20)
    dumpJsonData = json.dumps(data)
    timeOut = 25
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.121 Safari/537.36',
        "Content-Type": "application/json"
    }
    res = requests.post(url, data=jumpJsonData, headers=headers, timeout=timeOut, allow_redirects=True)
    allitems = json.loads(res.text)['data']['list']
    items = []
    for item in allitems:
        item_info = []
        for key in item.keys():
            item_info.append(item[key])
            print(item[key])
        item_info.append(i)
        products.loc[len(products)] = item_info
products.to_csv('cantonfair.csv', encoding='utf_8_sig', index=False)

