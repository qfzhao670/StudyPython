"""
nonlocal:
    他是python内置的关键字，可以实现 在内部函数中 修改外部函数的 变量值
"""

def func1():
    a = 100
    def func2():
        nonlocal a          # 这里要和global做区分，global是声明全局变量，nonlocal是对外部函数的变量进行修改
        a = a + 1
        print(f"a: {a}")
    return func2

if __name__ == '__main__':
    FUNC1 = func1()
    FUNC2 = FUNC1()
    FUNC3 = FUNC1()
