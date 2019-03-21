# 声明一个方法方法名为int_demo
def int_demo():
    # 声明aint变量，并赋值为1
    aint = 1
    # 打印aint的值
    print(aint)
    # 打印aint值的类型
    print(type(aint))

def str_demo():
    # 声明aint变量，并赋值为1
    astr = '1'
    # 打印aint的值
    print(astr)
    # 打印aint值的类型
    print(type(astr))

def float_demo():
    # 声明aint变量，并赋值为1
    afloat = 1.25
    # 打印aint的值
    print(afloat)
    # 打印aint值的类型
    print(type(afloat))

def int_add(aint, bint):
    print(aint)
    print(bint)
    return aint + bint


def jianfa(aint, bint):
    print(aint)
    print(bint)
    return aint - bint


if __name__ == '__main__':
    # int_demo()
    # add1 = int_add(1, 2)
    # print(add1)
    # jianfa1 = jianfa(9, 5)
    # print(jianfa1)
    str_demo()
    print("--------")
    float_demo()
    pass
