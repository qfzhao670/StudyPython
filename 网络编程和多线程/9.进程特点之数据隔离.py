"""
案例：演示进程的特点。

进程的特点：
    1. 进程之间数据是相互隔离的。
        因为子进程相当于是父进程的“副本”，会将父进程的“main外资源”拷贝一份，即：各是各的
    2. 默认情况下，主进程会等待子进程执行结束再结束。
"""
import multiprocessing
import time


mylist = []
print("hallo!你好呀")

def write_mylist():
    for i in range(6):
        mylist.append(i)
    print(f"write{mylist}")

def read_mylist():
    print(f"read{mylist}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_mylist)
    p2 = multiprocessing.Process(target=read_mylist)

    p1.start()
    time.sleep(3)
    p2.start()