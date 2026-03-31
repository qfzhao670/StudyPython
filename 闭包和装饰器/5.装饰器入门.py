"""
装饰器介绍：
    概述/作用：
        它的本质是一个闭包函数，目的是在不改变原有函数的基础上，对其功能做增强。
        大白话：装修队在不改变房屋结构的情况下，对房屋做装饰（功能增强）
    前提条件：
        1. 有嵌套
        2. 有引用
        3. 有返回
        4. 有额外功能
    装饰器的用法：
        格式1: 传统写法。
            装饰后的函数名 = 装饰器名（被装饰的函数名）
            装饰后的函数名（）
        
        格式2: 语法糖
            在要被装饰的原函数上，直接写@装饰器名，之后直接调用原函数即可
"""

def check_login(fc_name):
    def inner_func():
        print("正在登录.....登陆成功")
        fc_name()
    return inner_func

# 传统写法
def comment():
    print("进行评论操作...")
func1 = check_login(comment)

# 语法糖
@check_login
def comment2():
    print("进行评论操作2...")

if __name__ == '__main__':
    func1()
    print("_" * 23)
    comment2()