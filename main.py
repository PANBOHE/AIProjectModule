import logging
import logging.config
from core.configs.aiconfig import config

# 加载日志配置
logging.config.fileConfig(config.LOGGING_CONF)
# 创建 logger
logger = logging.getLogger('root')

# 记录日志消息
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")

def main():
    pass


if __name__ == "__main__":
    print("========= main.py is running! =========")