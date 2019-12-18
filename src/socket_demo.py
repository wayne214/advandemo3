from urllib.parse import *
from urllib.request import *

# 解析URL字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')

print(result)
# 通过属性名和索引来获取URL的各部分
print('scheme', result.scheme, result[0])
print('主机和端口', result.netloc, result[1])
print('主机名', result.hostname, )
print('端口', result.port, )
print('资源路径', result.path, result[2])
print('参数', result.params, result[3])
print('查询字符串', result.query, result[4])
print('fragment', result.fragment, result[5])
print(result.geturl())

# 解析查询字符串，返回类型为字典dict
result1 = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')

print(result1)
# 解析字符串，返回类型为list
result2 = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')

print(result2)
# 将列表格式的请求参数回复称请求参数字符串
print(urlencode(result2))

# 打开URL对应的资源
requestResult = urlopen('http://www.crazyit.org/index.php')
# 按字节读取数据
data = requestResult.read(326)
# 将字节数据恢复成字符串
# print(data.decode('utf-8'))

# 使用context manager来管理打开的URL资源
with urlopen('http://www.crazyit.org/index.php') as f:
    datas = f.read(326)
    print(datas.decode('utf-8'))
