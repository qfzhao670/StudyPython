"""
案例：演示多线程共享全局变量，可能出现问题

多线程共享全局变量，出现的问题：
    累加次数不够
产生原因：
    线程1还没有来得及执行完（一个完整的动作）前，被线程2抢走了资源，就可能会出问题
"""

# 需求：定义两个函数，分别对全局变量进行累加100w次，创建两个线程，关联这两个函数，执行看效果

import threading

sum = 0
def sum1():
    global sum
    for _ in range(1000000):
        sum = sum + 1
    print(f"总和1={sum}")

def sum2():
    global sum
    for _ in range(1000000):
        sum = sum + 1
    print(f"总和2={sum}")

if __name__ == '__main__':
    t1 = threading.Thread(target=sum1)
    t2 = threading.Thread(target=sum2)

    t1.start()
    t2.start()
