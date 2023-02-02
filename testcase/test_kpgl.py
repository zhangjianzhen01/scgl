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
types2 = {"MG": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票", "全电普票"],
          "YT": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票", "全电普票", "全电专票"],
          "YG": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票", "全电普票", "全电专票"],
          "HZ": ["其他", "N类", "未开票收入", "增值税普通发票", "增值税专用发票", "全电普票", "全电专票"]}
city = random.choice(cities)
n2 = random.choice(types2.get(city))

# 定义未开票id
wkpid = {'data': None}
# 定义8位随机开票号码
a = random.randint(99, 99999999)
# 定义99-399随机开票金额
b = random.randint(99, 399)
# 定义开票未含税金额
c = b * 0.85
# 定义开票含税金额
d = b * 0.15


# 销售申请开票


def test_sq():
    # 申请开票URL
    sq_url = 'http://192.168.0.217:9901/ApplyInvoice'
    # 申请请求头
    sq_header = {"content-type": "application/json", "authorization": f"Bearer {tk}"}
    # 申请请求体
    sq_data = {"invoice_remark": "测试申请发票备注", "invoice_title": "云南天奥信息技术有限公司",
               "invoice_tax": "91530121MA6P3HH01D",
               "address_and_tel": "云南省昆明市呈贡区吴家营街道万溪冲社区科技信息产业创新孵化中心研发办公楼A座5层18382305195",
               "bank_and_no": "中国工商银行股份有限公司昆明花园支行2502124109100030340", "invoice_email": "",
               "invoice_company": city, "invoice_term": "2023-02-10", "invoice_type": 101, "invoice_follow": 1,
               "invoice_total_amount": b, "express_address": "上海市普陀区中江路879号", "express_people": "测试",
               "express_tel": "13916271128", "remark": "测试销售申请开票备注", "enclosure": [],
               "order_list": [{"business_no": "XD23020001", "kp_business_no": "", "invoice_amount": b}],
               "content_list": [
                   {"product_name": "测试", "product_module": "tv", "product_quantity": 1, "product_price": b,
                    "product_amount": b, "product_unit": "个", "tax_amount": "", "tax_rate": 13, "no_tax_amount": ""}],
               "id": 0, "invoice_type_name": n2}
    # 申请请求
    r = requests.post(url=sq_url, json=sq_data, headers=sq_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 申请成功断言
    assert r.json()['message'] == 'success'
    # 打印json返回数据
    print(r.json())
    # 更新未开票id传参给下个线程
    wkpid['data'] = r.json()['data']


# test_sq()


# 财务确认开票

def test_qr():
    global wkpid, a

    # 确认开票URL
    qr_url = 'http://192.168.0.217:9901/AInvoice/invoice'
    # 确认请求头
    qr_header = {"content-type": "application/json", "authorization": f"Bearer {tk}"}
    # 确认请求体
    qr_data = {"dict_img": "https://hzdefault-1304855126.cos.ap-nanjing.myqcloud.com/fapiao/pic-fapiao-title05.png",
               "seller_info": {"id": 4, "alias_name": city, "invoice_title": "上海魔鸽数据科技有限公司",
                               "invoice_tax": "91310107MA1G19U98W", "address_and_tel": "", "bank_and_no": ""},
               "content_list": [
                   {"id": 6949, "apply_invoice_id": wkpid['data'], "product_name": "测试", "product_module": "tv",
                    "product_quantity": 1, "product_price": b, "product_amount": b, "product_unit": "台",
                    "tax_amount": d, "tax_rate": 13, "no_tax_amount": c, "no_tax_price": c,
                    "deleted_at": 0, "common_product_name": "*电子计算机整机*"}], "invoice_company": city,
               "apply_invoice_id": wkpid['data'], "invoice_no": a, "invoice_time": "2023-02-10",
               "total_invoice_amount": c, "invoice_type": 101, "invoice_type_name": n2,
               "remark": "测试财务开票备注", "enclosure": [], "invoice_list": [
            {"id": 5195, "apply_invoice_id": wkpid['data'], "business_no": "XD23020001", "kp_business_no": "",
             "invoice_amount": b, "status": 0, "deleted_at": 0, "customer_name": "云南天奥信息技术有限公司",
             "invoiced_amount": "0.00", "apply_not_invoice_amount": "5953500.00"}]}
    # 确认请求
    r = requests.post(url=qr_url, json=qr_data, headers=qr_header)
    # 输出日志
    logger.logger.debug(f'发送请求:{r}')
    # 申请成功断言
    assert r.json()['message'] == 'success'
    # 打印json返回数据
    print(r.json())
    print(city, n2)

# test_sq()
