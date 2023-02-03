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

# 折扣
# 定义折扣id
zhekou = {'id': None}
zkid = zhekou['id']
# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)


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
    zhekou['id'] = r.json()['data']['id']
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
    xgzk_data = {"id": zhekou['id'], "purchase_order_code": "87654321", "discount_amount": xgjine,
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


# test_xgzk()

# 删除折扣
def test_sczk():
    # 删除折扣URL
    sczk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # 删除折扣请求头
    sczk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 删除折扣请求
    r = requests.delete(url=sczk_url, headers=sczk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    print(r.json())
    print(zkid)


# test_sczk()

def test_cxrz():
    global zkid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select discount_id,`type` from hz_erp_test.hz_purchase_ap_discount_log where discount_id ={zkid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    print(rz)
    yf.close()

# test_cxrz()
