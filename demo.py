# coding=gbk

import business.dlxt
from business import dlxt
import requests
import business.logger
from business import logger
import random
import json

# ������
jine = random.randint(99, 399)
# �����޸Ľ��
xgjine = random.randint(99, 399)

# ����token
a = dlxt.test_dl()['data']['token']
# ���忪Ʊid
b = {'id': None}
c = b['id']


def test_fk():
    global c
    # ����URL
    fk_url = 'http://192.168.0.217:9901/PurchaseApPayment'
    # ��������ͷ
    fk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # ����������
    fk_data = {"payment_list": [
        {"payment_total_amount": 199, "payment_time": "2023-02-02T16:00:00.000Z", "payment_mode": 65,
         "payment_mode_name": "�����ֽ�"}], "remark": "���Ը���", "order_list": [
        {"not_payment_amount": "9995884.00", "offset_amount": 0, "pre_payment_amount": 0,
         "usable_pre_payment_amount": "6181.00", "purchase_order_code": "87654321", "payment_amount": 199}]}
    # ��������
    r = requests.post(url=fk_url, json=fk_data, headers=fk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ȡ�����id���µ��б�
    b['id'] = r.json()['data']['id']
    c = r.json()['data']['id']
    # ��ӡjson��������
    # print(r.json())
    # ���ø���ɹ�����
    assert r.json()['message'] == 'success'
    print(r.json())


# test_fk()


# �޸ķ�Ʊ���
def test_xgfk():
    global c
    # �޸ĸ���URL
    xgfk_url = f'http://192.168.0.217:9901/PurchaseApPayment/{c}'
    # �޸ĸ�������ͷ
    xgfk_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # �޸ĸ���������
    xgfk_data = {"id": b['id'], "remark": "�����޸Ŀ�Ʊ����", "creator_id": 1, "operate_id": 1, "payment_list": [
        {"id": 2029, "payment_id": b['id'], "payment_time": "2023-02-03", "payment_total_amount": 99, "payment_mode": 65,
         "payment_mode_name": "�����ֽ�", "deleted_at": 0}], "order_list": [
        {"id": 3727, "payment_id": b['id'], "purchase_order_code": "87654321", "payment_amount": 99,
         "pre_payment_amount": 0, "offset_amount": "0.00", "deleted_at": 0, "customer_name": "�㽭�콡Զ���Ƽ����޹�˾",
         "not_payment_amount": "9995585.00", "usable_pre_payment_amount": "6181.00"}], "creator_name": "Admin",
                 "operate_name": "Admin"}

    data = json.dumps(xgfk_data)
    # �޸�δ˰����
    r = requests.put(url=xgfk_url, json=data, headers=xgfk_header)
    # �����־
    logger.logger.debug(f'��������:{r}')
    # ��ӡjson��������
    print(r.json())
    print(jine)
    print(xgjine)
    print(b)
    print(c)
    print(data)
    print(xgfk_url)

