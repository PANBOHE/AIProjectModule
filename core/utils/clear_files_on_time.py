


from asyncio import subprocess
from datetime import datetime
import time

from project_config import config


SLEEP_TIME = config.SLEEP_TIME


def run_cmd(cmd):
    """
    运行系统命令行命令

    输入：
    -----------
    cmd : 命令行命令

    输出:
    -----------
    无
    """

    cmd_order = subprocess.Popen(cmd, shell = True)
    cmd_order.wait()


def execute_del_cmd():
    """
    执行删除文件指令
        注意:
        1)删除文件夹下面所有文件
        2)删除某个指定文件
        3)可以通过cmd_list来配置删除一个或者多个任务的指令
    """
    cmd_list = config.CMD_LIST

    for cmd in cmd_list:
        run_cmd(cmd)


if __name__ == "__main__":
    while True:
        #通过获取当前时间，和sleep函数，实现定时删的功能
        now_time = datetime.now().strftime(r'%Y%m%d%H%M%S')
        if now_time[7] == '5':
            execute_del_cmd()
            print(" DEL FILES!", now_time)
        time.sleep(SLEEP_TIME)
