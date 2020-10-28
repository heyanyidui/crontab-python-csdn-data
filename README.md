# crontab-python-csdn-data

使用 linux 的定时任务机制 (cron) 实现定时爬取 csdn 博客数据，并以邮件的形式发送给自己。

详细内容介绍 [博客地址](https://smileyan.blog.csdn.net/article/details/109312411) 。

### 效果说明

部署在自己的云服务器上，设置每天12点与23点统计自己CSDN博客相关数据，并以邮件的形式发送给自己。

### 文件介绍

* `myblog.py` python 源码，用于爬取 csdn 数据
* `blog.cron` 定时配置文件
* `myblog.log` 爬取数据的日志文件

### 使用方法

1. 修改myblog.py，主要修改自己的邮件相关信息，包括邮箱名称，密码，对应的邮箱服务器地址，收件人邮箱。

2. 查看 blog.cron 文件，配置自己希望的定时任务。配置过程中请注意保证 python3 文件的路径以及cron文件的路径正确。推荐使用绝对路径减少错误概率。

   ```bash
   0 12,23 * * * /home/yan/anaconda3/bin/python3 /home/yan/py_blog/myblog.py >> /home/yan/py_blog/myblog.log
   ```

   推荐测试时首先设置每分钟执行一次，以便于尽可能快看到效果。即

   ```bash
   * * * * * /home/yan/anaconda3/bin/python3 /home/yan/py_blog/myblog.py >> /home/yan/py_blog/myblog.log
   ```

3. 启动定时任务。命令为：`crontab blog.cron`。

### Q & A

使用时，如果有遇到任务问题欢饮 [issue](https://github.com/heyanyidui/crontab-python-csdn-data/issues)。



> heyanyidui
> 2020/10/28 