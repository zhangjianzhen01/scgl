# coding=gbk
import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random

# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)

# 定义8位随机开票号码
kphm = random.randint(99, 99999999)
# 定义8位随机开票号码
xgkphm = random.randint(99, 99999999)
# 定义开票未含税金额
hs = jine * 0.85
# 定义开票含税金额
whs = jine * 0.15

# 定义token
a = dlxt.test_dl()['data']['token']
# 定义开票id
b = {'id': None}
c = b['id']


def test_fp():
    global c
    # 发票URL
    fp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    # 发票请求头
    fp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 发票请求体
    fp_data = {"invoice_list": [
        {"invoice_total_amount": jine , "invoice_no": kphm, "invoice_time": "2023-02-01T16:00:00.000Z",
         "invoice_type": 86, "invoice_type_name": "增值税专用发票-HZ(13%)",
         "invoice_info": [{"invoice_amount": whs, "invoice_tax_amount": hs, "invoice_tax_rate": whs}]}],
               "remark": "测试开票", "order_list": [
            {"customer_name": "浙江天健远见科技有限公司", "purchase_order_code": "87654321", "invoice_amount": jine,
             "not_invoice_amount": "9996611.00"}]}
    # 发票请求
    r = requests.post(url=fp_url, json=fp_data, headers=fp_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 获取发票订单id更新到列表
    b['id'] = r.json()['data']['id']
    c = r.json()['data']['id']
    # 打印json返回数据
    # print(r.json())
    # 设置发票成功断言
    assert r.json()['message'] == 'success'
    print(r.json())


# test_fp()


# 修改发票金额


def test_xgfp():
    global c
    # 修改发票URL
    xgfp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{c}'
    # 修改发票请求头
    xgfp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 修改发票请求体
    xgfp_data = {"id": b['id'], "remark": "测试修改开票内容", "creator_id": 1, "operate_id": 1, "invoice_list": [
        {"id": 2448, "invoice_id": b['id'], "invoice_total_amount": jine, "invoice_no": xgkphm,
         "invoice_time": "2023-02-02", "invoice_type": 86, "invoice_type_name": "增值税专用发票-HZ(13%)",
         "deleted_at": 0, "invoice_info": [
            {"id": 2473, "invoice_item_id": 2448, "invoice_amount": whs, "invoice_tax_amount": hs,
             "invoice_tax_rate": hs, "deleted_at": 0}]}], "order_list": [
        {"id": 3953, "invoice_id": b['id'], "purchase_order_code": "87654321", "invoice_amount": jine, "deleted_at": 0,
         "customer_name": "浙江天健远见科技有限公司", "not_invoice_amount": "9996385.00"}], "creator_name": "Admin",
                 "operate_name": "Admin"}
    # 修改未税请求
    r = requests.put(url=xgfp_url, json=xgfp_data, headers=xgfp_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    print(jine)
    print(xgjine)
    print(b)
