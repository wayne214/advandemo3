import poplib, os.path, mimetypes
from email.parser import BytesParser, Parser
from email.policy import default

email = '******@qq.com'
password = '*********'
pop3_server = 'pop.qq.com'

conn = poplib.POP3_SSL(pop3_server, 995)

conn.set_debuglevel(1)

print(conn.getwelcome().decode('utf-8'))
# user name：向 POP 服务器发送登录的用户名。
conn.user(email)
# pass string：向 POP 服务器发送登录的密码。
conn.pass_('*******')  # 使用授权码
# stat：统计邮件服务器状态，包括邮件数和总大小。
message_num, total_size = conn.stat()
print('邮件数：%s 总大小" %s' % (message_num, total_size))
# 获取pop邮件服务器上邮件列表，pop3的list命令
# resp保存服务器的响应码
# mails列表保存每封邮件的编号，大小
resp, mails, octets = conn.list()
print(resp, mails)
# 获取指定邮件的内容（此处传入总长度，也就是获取最后一封邮件）
# 相当于发送POP 3的retr命令
# resp保存服务器的响应码
# data保存该邮件的内容
resp, data, octets = conn.retr(len(mails))
# 将data的所有数据（原本是一个字节列表）拼接在一起
msg_data = b'\r\n'.join(data)
# 将字符串内容解析成邮件，此处一定要指定policy=default
# 在创建 BytesParse 或 Parser 解析器时，一定要指定 policy=default；
# 否则，解析出来的对象就是 Message，而不是新的 EmailMessage。
msg = BytesParser(policy=default).parsebytes(msg_data)
# print(msg)
print('发件人', msg['from'])
print('收件人', msg['to'])
print('主题', msg['subject'])
print('第一个收件人名字:' + msg['to'].addresses[0].username)
print('第一个发件人名字:' + msg['from'].addresses[0].username)

for part in msg.walk():
    counter = 1
    # 如果maintype是multipart，说明是容器（用于包含正文、附件等）
    if part.get_content_maintype() == 'multipart':
        continue
    # 如果maintype是multipart，说明是邮件正文部分
    elif part.get_content_maintype() == 'text':
        print(part.get_content())
        # 处理附件
    else:
        # 获取附件的文件名
        filename = part.get_filename()
        # 如果没有文件名，程序要负责为附件生成文件名
        if not filename:
            # 根据附件的contnet_type来推测它的后缀名
            ext = mimetypes.guess_extension(part.get_content_type())
            # 如果推测不出后缀名
            if not ext:
                # 使用.bin作为后缀名
                ext = '.bin'
                # 程序为附件来生成文件名
            filename = 'part-%03d%s' % (counter, ext)
        counter += 1
        # 将附件写入的本地文件
        with open(os.path.join('.', filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))
# 退出服务器，相当于发送POP 3的quit命令
conn.quit()
