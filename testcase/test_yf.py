# coding=gbk
import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random
import pymysql


# 定义token
a = dlxt.test_dl()['data']['token']
# 定义金额
jine = random.randint(99, 399)
# 定义修改金额
xgjine = random.randint(99, 399)

# 开票
# 定义开票id
kaipiao = {'id': None}
kpid = kaipiao['id']
# 定义8位随机开票号码
kphm = random.randint(99, 99999999)
# 定义8位随机开票号码
xgkphm = random.randint(99, 99999999)
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
    # print(r.json())


# test_sckp()


# 查询发票操作记录
def test_cxfp():
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


# # test_cxfp()

# 定义付款id
fukuan = {'id': None}
fkid = fukuan['id']


# 付款
def test_fk():
    global fkid
    # 付款URL
    fk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    # 付款请求头
    fk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 付款请求体
    fk_data = {"payment_list": [
        {"payment_total_amount": jine, "payment_time": "2023-02-02T16:00:00.000Z", "payment_mode": 65,
         "payment_mode_name": "华胄现金"}], "remark": "测试付款", "order_list": [
        {"not_payment_amount": "9995884.00", "offset_amount": 0, "pre_payment_amount": 0,
         "usable_pre_payment_amount": "6181.00", "purchase_order_code": "87654321", "payment_amount": jine}]}
    # 付款请求
    r = requests.post(url=fk_url, json=fk_data, headers=fk_header)
    # 获取付款id更新到列表
    fukuan['id'] = r.json()['data']['id']
    fkid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置付款成功断言
    assert r.json()['message'] == 'success'
    # 打印json返回数据
    # print(r.json())


# test_fk()

# 删除收款
def test_scfk():
    # 删除收款URL
    scfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    # 删除收款请求头
    scfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 删除收款请求
    r = requests.delete(url=scfk_url, headers=scfk_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())


# test_scfk()


# 查询付款操作记录
def test_cxfk():
    global fkid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select payment_id,`type` from hz_erp_test.hz_purchase_ap_payment_log where payment_id ={fkid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxfk()


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
    zhekou['id'] = r.json()['data']['id']
    zkid = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
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
    # print(r.json())


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
    # print(r.json())


# test_sczk()

# 查询折扣操作记录
def test_cxzk():
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


# test_cxzk()


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
    # 打印json返回数据
    # print(r.json())


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
    # print(r.json())


# test_xgzz()


# 删除终止
def test_sczz():
    # 删除终止URL
    sczz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # 删除终止请求头
    sczz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 删除终止请求
    r = requests.delete(url=sczz_url, headers=sczz_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())


# test_sczz()


# 查询终止操作记录
def test_cxzz():
    global zzid
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select stop_id,`type` from hz_erp_test.hz_purchase_ap_stop_log where stop_id ={zzid}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxzz()


# 未税
# 定义未税id
weishui = {'id': None}
ws = weishui['id']


def test_ws():
    global ws
    # 未税URL
    ws_url = 'http://192.168.0.217:9901/PurchaseApNoTax'
    # 未税请求头
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 未税请求体
    ws_data = {"purchase_order_code": "87654321", "no_tax_amount": jine, "remark": "测试未税"}
    # 未税请求
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
    # 获取终止订单id更新到列表
    weishui['id'] = r.json()['data']['id']
    ws = r.json()['data']['id']
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置未税成功断言
    assert r.json()['message'] == 'success'
    # 打印json返回数据
    # print(r.json())


# test_ws()


# 修改未税


def test_xgws():
    global ws, weishui
    # 修改未税URL
    xgws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{ws}'
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
    # print(r.json())


# test_xgws()


# 删除未税
def test_scws():
    # 删除终止URL
    scws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{ws}'
    # 删除终止请求头
    scws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # 删除终止请求
    r = requests.delete(url=scws_url, headers=scws_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())


# test_scws()


# 查询未税操作记录
def test_cxws():
    global ws
    # 连接数据库
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('连接成功')
    # 创建一个游标对象
    yf = connect.cursor()
    # 精确查询操作日志
    sql_rz = f"select no_tax_id,`type` from hz_erp_test.hz_purchase_ap_no_tax_log where no_tax_id ={ws}"
    # 执行查询语句
    yf.execute(sql_rz)
    # 获取结果
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxws()


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
    # 打印json返回数据
    # print(r.json())

# test_yfk()
