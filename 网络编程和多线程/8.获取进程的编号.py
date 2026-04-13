"""
案例：演示获取进程的编号.

进程的编号解释：
    概述：
        在设备中,每一个程序(进程)都有自己的唯一进程id,当程序释放的时候,该进程的id也会释放,即:进程的id是可以重复使用的。
    目的：
        1. 查看子进程和父进程的关系，方便管理
        2. 例如：杀死指定进程，创建子进程...
    格式：
        查看当前进程的pid:
            os模块(operating,系统模块)的getpid()
            mutiprocessing #current_process()的pid属性

        查看当前进程的ppid:
            os #getppid()

细节:
    main中创建的进程,如果没有特殊指定,它的父进程都是main进程,
    而main进程的父进程是当前ide程序中的pid
"""


import multiprocessing
import time
import os


def coding(name: str, num: int):
    for i in range(num):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码......")
    print(f"p1的进程id为{os.getpid()}, {multiprocessing.current_process().pid}, 父进程的id为{os.getppid()}")

def music(name: str, num: int):
    for i in range(num):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首歌曲！！！！")
    print(f"p1的进程id为{os.getpid()}, {multiprocessing.current_process().pid}, 父进程的id为{os.getppid()}")

p1 = multiprocessing.Process(target=coding, kwargs={"name": "小明", "num": 10})
p2 = multiprocessing.Process(target=music, kwargs={"name": "小明", "num": 10})

if __name__ == '__main__':
    p1.start()
    p2.start()