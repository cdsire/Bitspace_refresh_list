#!/usr/bin/python 
# -*- coding: utf-8 -*-
# File  : 2018/8/10
# Author: Administrator
# Date  : 11:52
# IDE   : PyCharm
# ----------------------------------------------

import time
import hashlib
import requests
import requests.packages.urllib3.util.ssl_
import json
import configparser
import random


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "ALL"

class BitZ_Mode():
    # 构造方法读取配置文件infor.conf中的参数
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read("infor.conf")
        self.Secret = parser.get("key", "Secret")
        self.ApiKey = parser.get("key", "ApiKey")
        self.TradePw = parser.get("key", "TradePw")
        self.URL = parser.get("key", "URL")
        self.TradeURL = parser.get("key", "tradeURL")
        self.AssetsURL = parser.get('key', "assetsURL")
        self.indent = random.randint(1,2)

    def httpGet(self, url):
        response = requests.get(url)
        return response

    def httpsPost(self, url, params):
        response = requests.post(url=url, params=params)
        return response

    # 签名
    def signature(self):
        iniSign = ''
        list = []
        for key in sorted(self.params.keys()):
            iniSign += key + '=' + str(self.params[key]) + '&'
            signs = iniSign[:-1]
            list.append(signs)
        sign = list[-1]
        data = sign + str(self.Secret)
        self.params['sign'] = hashlib.md5(data.encode("utf-8")).hexdigest().lower()
        return self.params['sign']

    # 提交委托单
    def addEntrustSheet(self, _type, price, number, symbol):
        """
        :param _type: 1:buy  2:sell
        :param price: order price
        :param number: trust order number
        :param symbol: Trading of column
        :return:
        """

        self.params = {}
        self.params['apiKey'] = self.ApiKey
        self.params['timeStamp'] = str(int(time.time()))
        self.params['nonce'] = str(int(time.time() % 1000000))
        self.params['type'] = str(_type)
        self.params['price'] = str(price)
        self.params['number'] = str(number)
        self.params['symbol'] = str(symbol)
        self.params['tradePwd'] = self.TradePw
        self.signature()
        __url = self.TradeURL + "addEntrustSheet"
        __response = BitZ_Mode().httpsPost(url=__url, params=self.params)
        return json.dumps(__response.json(), indent=self.indent)