# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/16 19:33 
# ide： PyCharm
import requests
import time
import pandas as pd
import json

url = "https://www.cantonfair.org.cn/api/exhibitsSreach/getSearchCompany"
cateid = ['411002']
products = pd.DataFrame(
    columns=['productId', 'companyId', 'isBrand', 'companyNameEN', 'companyNameCN', 'productNamePinyin',
             'productNameCN', 'productNameEN', 'productHrefCN', 'productHrefEN', 'productH5HrefCN', 'productH5HrefEN',
             'companyHrefCN', 'companyHrefEN', 'companyH5HrefCN', 'companyH5HrefEN', 'threeDVR', 'descriptionCN',
             'descriptionEN', 'minPrice', 'maxPrice', 'moq', 'currency', 'isCf', 'isCfWinner', 'cfLevel', 'upTime',
             'upStatus', 'isExport', 'isOpen', 'companyLogo', 'categoryList', 'countryArea', 'logoList', 'imageList',
             'productTrait', 'domesticTrade', 'isNew', 'isSave', 'productKeyWordEN', 'productKeyWordCN', 'scopes',
             'tagNameCN', 'tagNameEN', 'page'])
for id in cateid:
    data = {"area": {"china": 0, "other": 0}, "busType": {"isProduct": 0, "isExport": 0, "other": 0},
            "companyType": {"isBrand": 0, "isGreen": 0, "isInvite": 0, "isAeo": 0, "isCf": 0, "isPoorSpecial": 0},
            "history": {"isFirst": 0, "isSecond": 0}, "productType": {"isNew": 0, "isCf": 0, "domesticSales": 0},
            "tradeType": {"isOem": 0, "isOBM": 0, "isCDM": 0}, "lang": "cn", "order": {"relevant": 1}, "pageIndex": 0,
            "searchType": "keyword", "pageSize": 60, "sessionId": "50ad2647-c75e-4e66-b05c-3d5f106ab1af", "keyword": "",
            "category": id, "isRecommend": 0}
    jumpJsonData = json.dumps(data)
    timeOut = 25
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        "Content-Type": "application/json"
    }
    res = requests.post(url, headers=headers, data=jumpJsonData, timeout=timeOut, allow_redirects=True)
    totalpage = json.loads(res.text)['data']['page']['totalPage']
    print(totalpage)
    totalpage = min(totalpage, 50)
    for i in range(0, totalpage):
        data = {"area": {"china": 0, "other": 0}, "busType": {"isProduct": 0, "isExport": 0, "other": 0},
                "companyType": {"isBrand": 0, "isGreen": 0, "isInvite": 0, "isAeo": 0, "isCf": 0, "isPoorSpecial": 0},
                "history": {"isFirst": 0, "isSecond": 0}, "productType": {"isNew": 0, "isCf": 0, "domesticSales": 0},
                "tradeType": {"isOem": 0, "isOBM": 0, "isCDM": 0}, "lang": "cn", "order": {"relevant": 1},
                "pageIndex": i, "searchType": "keyword", "pageSize": 60,
                "sessionId": "50ad2647-c75e-4e66-b05c-3d5f106ab1af", "keyword": "", "category": id, "isRecommend": 0}
        if i % 10 == 0:
            time.sleep(5)
            dumpJsonData = json.dumps(data)
            timeOut = 20
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
                # print(item_info[1])
                # item = []
                for key in item.keys():
                    item_info.append(item[key])
                    print(item[key])
    # print("-" * 100)
                item_info.append(i)
                products.loc[len(products)] = item_info
    #             print(item_info)
    #         print(allitems)
