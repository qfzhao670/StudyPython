import multiprocessing
import time


def coding(name: str, num: int):
    for i in range(num):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码......")

def music(name: str, num: int):
    for i in range(num):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首歌曲！！！！")

p1 = multiprocessing.Process(target=coding, kwargs={"name": "小明", "num": 10})
p2 = multiprocessing.Process(target=music, kwargs={"name": "小明", "num": 10})

if __name__ == '__main__':
    p1.start()
    p2.start()