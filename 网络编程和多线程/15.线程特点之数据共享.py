"""
多线程的特点：
    1. 线程执行具有随机性，原因是因为CPU做着高效的切换
        CPU调度资源的策略：
            1. 均分时间片
            2. 抢占式调度（大部分场景都是这个）
    2. 默认情况下，主线程会等待子线程结束再结束
    3. （同一个）进程间 数据共享
    4. 多线程操作共享数据， 可能会出现安全问题，可以用互斥锁解决。
"""

import threading, time


my_list= []
def write_list():
    for i in range(6):
        my_list.append(i)
    print(f"write{my_list}")

def read_list():
    print(f"read{my_list}")

if __name__ == '__main__':
    t1 = threading.Thread(target=write_list)
    t2 = threading.Thread(target=read_list)

    t1.start()
    time.sleep(0.5)
    t2.start()