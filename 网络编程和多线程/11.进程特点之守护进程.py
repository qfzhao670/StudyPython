"""
案例：演示进程的特点。

进程的特点：
    1. 进程之间数据是相互隔离的。
        因为子进程相当于是父进程的“副本”，会将父进程的“main外资源”拷贝一份，即：各是各的
    2. 默认情况下，主进程会等待子进程执行结束再结束。
        如果要设置主进程结束，子进程同步结束，方式如下：
        思路1:设置子进程为守护进程
        思路2:强制关闭子进程，可能会导致子进程编程僵尸进程，交由python解释器自动回收（底层有init初始化进程来管理维护）
"""
import multiprocessing
import time


def work():
    for i in range(10):
        time.sleep(0.2)
        print("working.....")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=work)
    # 方法1:守护进程
    p1.daemon = True

    p1.start()

    time.sleep(1)
    #方式2:强制关闭
    # p1.terminate()

    print("主进程main结束")