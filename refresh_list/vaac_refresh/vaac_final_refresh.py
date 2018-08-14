#!/usr/bin/python 
# -*- coding: utf-8 -*-
import json
import requests
import random
import time
import threading
from hashlib import md5


# 刷单类
class RefreshTransaction:
    def __init__(self, phone, password, passwd):
        self.phone = phone  # 登录手机号
        self.password = password  # 登录密码
        self.passwd = passwd  # 交易密码
        self.session = requests.session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        self.contract_type_list = ["71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
                              "92", "93", "94", "95", "96", "97", "98", "99", "100"]

    # 对密码进行md5加密方法
    def Password_encryption(self, password):
        pwd = md5()
        pwd.update(password.encode())

        # 返回加密过后的密码
        return pwd.hexdigest()

    # 登录方法
    def login(self):
        # 登录接口
        login_url = "http://exchang.dev1.xsl.ph/api/json/user/login.do"
        # 登录FormData
        postData = {
            "phone": self.phone,
            "imgCode": "123456#1",
            "password": self.Password_encryption(self.password),
            "countryCode": "86"
        }

        # 返回登录过后的状态
        return self.session.post(login_url, data=postData, headers=self.headers)

    # 交易方法
    def transaction(self, contractType, orderPrice, orderQty, orderType, bsFlag):
        transaction_url = 'http://exchang.dev1.xsl.ph/api/json/user/torder.do'
        transaction_data = {
            "orderPrice": orderPrice,  # 订单价格
            "orderQty": orderQty,  # 订单数量
            "orderType": orderType,  # 订单类型，目前都是1
            "contractType": contractType,  # 交易类型
            "passwd": self.Password_encryption(self.passwd),  # 交易密码
            "bsFlag": bsFlag  # 买卖标识：1=买， 2=卖
        }

        return self.session.post(url=transaction_url, headers=self.headers, data=transaction_data)

r = RefreshTransaction(phone="13924379750", password="Cdsire0124", passwd="625280")
def deal(begin, end):
    global r
    num = 0

    # 登录返回的json
    data = json.loads(r.login().text)

    for i in range(begin,end):
        # 如果登录成功
        if data['success']:
            contract_type = random.choice(r.contract_type_list)

            if contract_type == "71":
                price = str(random.uniform(0.05084512, 0.08492288))
                number = str("%.2f" % (random.uniform(0.1, 3)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_ETH --- 交易成功')
                else:
                    print("BTC_ETH --- 交易失败")

            if contract_type == "72":
                price = str(random.uniform(0.01170842, 0.02045758))
                number = str("%.2f" % (random.uniform(0.1, 20)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_LTC --- 交易成功')
                else:
                    print("BTC_LTC --- 交易失败")

            if contract_type == "73":
                price = str(random.uniform(0.00007817, 0.00011273))
                number = str("%.2f" % (random.uniform(0.1, 100)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_XRP --- 交易成功')
                else:
                    print("BTC_XRP --- 交易失败")

            if contract_type == "74":
                price = str(random.uniform(0.00005455, 0.00011331))
                number = str("%.2f" % (random.uniform(0.1, 3000)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_VAAC --- 交易成功')
                else:
                    print("BTC_VAAC --- 交易失败")

            if contract_type == "75":
                price = str(random.uniform(0.00000578, 0.00000886))
                number = str("%.2f" % (random.uniform(0.1, 500)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_CSC --- 交易成功')
                else:
                    print("BTC_CSC --- 交易失败")

            if contract_type == "76":
                price = str(random.uniform(0.00000369, 0.00000765))
                number = str("%.2f" % (random.uniform(0.1, 240)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_CFC --- 交易成功')
                else:
                    print("BTC_CFC --- 交易失败")

            if contract_type == "77":
                price = str(random.uniform(0.00010114, 0.00024228))
                number = str("%.2f" % (random.uniform(0.1, 520)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_NLC --- 交易成功')
                else:
                    print("BTC_NLC --- 交易失败")

            if contract_type == "78":
                price = str(random.uniform(0.00000585, 0.00001115))
                number = str("%.2f" % (random.uniform(0.1, 152)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_FTCT --- 交易成功')
                else:
                    print("BTC_FTCT --- 交易失败")

            if contract_type == "79":
                price = str(random.uniform(0.00000047, 0.00000085))
                number = str("%.2f" % (random.uniform(0.1, 132)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_DOGE --- 交易成功')
                else:
                    print("BTC_DOGE --- 交易失败")

            if contract_type == "80":
                price = str(random.uniform(0.00000054, 0.00000084))
                number = str("%.2f" % (random.uniform(0.1, 91)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('BTC_SWTC --- 交易成功')
                else:
                    print("BTC_SWTC --- 交易失败")

            if contract_type == "92":
                price = str(random.uniform(0.17635801, 0.24056399))
                number = str("%.2f" % (random.uniform(0.1, 10)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_LTC --- 交易成功')
                else:
                    print("ETH_LTC --- 交易失败")

            if contract_type == "93":
                price = str(random.uniform(0.00127584, 0.00163372))
                number = str("%.2f" % (random.uniform(0.1, 100)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_XRP --- 交易成功')
                else:
                    print("ETH_XRP --- 交易失败")

            if contract_type == "94":
                price = str(random.uniform(0.00114337, 0.00178835))
                number = str("%.2f" % (random.uniform(0.1, 300)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_VAAC --- 交易成功')
                else:
                    print("ETH_VAAC --- 交易失败")

            if contract_type == "95":
                price = str(random.uniform(0.00008937, 0.00012341))
                number = str("%.2f" % (random.uniform(0.1, 250)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_CSC --- 交易成功')
                else:
                    print("ETH_CSC --- 交易失败")

            if contract_type == "96":
                price = str(random.uniform(0.00006744, 0.00009746))
                number = str("%.2f" % (random.uniform(0.1, 452)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_CFC --- 交易成功')
                else:
                    print("ETH_CFC --- 交易失败")

            if contract_type == "97":
                price = str(random.uniform(0.00218019, 0.00281451))
                number = str("%.2f" % (random.uniform(0.1, 280)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_NLC --- 交易成功')
                else:
                    print("ETH_NLC --- 交易失败")

            if contract_type == "98":
                price = str(random.uniform(0.00008820, 0.00014668))
                number = str("%.2f" % (random.uniform(0.1, 157)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_FTCT --- 交易成功')
                else:
                    print("ETH_FTCT --- 交易失败")

            if contract_type == "99":
                price = str(random.uniform(0.00000821, 0.00001095))
                number = str("%.2f" % (random.uniform(0.1, 174)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_DOGE --- 交易成功')
                else:
                    print("ETH_DOGE --- 交易失败")

            if contract_type == "100":
                price = str(random.uniform(0.00000807, 0.00001205))
                number = str("%.2f" % (random.uniform(0.1, 241)))
                order_type = "1"
                flag = str(random.randint(1, 2))

                # 交易返回的json
                da = json.loads(r.transaction(contract_type, price, number, order_type, flag).text)
                if da['success']:
                    print('ETH_SWTC --- 交易成功')
                else:
                    print("ETH_SWTC --- 交易失败")

        else:
            print('登陆失败')

        num += 1
        print("第 [%d] 次刷单。" % (num))


if __name__ == '__main__':
    print("start....")
    start_time = time.time()
    num = 0
    thread_list = []
    for i in range(200):
        t = threading.Thread(target=deal, args=(1,501))
        thread_list.append(t)

    for t in thread_list:
        t.start()
    t.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("**************************************刷单耗时：%.2f" % (elapsed_time))

    print('**************************************main over')
