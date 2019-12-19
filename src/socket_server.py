import socket
import threading

# 服务端创建socket
# 1. 创建一个socket对象
# 2. 绑定指定IP地址和端口号
# 3. 调用listen监听网络
# 4. 循环不断的调用socket 的accept() 方法接受来自客户端的链接

# s = socket.socket()
#
# s.bind(('172.16.193.140', 30000))
#
# s.listen()
#
# while True:
#     c, addr = s.accept()
#     print(c)
#     print('连接地址', addr)
#     # 调用send()发送数据， sendto()用于UDP协议的通信
#     c.send('您好，你收到了服务器的新年祝福'.encode('utf-8'))
#     c.close()

# 多线程
ss = socket.socket()

ss.bind(('172.16.193.140', 40000))

ss.listen()

socket_list = []


# 读取每一个客户端socket 信息
def read_from_client(s):
    try:
        # 将字节数据恢复成字符串
        return s.recv(2048).decode('utf-8')
    # 如果捕获到异常，则表明该socket对应的客户端已经关闭
    except:
        # 删除该socket
        socket_list.remove(s)


def server_target(s):
    try:
        # 采用循环不断地从socket中读取客户端发送过来的数据
        while True:
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client in socket_list:
                # 将字符串编码成字节数据
                client.send(content.encode('utf-8'))
    except e:
        print(e.strerror)


while True:
    # 此行代码会阻塞，将一直等待别人的连接
    s, addr = ss.accept()
    socket_list.append(s)
    # 每当客户端连接后启动一个线程为该客户端服务
    threading.Thread(target=server_target, args=(s,)).start()
