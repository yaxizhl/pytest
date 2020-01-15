import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

sender = 'imyaxi@126.com'  # 邮件发送者的邮箱地址
receivers = '404282939@qq.com'  # 邮件接收者的邮箱地址

# 三个参数：第一个为邮件正文文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message_html = '''<html><div style="color:red;">就斤斤计较</div></html>'''
message = MIMEText(message_html, 'html', 'utf-8')
message['From'] = formataddr(['ming', sender])  # 发送者
message['To'] = formataddr(["hei", receivers])  # 接收者

subject = '这是一封正常的测试邮件， 并不是异常的！'
message['Subject'] = Header(subject, 'utf-8')  # 邮件的主题

smtpObj = smtplib.SMTP('smtp.126.com', port=25)
smtpObj.login(user=sender, password='ya7q587a')  # password并不是邮箱的密码，而是开启邮箱的授权码
smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件
print('发送成功')
