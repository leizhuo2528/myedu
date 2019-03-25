def break_demo():
    for i in range(5):
        print('第%s循环'%(i))
        if i == 2:
            #终止所以循环
            break
def contiune_demo():
    for i in range(5):
        print('第%s循环'%(i))
        if i == 2:
            print("")
            #终止本次循环
            continue
        print('第%s次循环，if判断之后'%(i))
        print('')

if __name__ == '__main__':
    for i in range(5):
        print('第%s循环'%(i))
        if i == 2:
            print("")
            continue
        print('第%s次循环，if判断之后'%(i))
        print('')

    pass
