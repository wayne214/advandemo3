import socket, selectors, threading

# 创建默认的selectors
sel = selectors.DefaultSelector()


# 负责监听“有数据可读”事件的函数
def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print(data.decode('utf-8'))
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


s = socket.socket()
s.connect(('172.16.193.140', 40000))
# 设置该socket是非阻塞的
s.setblocking(False)
# 使用sel为s的EVENT_READ事件注册read监听函数
sel.register(s, selectors.EVENT_READ, read)


# 定义不断读取用户键盘输入的函数
def keyboard_input(s):
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
            # 将用户的键盘输入内容写入socket
        s.send(line.encode('utf-8'))


# 采用线程不断读取用户的键盘输入
threading.Thread(target=keyboard_input, args=(s,)).start()

while True:
    # 获取事件
    events = sel.select()
    for key, mask in events:
        # key的data属性获取为该事件注册的监听函数
        callback = key.data
        # 调用监听函数, key的fileobj属性获取被监听的socket对象
        callback(key.fileobj, mask)
