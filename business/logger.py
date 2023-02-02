"""
定义日志文件
"""

import logging

# 配置logging  设置日志记录器的名字
logger = logging.getLogger("生产管理系统")

# 配置logger的级别
logger.setLevel(logging.DEBUG)

# 配置通用的日志格式            时间          日志级别      记录器名字   日志信息     文件名称        线程名称
format = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s %(filename)s %(funcName)s')

# 配置控制台打印
sh = logging.StreamHandler()
# 设置日志级别
sh.setLevel(logging.DEBUG)
# 设置日志格式
sh.setFormatter(format)

# 将控制台打印 添加到logger中
logger.addHandler(sh)

# 日志文件按天划分，每次执行的时候，比如今天是 2022-2-13, 创建目录 2022-2 表示2022年2月份日志
# 在目录中创建文件 13.log 表示13日的日志
import time
import os

dir = time.strftime("%Y-%m")
file = time.strftime("%d")
print(dir, file)
# 创建目录 设置logs 目录
logs = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(logs):
    os.mkdir(logs)
# 拼接日志目录和 年-月 的目录
log_dir = os.path.join(logs, dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# 日志文件
log_file = os.path.join(log_dir, file + ".log")

# 配置文件存储
fh = logging.FileHandler(filename=log_file, encoding='UTF8')
# 日志文件的 级别
fh.setLevel(logging.DEBUG)
# 日志文件的内容格式
fh.setFormatter(format)

# 将日志文件配置添加到logger
logger.addHandler(fh)

if __name__ == '__main__':
    logger.info("hahahah")
