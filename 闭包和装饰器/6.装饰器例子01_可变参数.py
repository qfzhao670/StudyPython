def my_docorator(fn_name):
    # inner_func的 输入/是否有return 和原函数保持一致
    def inner_func(*args, **kwargs):
        print("正在进行计算中.....")
        return fn_name(*args, **kwargs)
    return inner_func

@my_docorator
def get_sum(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(kwargs.values())

print(get_sum(1, 2, 3, a=4, b=5))