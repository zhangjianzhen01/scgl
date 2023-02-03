# coding=gbk

import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random
import json

# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)

# 定义token
a = dlxt.test_dl()['data']['token']
# 定义开票id
b = {'id': None}
c = b['id']


def test_fk():
    global c
    # 付款URL
    fk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    # 付款请求头
    fk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 付款请求体
    fk_data = {"payment_list": [
        {"payment_total_amount": 199, "payment_time": "2023-02-02T16:00:00.000Z", "payment_mode": 65,
         "payment_mode_name": "华胄现金"}], "remark": "测试付款", "order_list": [
        {"not_payment_amount": "9995884.00", "offset_amount": 0, "pre_payment_amount": 0,
         "usable_pre_payment_amount": "6181.00", "purchase_order_code": "87654321", "payment_amount": 199}]}
    # 付款请求
    r = requests.post(url=fk_url, json=fk_data, headers=fk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 获取付款订单id更新到列表
    b['id'] = r.json()['data']['id']
    c = r.json()['data']['id']
    # 打印json返回数据
    # print(r.json())
    # 设置付款成功断言
    assert r.json()['message'] == 'success'
    print(r.json())


# test_fk()


# 修改发票金额
def test_xgfk():
    global c
    # 修改付款URL
    xgfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{c}'
    # 修改付款请求头
    xgfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 修改付款请求体
    xgfk_data = {"id": b['id'], "remark": "测试修改开票付款", "creator_id": 1, "operate_id": 1, "payment_list": [
        {"id": 2029, "payment_id": b['id'], "payment_time": "2023-02-03", "payment_total_amount": 99, "payment_mode": 65,
         "payment_mode_name": "华胄现金", "deleted_at": 0}], "order_list": [
        {"id": 3727, "payment_id": b['id'], "purchase_order_code": "87654321", "payment_amount": 99,
         "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0, "customer_name": "浙江天健远见科技有限公司",
         "not_payment_amount": "9995585.00", "usable_pre_payment_amount": "6181.00"}], "creator_name": "Admin",
                 "operate_name": "Admin"}

    data = json.dumps(xgfk_data)
    # 修改未税请求
    r = requests.put(url=xgfk_url, json=data, headers=xgfk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    print(jine)
    print(xgjine)
    print(b)
    print(c)
    print(data)
    print(xgfk_url)

