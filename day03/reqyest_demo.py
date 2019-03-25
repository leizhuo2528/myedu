# 导入 requests 第三方包
import requests

if __name__ == '__main__':
    # 封装请求参数
    data = {"username": "admin", "password": "123456"}
    # 发送请求 带上两个参数 url 和 请求正文 就json
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    # 响应报文以text展现
    # text_body = response.text
    # print(text_body)
    json_body = response.json()
    print(json_body)

    # assert 200 == response.status_code
    assert 200 == json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization':token_head+' '+token_}
    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    info_json = get_info.json()
    print(info_json)
    assert 200== info_json['code']
    assert '作成功'in info_json['message']
    get = requests.get(url='http://192.168.60.132:8080/brand/list?pageNum=1&pageSize=3', headers=head)
    param = {'pageNum':1,'pageSize':5}
    requests_get = requests.get(url='http://192.168.60.132:8080/brand/list?', params=param, headers=head)
    print(requests_get.text)
    json = requests_get.json()
    json_data_ = json['data']
    list_ = json_data_['list']
    for i in list_:
        print(i)
    pass
