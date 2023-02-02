import requests
from business import logger as rz

# 登录系统
# 登录URL
dl_url = "http://192.168.0.217:9901/login"


def test_dl():
    # 登录请求体
    dl_data = {"username": "admin", "password": "huazhou3"}
    # 登录请求头
    dl_header = {"content-type": "application/json"}
    # 登录post请求
    r = requests.post(url=dl_url, json=dl_data, headers=dl_header)
    # 打印响应返回结果
    # print(r.json())
    # 断言登录成功
    assert r.json()['code'] == 10000
    return r.json()
# test_dl()
