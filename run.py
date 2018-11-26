from datetime import datetime
import os
import time

from config import app
from flask import render_template
import psutil
import socket
import platform


@app.route('/sys/')
def sys():
    now_time= datetime.now()  # 现在时间
    start_time=datetime.fromtimestamp(psutil.boot_time()) # 开机时间
    syss={
    'system':platform.system(), #操作系统
    'version':platform.version(), #系统版本号
    'architecture':platform.architecture(), #位数
    'machine':platform.machine(), #类型
    'processor':platform.processor(), #处理器信息
    'run_time':str(now_time-start_time).split('.')[0]  #运行时间
    }
    # run_time=datetime.datetime.fromtimestamp(now_time-start_time)   #运行时间
    return render_template('sys.html',now_time=str(now_time).split('.')[0],start_time=start_time,
                           syss=syss)

@app.route('/cpu/')
def cpu():
    cpu={
    'p_CPU':psutil.cpu_count(logical=False),
    'CPU':psutil.cpu_count(),
    'averageload_1':psutil.cpu_percent(interval=1),
    'averageload_5':psutil.cpu_percent(interval=5),
    'averageload_15':psutil.cpu_percent(interval=15),
    'user':psutil.cpu_times_percent().user,
    'system':psutil.cpu_times_percent().system,
    'idle':psutil.cpu_times_percent().idle,
    'nowfrequency':psutil.cpu_freq().current,
    'minfrequency':psutil.cpu_freq().min,
    'maxfrequency':psutil.cpu_freq().max
    }
    return render_template('cpu.html',cpu=cpu)

@app.route('/ram/')
def ram():
    ram={
    'memmorySize':round(psutil.virtual_memory().total/(1024**3),3),
    'available':round(psutil.virtual_memory().available/(1024**3),3),
    'percent':psutil.virtual_memory().percent,
    'used':round(psutil.virtual_memory().used/(1024**3),3),
    'free':round(psutil.virtual_memory().free/(1024**3),3)
    }
    return render_template('ram.html',ram=ram)

@app.route('/disk/')
def disk():
    disks=psutil.disk_partitions()
    return render_template('disk.html',disks=disks)

@app.route('/process/')
def process():
     pid=psutil.pids()[:20]
     processes=[]
     for i in pid:
         p=psutil.Process(i)
         processes.append((p.name(),p.status(),datetime.fromtimestamp(p.create_time()),round(p.memory_percent(),3)))
     return render_template('process.html',processes=processes)
if __name__ == '__main__':
    app.run()
