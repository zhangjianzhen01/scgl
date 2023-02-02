# coding=gbk
import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random

# 定义token
a = dlxt.test_dl()['data']['token']
# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)

# 折扣
# 定义折扣id
zhekou = {'id': None}
zkid = zhekou['id']


def test_zk():
    global zkid
    # 折扣URL
    zk_url = 'http://192.168.0.217:9901/PurchaseApDiscount'
    # 折扣请求头
    zk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 折扣请求体
    zk_data = {"purchase_order_code": "87654321", "discount_amount": jine, "remark": "测试折扣"}
    # 折扣请求
    r = requests.post(url=zk_url, json=zk_data, headers=zk_header)
    # 获取折扣订单id更新到列表
    zhekou['token'] = r.json()['data']['id']
    zkid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    # 设置收款成功断言
    assert r.json()['message'] == 'success'


# test_zk()


# 修改折扣


def test_xgzk():
    global zkid
    # 修改折扣URL
    xgzk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # 修改折扣请求头
    xgzk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 修改折扣请求体
    xgzk_data = {"id": zhekou['token'], "purchase_order_code": "87654321", "discount_amount": xgjine,
                 "remark": "测试编辑折扣",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # 修改折扣请求
    r = requests.put(url=xgzk_url, json=xgzk_data, headers=xgzk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    # print(jine)
    # print(xgjine)


# 终止
# 定义终止id
zhongzhi = {'id': None}
zzid = zhongzhi['id']


def test_zz():
    global zzid
    # 终止URL
    zz_url = 'http://192.168.0.217:9901/PurchaseApStop'
    # 终止请求头
    zz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 终止请求体
    zz_data = {"purchase_order_code": "87654321", "stop_amount": jine, "remark": "测试终止"}
    # 终止请求
    r = requests.post(url=zz_url, json=zz_data, headers=zz_header)
    # 获取终止订单id更新到列表
    zhongzhi['id'] = r.json()['data']['id']
    zzid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置终止成功断言
    assert r.json()['message'] == 'success'
    print(r.json())


# test_zz()


# 修改终止


def test_xgzz():
    global zzid
    # 修改终止URL
    xgzz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # 修改终止请求头
    xgzz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 修改终止请求体
    xgzz_data = {"id": zhongzhi['id'], "purchase_order_code": "87654321", "stop_amount": xgjine,
                 "remark": "测试编辑终止",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # 修改终止请求
    r = requests.put(url=xgzz_url, json=xgzz_data, headers=xgzz_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


# test_xgzz()

# 未税
# 定义终止id
weishui = {'id': None}
zzws = zhongzhi['id']


def test_ws():
    # 未税URL
    ws_url = 'http://192.168.0.217:9901/PurchaseApNoTax'
    # 未税请求头
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 未税请求体
    ws_data = {"purchase_order_code": "87654321", "no_tax_amount": jine, "remark": "测试未税"}
    # 未税请求
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置未税成功断言
    assert r.json()['message'] == 'success'
    print(r.json())


# test_ws()


# 修改未税


def test_xgws():
    global zzws
    # 修改未税URL
    xgws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{zzws}'
    # 修改未税请求头
    xgws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 修改未税请求体
    xgws_data = {"id": weishui['id'], "purchase_order_code": "87654321", "no_tax_amount": xgjine,
                 "remark": "测试编辑未税",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # 修改未税请求
    r = requests.put(url=xgws_url, json=xgws_data, headers=xgws_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


# 预付款变更
# 定义随机增加减少预付款金额
yfk = random.randint(-199, 399)


def test_yfk():
    # 预付款URL
    yfk_url = 'http://192.168.0.217:9901/PurchaseApCustomerPre'
    # 预付款请求头
    yfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 预付款请求体
    yfk_data = {"total_pre_payment_amount": "", "customer_name": "浙江天健远见科技有限公司", "payment_mode": 65,
                "payment_mode_name": "华胄现金", "payment_time": "2023-02-28", "pre_payment_amount": yfk,
                "remark": "测试新增预付款"}
    # 预付款请求
    r = requests.post(url=yfk_url, json=yfk_data, headers=yfk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置预付款变更成功断言
    assert r.json()['message'] == 'success'
    print(r.json())

# test_ws()
