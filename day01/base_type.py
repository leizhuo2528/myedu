# 声明一个方法方法名为int_demo

blist = [7,856,526,222]

def list_sda():
    alist = [7, 856, 526, 222]
    return alist

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

def str_demo():
    # int_demo()
    # add1 = int_add(1, 2)
    # print(add1)
    # jianfa1 = jianfa(9, 5)
    # print(jianfa1)
    # str_demo()
    # print("--------")
    # float_demo()
    # print(blist)
    # print(list_sda())
    pass

def orderBy_name():
    print('调用正序排序的方法')
    srot_demo()
    print('调用倒序排序的方法')
    reverse_demo()
    pass
# 正序方法
def srot_demo():
    blist.sort()
    print(blist)
    pass
#倒序按方法
def reverse_demo():
    blist.reverse()
    print(blist)
    pass

def pop_demo():
    sdsasd.pop()
    # print(sdsasd.pop())
    sdsasd.pop(1)
    # print(sdsasd.pop(1))

if __name__ == '__main__':
    # sdsasd = [1, 52, 125, 251]
    # pop_demo()
    # print(sdsasd)
    orderBy_name()
    pass
