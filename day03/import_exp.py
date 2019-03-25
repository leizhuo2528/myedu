import os

def os_demo():
    getcwd = os.getcwd()
    print(getcwd)
    abspath = os.path.abspath('..')
    print(abspath)

def open_demo1():
    text_io = open('../test.text', 'w+')
    text_io.write('呵呵呵呵')

def open_demo2():
    text_io = open('../test.text', 'r')
    readable= text_io.readable()
    print(readable)
    readlines = text_io.readlines()
    print(readlines)


if __name__ == '__main__':
    open_demo2()

    pass
