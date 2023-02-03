# coding=gbk
import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random
import pymysql


# ����token
a = dlxt.test_dl()['data']['token']
# ������
jine = random.randint(99, 399)
# �����޸Ľ��
xgjine = random.randint(99, 399)

# ��Ʊ
# ���忪Ʊid
kaipiao = {'id': None}
kpid = kaipiao['id']
# ����8λ�����Ʊ����
kphm = random.randint(99, 99999999)
# ����8λ�����Ʊ����
xgkphm = random.randint(99, 99999999)
# ���忪Ʊδ��˰���
hs = jine * 0.85
# ���忪Ʊ��˰���
whs = jine * 0.15


def test_fp():
    global kpid
    # ��ƱURL
    fp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    # ��Ʊ����ͷ
    fp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ��Ʊ������
    fp_data = {"invoice_list": [
        {"invoice_total_amount": jine, "invoice_no": kphm, "invoice_time": "2023-02-01T16:00:00.000Z",
         "invoice_type": 86, "invoice_type_name": "��ֵ˰ר�÷�Ʊ-HZ(13%)",
         "invoice_info": [{"invoice_amount": whs, "invoice_tax_amount": hs, "invoice_tax_rate": whs}]}],
        "remark": "���Կ�Ʊ", "order_list": [
            {"customer_name": "�㽭�콡Զ���Ƽ����޹�˾", "purchase_order_code": "87654321", "invoice_amount": jine,
             "not_invoice_amount": "9996611.00"}]}
    # ��Ʊ����
    r = requests.post(url=fp_url, json=fp_data, headers=fp_header)
    # ��ȡ��Ʊid���µ��б�
    kaipiao['id'] = r.json()['data']['id']
    kpid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ���÷�Ʊ�ɹ�����
    assert r.json()['message'] == 'success'
    # ��ӡjson��������
    # print(r.json())


# test_fp()


# ɾ����Ʊ
def test_sckp():
    # ɾ����ƱURL
    sckp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{kpid}'
    # ɾ����Ʊ����ͷ
    sckp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ɾ����Ʊ����
    r = requests.delete(url=sckp_url, headers=sckp_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_sckp()


# ��ѯ��Ʊ������¼
def test_cxfp():
    global kpid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select invoice_id,`type` from hz_erp_test.hz_purchase_ap_invoice_log where invoice_id ={kpid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    print(rz)
    yf.close()


# # test_cxfp()

# ���帶��id
fukuan = {'id': None}
fkid = fukuan['id']


# ����
def test_fk():
    global fkid
    # ����URL
    fk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    # ��������ͷ
    fk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ����������
    fk_data = {"payment_list": [
        {"payment_total_amount": jine, "payment_time": "2023-02-02T16:00:00.000Z", "payment_mode": 65,
         "payment_mode_name": "�����ֽ�"}], "remark": "���Ը���", "order_list": [
        {"not_payment_amount": "9995884.00", "offset_amount": 0, "pre_payment_amount": 0,
         "usable_pre_payment_amount": "6181.00", "purchase_order_code": "87654321", "payment_amount": jine}]}
    # ��������
    r = requests.post(url=fk_url, json=fk_data, headers=fk_header)
    # ��ȡ����id���µ��б�
    fukuan['id'] = r.json()['data']['id']
    fkid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ���ø���ɹ�����
    assert r.json()['message'] == 'success'
    # ��ӡjson��������
    # print(r.json())


# test_fk()

# ɾ���տ�
def test_scfk():
    # ɾ���տ�URL
    scfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{fkid}'
    # ɾ���տ�����ͷ
    scfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ɾ���տ�����
    r = requests.delete(url=scfk_url, headers=scfk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_scfk()


# ��ѯ���������¼
def test_cxfk():
    global fkid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select payment_id,`type` from hz_erp_test.hz_purchase_ap_payment_log where payment_id ={fkid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxfk()


# �ۿ�
# �����ۿ�id
zhekou = {'id': None}
zkid = zhekou['id']


def test_zk():
    global zkid
    # �ۿ�URL
    zk_url = 'http://192.168.0.217:9901/PurchaseApDiscount'
    # �ۿ�����ͷ
    zk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # �ۿ�������
    zk_data = {"purchase_order_code": "87654321", "discount_amount": jine, "remark": "�����ۿ�"}
    # �ۿ�����
    r = requests.post(url=zk_url, json=zk_data, headers=zk_header)
    # ��ȡ�ۿ۶���id���µ��б�
    zhekou['id'] = r.json()['data']['id']
    zkid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # �����տ�ɹ�����
    assert r.json()['message'] == 'success'


# test_zk()


# �޸��ۿ�


def test_xgzk():
    global zkid
    # �޸��ۿ�URL
    xgzk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # �޸��ۿ�����ͷ
    xgzk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # �޸��ۿ�������
    xgzk_data = {"id": zhekou['id'], "purchase_order_code": "87654321", "discount_amount": xgjine,
                 "remark": "���Ա༭�ۿ�",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸��ۿ�����
    r = requests.put(url=xgzk_url, json=xgzk_data, headers=xgzk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_xgzk()

# ɾ���ۿ�
def test_sczk():
    # ɾ���ۿ�URL
    sczk_url = f'http://192.168.0.217:9901/PurchaseApDiscount/{zkid}'
    # ɾ���ۿ�����ͷ
    sczk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ɾ���ۿ�����
    r = requests.delete(url=sczk_url, headers=sczk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_sczk()

# ��ѯ�ۿ۲�����¼
def test_cxzk():
    global zkid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select discount_id,`type` from hz_erp_test.hz_purchase_ap_discount_log where discount_id ={zkid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxzk()


# ��ֹ
# ������ֹid
zhongzhi = {'id': None}
zzid = zhongzhi['id']


def test_zz():
    global zzid
    # ��ֹURL
    zz_url = 'http://192.168.0.217:9901/PurchaseApStop'
    # ��ֹ����ͷ
    zz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ��ֹ������
    zz_data = {"purchase_order_code": "87654321", "stop_amount": jine, "remark": "������ֹ"}
    # ��ֹ����
    r = requests.post(url=zz_url, json=zz_data, headers=zz_header)
    # ��ȡ��ֹ����id���µ��б�
    zhongzhi['id'] = r.json()['data']['id']
    zzid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ������ֹ�ɹ�����
    assert r.json()['message'] == 'success'
    # ��ӡjson��������
    # print(r.json())


# test_zz()


# �޸���ֹ


def test_xgzz():
    global zzid
    # �޸���ֹURL
    xgzz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # �޸���ֹ����ͷ
    xgzz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # �޸���ֹ������
    xgzz_data = {"id": zhongzhi['id'], "purchase_order_code": "87654321", "stop_amount": xgjine,
                 "remark": "���Ա༭��ֹ",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸���ֹ����
    r = requests.put(url=xgzz_url, json=xgzz_data, headers=xgzz_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_xgzz()


# ɾ����ֹ
def test_sczz():
    # ɾ����ֹURL
    sczz_url = f'http://192.168.0.217:9901/PurchaseApStop/{zzid}'
    # ɾ����ֹ����ͷ
    sczz_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ɾ����ֹ����
    r = requests.delete(url=sczz_url, headers=sczz_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_sczz()


# ��ѯ��ֹ������¼
def test_cxzz():
    global zzid
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select stop_id,`type` from hz_erp_test.hz_purchase_ap_stop_log where stop_id ={zzid}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxzz()


# δ˰
# ����δ˰id
weishui = {'id': None}
ws = weishui['id']


def test_ws():
    global ws
    # δ˰URL
    ws_url = 'http://192.168.0.217:9901/PurchaseApNoTax'
    # δ˰����ͷ
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # δ˰������
    ws_data = {"purchase_order_code": "87654321", "no_tax_amount": jine, "remark": "����δ˰"}
    # δ˰����
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
    # ��ȡ��ֹ����id���µ��б�
    weishui['id'] = r.json()['data']['id']
    ws = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ����δ˰�ɹ�����
    assert r.json()['message'] == 'success'
    # ��ӡjson��������
    # print(r.json())


# test_ws()


# �޸�δ˰


def test_xgws():
    global ws, weishui
    # �޸�δ˰URL
    xgws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{ws}'
    # �޸�δ˰����ͷ
    xgws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # �޸�δ˰������
    xgws_data = {"id": weishui['id'], "purchase_order_code": "87654321", "no_tax_amount": xgjine,
                 "remark": "���Ա༭δ˰",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸�δ˰����
    r = requests.put(url=xgws_url, json=xgws_data, headers=xgws_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_xgws()


# ɾ��δ˰
def test_scws():
    # ɾ����ֹURL
    scws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{ws}'
    # ɾ����ֹ����ͷ
    scws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ɾ����ֹ����
    r = requests.delete(url=scws_url, headers=scws_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())


# test_scws()


# ��ѯδ˰������¼
def test_cxws():
    global ws
    # �������ݿ�
    connect = pymysql.connect(host='192.168.0.226', user='root', password='CLd8T8TWt58ypaxd', db='hz_erp_test')
    if connect:
        print('���ӳɹ�')
    # ����һ���α����
    yf = connect.cursor()
    # ��ȷ��ѯ������־
    sql_rz = f"select no_tax_id,`type` from hz_erp_test.hz_purchase_ap_no_tax_log where no_tax_id ={ws}"
    # ִ�в�ѯ���
    yf.execute(sql_rz)
    # ��ȡ���
    rz = yf.fetchall()
    print(rz)
    yf.close()


# test_cxws()


# Ԥ������
# ����������Ӽ���Ԥ������
yfk = random.randint(-199, 399)


def test_yfk():
    # Ԥ����URL
    yfk_url = 'http://192.168.0.217:9901/PurchaseApCustomerPre'
    # Ԥ��������ͷ
    yfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # Ԥ����������
    yfk_data = {"total_pre_payment_amount": "", "customer_name": "�㽭�콡Զ���Ƽ����޹�˾", "payment_mode": 65,
                "payment_mode_name": "�����ֽ�", "payment_time": "2023-02-28", "pre_payment_amount": yfk,
                "remark": "��������Ԥ����"}
    # Ԥ��������
    r = requests.post(url=yfk_url, json=yfk_data, headers=yfk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ����Ԥ�������ɹ�����
    assert r.json()['message'] == 'success'
    # ��ӡjson��������
    # print(r.json())

# test_yfk()
