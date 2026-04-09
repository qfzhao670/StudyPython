"""
案例：网编入门案例，服务器端给客户端发送消息，客户端给出回执信息

服务器端开发流程：
    1. 创建服务器端Socket对象
    2. 绑定IP地址和端口号
    3. 设置最大监听数
    4. 等待客户端申请建立连接
    5. 给客户端发送消息
    6. 接收客户端的信息并打印
    7. 释放资源

细节：
    客户端和服务器端通过 字节流（bytes）的形式实现的
"""


import socket
# 1. 创建服务器端Socket对象
# 参1:Address Family，地址族，即：Ipv4 还是 IpV6，默认街：AF_INET（ipv4）AF_INET6(ipv6)
# # 参2:Socket Type, Socket类型，即：TCP 还是 UDP，默认值：SOCK_STREAM（TCP）SOCK_DGRAM(UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号
server_socket.bind(("127.0.0.1", 10086))
# 3. 设置最大监听数
server_socket.listen(5)
# 4. 等待客户端申请建立连接
accept_server, client_info = server_socket.accept()
# 5. 给客户端发送消息
accept_server.send(b'Welcome!')
# 6. 接收客户端的信息并打印
data = accept_server.recv(1024).decode("utf-8")
print(f"服务器端收到：{data}")
# 7. 释放资源
accept_server.close()