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
tk = dlxt.test_dl()['data']['token']

# 定义随机开票公司及开票类型
cities = ["MG", "YT", "YG", "HZ"]
types2 = {"MG": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票"],
          "YT": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票"],
          "YG": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票"],
          "HZ": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票"]}
city = random.choice(cities)
n2 = random.choice(types2.get(city))
print(city, n2)

# 定义8位随机开票号码
a = random.randint(99, 99999999)
# 定义99-399随机开票金额
b = random.randint(99, 399)


# 开票


def test_kp():
    # 开票URL
    kp_url = "http://192.168.0.217:9901/SalesArInvoice"
    # 开票请求头
    kp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 开票请求体
    kp_data = {"invoice_no": a, "invoice_time": "2023-01-30", "total_invoice_amount": b, "invoice_type": 53,
               "invoice_type_name": n2, "remark": "测试开票备注", "invoice_list": [
            {"business_no": "XD23010004", "kp_business_no": "", "invoice_amount": b,
             "not_invoice_amount": "403490.00"}], "invoice_company": city}
    # 开票请求
    r = requests.post(url=kp_url, json=kp_data, headers=kp_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置开票成功断言
    assert r.json()['message'] == 'success'


# test_kp()


# 收款


def test_skxj():
    # 收款现结URL
    skxj_url = "http://192.168.0.217:9901/SalesArReceive"
    # 收款请求头
    skxj_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 收款请求体
    skxj_data = {"usable_pre_amount": 0, "receive_time": "2023-01-24", "total_receive_amount": 199, "payment_mode": 66,
                 "payment_mode_name": "优果现金", "remark": "测试收款现结", "receive_list": [
            {"business_no": "XD22120168", "kp_business_no": "XD-2212-0449", "receive_amount": 199,
             "not_receive_amount": "863618.00", "offset_amount": 0, "pre_amount": 0}]}
    # 收款请求
    r = requests.post(url=skxj_url, json=skxj_data, headers=skxj_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置收款成功断言
    assert r.json()['message'] == 'success'


# test_skxj()


# 收款


def test_skcd():
    # 收款承兑URL
    skcd_url = "http://192.168.0.217:9901/SalesArReceipt"
    # 收款请求头
    skcd_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 收款请求体
    skcd_data = {"expire_time": "2024-01-30", "business_no": "XD22120168", "kp_business_no": "XD-2212-0449",
                 "receipt_id": 71, "receipt_name": "承兑汇票", "receipt_time": "2023-01-30", "receipt_amount": 199,
                 "remark": "测试承兑"}
    # 收款请求
    r = requests.post(url=skcd_url, json=skcd_data, headers=skcd_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置收款成功断言
    assert r.json()['message'] == 'success'


# test_skcd()


# 收款


def test_skzp():
    # 收款支票URL
    skzp_url = "http://192.168.0.217:9901/SalesArReceipt"
    # 收款请求头
    skzp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 收款请求体
    skzp_data = {"business_no": "XD22120168", "kp_business_no": "XD-2212-0449", "receipt_id": 70,
                 "receipt_name": "支票", "receipt_time": "2023-01-30", "expire_time": "", "receipt_amount": 199,
                 "remark": "测试支票"}
    # 收款请求
    r = requests.post(url=skzp_url, json=skzp_data, headers=skzp_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置收款成功断言
    assert r.json()['message'] == 'success'


# test_skzp()


# 退款


def test_tk1():
    # 退款URL
    tk1_url = "http://192.168.0.217:9901/SalesArRefund"
    # 退款请求头
    tk1_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 退款请求体
    tk1_data = {"business_no": "XD23010007", "kp_business_no": "", "refund_time": "2023-01-31", "refund_mode": 63,
                "refund_mode_name": "郢通上海银行", "refund_amount": 199, "refund_pre_amount": 0, "remark": "测试退款"}
    # 退款请求
    r = requests.post(url=tk1_url, json=tk1_data, headers=tk1_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置退款成功断言
    assert r.json()['message'] == 'success'


# test_tk1()


# 未税


def test_ws():
    # 未税URL
    ws_url = "http://192.168.0.217:9901/SalesArNoTax"
    # 未税请求头
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 未税请求体
    ws_data = {"business_no": "XD23010004", "kp_business_no": "", "refund_time": "", "refund_mode": "",
               "refund_mode_name": "", "refund_amount": "", "no_tax_amount": 199, "remark": "测试未税"}
    # 未税请求
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置未税成功断言
    assert r.json()['message'] == 'success'


# test_ws()


#  终止


def test_zz():
    # 终止URL
    zz_url = "http://192.168.0.217:9901/SalesArStop"
    # 终止请求头
    zz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {tk}"}
    # 终止请求体
    zz_data = {"business_no": "XD23010003", "kp_business_no": "XD-2212-0355", "stop_amount": 199, "remark": "测试终止"}
    # 终止请求
    r = requests.post(url=zz_url, json=zz_data, headers=zz_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 打印json返回数据
    # print(r.json())
    # 设置未税成功断言
    assert r.json()['message'] == 'success'

# test_zz()
