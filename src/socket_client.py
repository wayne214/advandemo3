import socket
import threading

# socket客户端
# 1.创建socket对象
# 2.调用socket 的connect()方法连接远程服务器

s = socket.socket()

s.connect(('172.16.193.140', 40000))


# print('--%s--' % s.recv(1024).decode('utf-8'))
#
# s.close()
def read_from_server(s):
    while True:
        print(s.recv(2048).decode('utf-8'))


# 客户端启动线程不断地读取来自服务器的数据
threading.Thread(target=read_from_server, args=(s,)).start()

while True:
    line = input('')
    if line is None or line == 'exit':
        break
    # 将用户的键盘输入内容写入socket
    s.send(line.encode('utf-8'))
