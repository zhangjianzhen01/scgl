# coding=gbk
import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random

# ������
jine = random.randint(99, 399)
# �����޸Ľ��
xgjine = random.randint(99, 399)

# ����8λ�����Ʊ����
kphm = random.randint(99, 99999999)
# ����8λ�����Ʊ����
xgkphm = random.randint(99, 99999999)
# ���忪Ʊδ��˰���
hs = jine * 0.85
# ���忪Ʊ��˰���
whs = jine * 0.15

# ����token
a = dlxt.test_dl()['data']['token']
# ���忪Ʊid
b = {'id': None}
c = b['id']


def test_fp():
    global c
    # ��ƱURL
    fp_url = 'http://192.168.0.217:9901/PurchaseApInvoice'
    # ��Ʊ����ͷ
    fp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ��Ʊ������
    fp_data = {"invoice_list": [
        {"invoice_total_amount": jine , "invoice_no": kphm, "invoice_time": "2023-02-01T16:00:00.000Z",
         "invoice_type": 86, "invoice_type_name": "��ֵ˰ר�÷�Ʊ-HZ(13%)",
         "invoice_info": [{"invoice_amount": whs, "invoice_tax_amount": hs, "invoice_tax_rate": whs}]}],
               "remark": "���Կ�Ʊ", "order_list": [
            {"customer_name": "�㽭�콡Զ���Ƽ����޹�˾", "purchase_order_code": "87654321", "invoice_amount": jine,
             "not_invoice_amount": "9996611.00"}]}
    # ��Ʊ����
    r = requests.post(url=fp_url, json=fp_data, headers=fp_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ȡ��Ʊ����id���µ��б�
    b['id'] = r.json()['data']['id']
    c = r.json()['data']['id']
    # ��ӡjson��������
    # print(r.json())
    # ���÷�Ʊ�ɹ�����
    assert r.json()['message'] == 'success'
    print(r.json())


# test_fp()


# �޸ķ�Ʊ���


def test_xgfp():
    global c
    # �޸ķ�ƱURL
    xgfp_url = f'http://192.168.0.217:9901/PurchaseApInvoice/{c}'
    # �޸ķ�Ʊ����ͷ
    xgfp_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # �޸ķ�Ʊ������
    xgfp_data = {"id": b['id'], "remark": "�����޸Ŀ�Ʊ����", "creator_id": 1, "operate_id": 1, "invoice_list": [
        {"id": 2448, "invoice_id": b['id'], "invoice_total_amount": jine, "invoice_no": xgkphm,
         "invoice_time": "2023-02-02", "invoice_type": 86, "invoice_type_name": "��ֵ˰ר�÷�Ʊ-HZ(13%)",
         "deleted_at": 0, "invoice_info": [
            {"id": 2473, "invoice_item_id": 2448, "invoice_amount": whs, "invoice_tax_amount": hs,
             "invoice_tax_rate": hs, "deleted_at": 0}]}], "order_list": [
        {"id": 3953, "invoice_id": b['id'], "purchase_order_code": "87654321", "invoice_amount": jine, "deleted_at": 0,
         "customer_name": "�㽭�콡Զ���Ƽ����޹�˾", "not_invoice_amount": "9996385.00"}], "creator_name": "Admin",
                 "operate_name": "Admin"}
    # �޸�δ˰����
    r = requests.put(url=xgfp_url, json=xgfp_data, headers=xgfp_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    print(jine)
    print(xgjine)
    print(b)
