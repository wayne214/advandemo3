import socket
# 定义端口号
PORT = 40000
# 定义数据报包的大小最大为4KB
DATA_LEN = 4096
# 定义一个字符串数组，服务器端发送该数组的元素
books = ("疯狂Python讲义",
    "疯狂Kotlin讲义",
    "疯狂Android讲义",
    "疯狂Swift讲义")
# 通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)

s.bind(('172.16.193.140', PORT))

for i in range(100):
    # 获取socket中数据的数据和发送地址
    data, addr = s.recvfrom(DATA_LEN)
    print(data.decode('utf-8'))

    send_data = books[i % 4].encode('utf-8')

    s.sendto(send_data, addr)
s.close()