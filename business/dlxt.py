import requests
from business import logger as rz

# ��¼ϵͳ
# ��¼URL
dl_url = "http://192.168.0.217:9901/login"


def test_dl():
    # ��¼������
    dl_data = {"username": "admin", "password": "huazhou3"}
    # ��¼����ͷ
    dl_header = {"content-type": "application/json"}
    # ��¼post����
    r = requests.post(url=dl_url, json=dl_data, headers=dl_header)
    # ��ӡ��Ӧ���ؽ��
    # print(r.json())
    # ���Ե�¼�ɹ�
    assert r.json()['code'] == 10000
    return r.json()
# test_dl()
