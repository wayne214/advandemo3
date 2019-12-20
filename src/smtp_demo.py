import smtplib
from email.message import EmailMessage

# 定义SMTP邮件服务器地址
smtp_server = 'smtp.qq.com'
# 邮件发送人邮箱
from_addr = '*******@qq.com'  # 自己的邮想
# 邮件发送人邮箱密码
password = '*****'  # 邮箱密码
# 邮件接收人
to_addr = '******@163.com'  # 接收邮件地址邮箱

# 创建SMTP连接
# 早期SMTP 服务器都采用普通的网络连接，因此默认端口是 25。但现在绝大部分 SMTP 都是基于 SSL（Secure Socket Layer）的，
# 这样保证网络上传输的信息都是加密过的，
# 从而使得信息更加安全。这种基于 SSL 的 SMTP 服务器的默认端口是 465。
# 上面程序中连接的是 QQ 邮箱的基于 SSL 的 SMTP 服务器，QQ 邮箱服务器不支持普通的 SMTP。
conn = smtplib.SMTP_SSL(smtp_server, 465)
# 设计调试级别
conn.set_debuglevel(1)
# 登录邮箱
conn.login(from_addr, password)
# 创建邮件内容对象
msg = EmailMessage()
# 设置邮件内容
msg.set_content('您好，这是一封来自Python的测试邮件', 'plain', 'utf-8')
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
msg['subject'] = '一封html邮件'
msg['from'] = '李刚<%s>' % from_addr
msg['to'] = '新用户<%s>' % to_addr
# 退出连接
conn.quit()
