#!/usr/bin/python 
# -*- coding: utf-8 -*-
# File  : 2018/8/10
# Author: Administrator
# Date  : 11:03
# IDE   : PyCharm
# ----------------------------------------------
import random

from refresh_list.Bit_Z_refresh_list.api_mode import BitZ_Mode



#提交委托单
def addEntrustSheet():
    a = BitZ_Mode()
    _type = str(a.indent)             #买：1  卖：2
    buy_price = str(random.uniform(0.00000064, 0.00000070))
    sell_price = str(random.uniform(0.00000064, 0.00000070))
    if _type == "1":
        price = buy_price          #价格
    else:
        price = sell_price
    number = str(random.uniform(10, 30))            #数量
    symbol = 'eth_eds'      #交易对
    print(BitZ_Mode().addEntrustSheet(_type,price,number,symbol))


if __name__ == '__main__':
    addEntrustSheet()