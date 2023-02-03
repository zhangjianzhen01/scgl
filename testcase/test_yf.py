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
    # δ˰URL
    ws_url = 'http://192.168.0.217:9901/PurchaseApNoTax'
    # δ˰����ͷ
    ws_header = {"Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"}
    # δ˰������
    ws_data = {"purchase_order_code": "87654321", "no_tax_amount": jine, "remark": "����δ˰"}
    # δ˰����
    r = requests.post(url=ws_url, json=ws_data, headers=ws_header)
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
    global zzws
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

# test_ws()
