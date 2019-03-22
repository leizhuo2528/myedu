import json

adict ={"name":"zhuolei","pad":"1233456",1:"数字1"}

adictSte='{"name":"zhuolei","pad":"1233456"}'

if __name__ == '__main__':
    # print(adict)
    # adict.pop('name')
    # print(adict['name'])
    # print(adict)
    print(type(adict))
    print(type(adictSte))
    loads = json.loads(adictSte)
    print(type(loads))
    dumps = json.dumps(adict,ensure_ascii=False)
    print(dumps)