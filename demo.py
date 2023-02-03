# -*- coding:utf-8 -*-   #转码
import pymysql
# 调用requests库
import requests
# 调用random库
import random
# 调用日志代码
import business.logger
from business import logger
# 调用登录系统代码
import business.dlxt
from business import dlxt
# 定义token
a = dlxt.test_dl()['data']['token']
# 开票
# 定义开票id
kaipiao = {'id': None}
kpid = kaipiao['id']
# 定义8位随机开票号码
kphm = random.randint(99, 99999999)
# 定义8位随机开票号码
xgkphm = random.randint(99, 99999999)
# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)
# 定义开票未含税金额
hs = jine * 0.85
# 定义开票含税金额
whs = jine * 0.15


def test_fp():
    global kpid
    # 发票URL
    fp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    # 发票请求头
    fp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 发票请求体
    fp_data = {"invoice_list": [
        {"invoice_total_amount": jine, "invoice_no": kphm, "invoice_time": "2023-02-01T16:00:00.000Z",
         "invoice_type": 86, "invoice_type_name": "增值税专用发票-HZ(13%)",
         "invoice_info": [{"invoice_amount": whs, "invoice_tax_amount": hs, "invoice_tax_rate": whs}]}],
        "remark": "测试开票", "order_list": [
            {"customer_name": "浙江天健远见科技有限公司", "purchase_order_code": "87654321", "invoice_amount": jine,
             "not_invoice_amount": "9996611.00"}]}
    # 发票请求
    r = requests.post(url=fp_url, json=fp_data, headers=fp_header)
    # 获取开票id更新到列表
    kaipiao['id'] = r.json()['data']['id']
    kpid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置发票成功断言
    assert r.json()['message'] == 'success'
    # 打印json返回数据
    # print(r.json())


# test_fp()


# 删除开票
def test_sckp():
    # 删除发票URL
    sckp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    # 删除发票请求头
    sckp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 删除发票请求
    r = requests.delete(url=sckp_url, headers=sckp_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())


# test_sckp()


# 查询发票操作记录
def test_查询发票操作日志():
    global kpid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select invoice_id,`type` from hz_erp_test.hz_purchase_ap_invoice_log where invoice_id ={kpid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    print(rz)
    yf.close()


# # test_查询发票操作日志()