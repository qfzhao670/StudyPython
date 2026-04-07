"""
案例：含参数的装饰器

记忆：
    1.一个装饰器只能携带一个参数
    2.如果装饰器需要加载多个参数，可以在装饰器外面再包裹一层，把装饰器作为内部函数返回即可。
"""
def wrapper(flag1, flag2):
    def my_decorator(fn_name):
        def inner_func(a, b):
            if flag1 == "+" and flag2 == True:
                print("正在执行【加法】运算")
            if flag1 == "-" and flag2 == True:
                print("正在执行【减法】运算")
            fn_name(a, b)
        return inner_func
    return my_decorator

@wrapper("+", False)
def get_sum(a, b):
    print(f"求和结果为{a + b}")

@wrapper("+", True)
def get_sub(a, b):
    print(f"求和结果为{a - b}")

if __name__ == '__main__':
    print("*" * 21)
    get_sum(1, 2)
    print("*" * 21)
    get_sub(1, 2)
    print("*" * 21)
    