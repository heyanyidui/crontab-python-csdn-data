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
soup = BeautifulSoup(html.read(),features='lxml')

sources = soup.select('.data-info')

soup = BeautifulSoup(str(sources),features='lxml')

# soup
results = soup.find_all(['span'])

# 总排名
place = results[2].get_text()

# 总积分
# score = results[4].get_text()      # 如果积分不超过1万可以这么使用
score = soup.find_all(['dl'])[5]['title']

# 总粉丝
fans = results[5].get_text()

# 总访客
text = soup.find_all(style='min-width:58px')[0]
visitors = text['title']

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(date)
print('排名：',place)
print('积分：',score)
print('粉丝：',fans)
print('访客：',visitors)

common = '排名：{}; 积分：{}; 粉丝：{}; 访客：{}'.format(place, score, fans, visitors)

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

