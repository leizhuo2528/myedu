import requests


if __name__ == '__main__':
    data={
  "email": "1555855@qq.com",
  "icon": "",
  "nickName": "",
  "note": "",
  "password": "123456",
  "username": "admin"
}
    register = requests.post(url='http://192.168.60.132:8080/admin/register', json=data)
    print(register.text)
    json = register.json()
    assert 200== json['code']
    login_data1={
  "password": "123456",
  "username": "admin"
}
    login = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data1)
    print(login.text)
    login_json = login.json()
    data_dict = login_json['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head + ' ' + token_}
    info_resp = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    info_json = info_resp.json()
    print(info_json)
    list_resp = requests.get(url='http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10&status=1&orderType=',
                       headers=head)
    list_resp_json = list_resp.json()
    print(list_resp_json)
    data_ = list_resp_json['data']
    list_ = data_['list']
    list__1= list_[0]
    order_id = list__1['id']

    #发货
    fahuo_data=[
                  {
                    "deliveryCompany": "运达",
                    "deliverySn": "2222",
                    "orderId": order_id
                  }
                ]
    requests_post = requests.post('http://192.168.60.132:8080/order/update/delivery', headers=head, json=fahuo_data)
    print(requests_post.text)
    json = requests_post.json()

    # 关闭
    guanbi_param={'ids':order_id,'note':'guggg'}
    close_ = requests.post(url='http://192.168.60.132:8080/order/update/close', params=guanbi_param, headers=head)
    print(close_.text)
    json1 = close_.json()
    pass