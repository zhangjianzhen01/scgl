# coding=gbk
import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random

# ����token
a = dlxt.test_dl()['data']['token']
# ������
jine = random.randint(99, 399)
# �����޸Ľ��
xgjine = random.randint(99, 399)

# ��Ʊ
# ���忪Ʊid
b = {'id': None}
c = b['id']
# ����8λ�����Ʊ����
kphm = random.randint(99, 99999999)
# ����8λ�����Ʊ����
xgkphm = random.randint(99, 99999999)
# ���忪Ʊδ��˰���
hs = jine * 0.85
# ���忪Ʊ��˰���
whs = jine * 0.15


def test_fp():
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
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ���÷�Ʊ�ɹ�����
    assert r.json()['message'] == 'success'
    print(r.json())


# test_fp()

# ����
def test_fk():
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
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ���ø���ɹ�����
    assert r.json()['message'] == 'success'
    print(r.json())


# test_fk()


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
    zhekou['token'] = r.json()['data']['id']
    zkid = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
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
    xgzk_data = {"id": zhekou['token'], "purchase_order_code": "87654321", "discount_amount": xgjine,
                 "remark": "���Ա༭�ۿ�",
                 "creator_id": 1, "operate_id": 1, "creator_name": "Admin", "operate_name": "Admin"}
    # �޸��ۿ�����
    r = requests.put(url=xgzk_url, json=xgzk_data, headers=xgzk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    # print(jine)
    # print(xgjine)


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
    print(r.json())


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
    print(r.json())


# test_xgzz()

# δ˰
# ������ֹid
weishui = {'id': None}
zzws = zhongzhi['id']


def test_ws():
    global zzws
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
    zzws = r.json()['data']['id']
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    # print(r.json())
    # ����δ˰�ɹ�����
    assert r.json()['message'] == 'success'
    print(r.json())


# test_ws()


# �޸�δ˰


def test_xgws():
    global zzws, weishui
    # �޸�δ˰URL
    xgws_url = f'http://192.168.0.217:9901/PurchaseApNoTax/{zzws}'
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
    print(r.json())

# test_xgws()


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
    print(r.json())

# test_yfk()
