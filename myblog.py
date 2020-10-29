#!/usr/bin/python
# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

# 博客地址
url = 'https://blog.csdn.net/smileyan9'
html = urlopen(url)
soup = BeautifulSoup(html.read())

# 进一步缩小范围
sources = soup.select('.data-info')
soup = BeautifulSoup(str(sources))

dls = soup.find_all(['dl']) 
notes = ['原创','周排名','总排名','访问','等级','积分','粉丝','获赞','评论','收藏']

common = ''

# 选择自己关注的数据以及顺序
keys = [6,3,5,8,7,9]

for key in keys:
    common += (notes[key]+':'+dls[key]['title']+" ")

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(date,'->',common)

# 第三方 SMTP 服务
mail_host = 'smtp.exmail.qq.com'  #设置服务器
mail_user = "root@smileyan.cn"    #用户名
mail_pass="Your password"   

sender = 'root@smileyan.cn'
receivers = ['root@smileyan.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText(common, 'plain', 'utf-8')
message['From'] = Header("Python 脚本(by smileyan)", 'utf-8')
message['To'] =  Header("幸运儿", 'utf-8')

subject = date
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
