def zhuen():
    a = '123456'
    # try 用于处理异常；如果出现异常 则执行except内的代码
    try:
        # 判断a 是否包含7
        assert '7' in a
    # except 报错后执行
    except:
        print('a里面没有7')
def shenj():
    a = '123456'
    # try 用于处理异常；如果出现异常 则执行except内的代码
    try:
        # 判断a 是否包含7
        assert '7' in a
    # except 报错后执行
    except:
        print('a里面没有7')
    # 不管 是否异常，finally里面的代码 都会被执行
    finally:
        print('最后')

if __name__ == '__main__':

    pass

