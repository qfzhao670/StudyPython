import socket
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 10086))
data = client_socket.recv(1024).decode("utf-8")
print(f"客户端收到：{data}")
time.sleep(5)
client_socket.send("你也好！".encode())
client_socket.close()