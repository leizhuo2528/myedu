def if_demo():
    sum1 = 0
    for i in range(1, 51):
        if i % 2 != 0:
            print(f"i的值{i}")
            sum1 = sum1 + i
            print(f"和{sum1}")

    print(f"1-50之间奇数的和是：{sum1}")


def for_demo():
    for i in range(9,0,-1):
        for j in range(1,i+1,):
            print("%sX%s=%s"%(i,j,i*j),end=' ')
        print()
    pass

def int_demo(a,b):
    if a>b:
        b=b+1
        sum=0
        for i in range(b,a):
            i%2 == 0
            sum+=i
            print(sum)
    elif a<b:
        a=a+1
        for i in range(a,b):
            i%2==0
            sum+=i
            print(sum)
    else:
        print("两数相等")


    pass

if __name__ == '__main__':

    int_demo(5,10)

    # 生成迭代器



    pass