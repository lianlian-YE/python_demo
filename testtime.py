import datetime
import os
import psutil
# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.localtime().tm_year)

# mtime=os.path.getatime('G:\\python_classroom2\\day28\\01_预备知识绪论.py')
# print(mtime)
# print(time.ctime(mtime))
#
# ttime=time.localtime(mtime)
# print(ttime)
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(psutil.boot_time())
# print(datetime.datetime.fromtimestamp(psutil.boot_time()))
# print(time.time(time.strftime('%Y-%m-%d %H:%M:%S'))-(datetime.datetime.fromtimestamp(psutil.boot_time())))
# print(type(psutil.boot_time()))
# print(time.time()-psutil.boot_time())
# print(datetime.datetime.fromtimestamp(time.time()-psutil.boot_time()))
"""
Name:04_应用案例_系统监控.py
Author: lvah
Date: 2018-09-08
Email: xc_guofan@163.com
Desc:
    这是一个python脚本.


需求：

    1. 获取当前主机信息， 包含操作系统名， 主机名， 内核版本， 硬件架构等


    2. 获取开机时间和开机时长；


    3. 获取当前登陆用户


"""

import  os
import psutil
import time

from datetime import datetime

from psutil._common import suser

# info = os.uname(/)

print("1. 主机信息".center(50, '*'))
# print("""
#     操作系统: %s,
#     主机名: %s,
#     内核版本: %s,
#     硬件架构: %s
# """ %(info.sysname, info.nodename, info.release, info.machine))


# 2.
print("2. 开机时间".center(50, '*'))
# 获取开机时间的时间戳， 需要安装psutil模块;
boot_time = psutil.boot_time()
# 将时间戳转换为字符串格式, 两种方法， 任选一种l
# print(time.ctime(boot_time))
boot_time  = datetime.fromtimestamp(boot_time)

# 获取当前时间
now_time = datetime.now()
# 获取时间差
delta_time = now_time-boot_time
delta_time = str(delta_time).split('.')[0]
print("""
    开机时间: %s
    当前时间: %s
    开机时长: %s
""" %(boot_time,now_time, delta_time))


# 3.
print("3. 当前登陆用户".center(50, '*'))

# 获取当前登陆用户的详细信息， 需求是获取用户名和登陆主机;
users = psutil.users()

# 获取需要的信息
users = {"%s %s" %(user.name, user.host) for user in users}

# 实现信息的去重
for user in users:
    print("\t  %s" %(user))

# kiosk  foundation0.ilt.example.com
# root   172.25.254.250


# 此处自行探索
# print(psutil.disk_partitions())
# print(psutil.virtual_memory())

