import logging
from datetime import datetime
import time
import traceback


def get_logger(
        name = 'utils',  #对应的模块名
        file = "demo.log",
        logger_level = 'DEBUG',
        stream_level = 'DEBUG',
        file_level = 'INFO',
        fmt = '[%(asctime)s--%(filename)s--line:%(lineno)d]--%(levelname)s:%(message)s'
        
):
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)

    fmt = logging.Formatter(fmt)

    stream_handler.setFormatter(fmt)
    logger.addHandler(stream_handler)

    if file:
        # 初始化文件输出处理器
        file_handle = logging.FileHandler(file, encoding='utf8')
        # 设置文件输出处理器为绝对路径
        file_handle.name = file_handle.baseFilename
        # 设置文件输出处理器等级
        file_handle.setLevel(file_level)
        # 将收集器和文件输出处理器绑定
        logger.addHandler(file_handle)
        # 设置输出处理器日志格式
        file_handle.setFormatter(fmt)
    
    return logger






if __name__ == "__main__":
    strname = '=== panbo use to write ==='
    logger = get_logger(name = "utils/log", file = "./logs/demo_log.log")
    logger.error(f'here is more error information!{strname}')

