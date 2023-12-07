# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 15:24
# @Author  : Pl
# @File    : run_work.py.py
from imp import PY_FROZEN
import os, argparse

from boto import config

def run_py(py_name, log_dir):
    """
    后台执行py_name.py的python程序
    """
    cmd = "nohup python -u {} >>{} 2>&l &".format(py_name, log_dir)
    print("run_py cmd is {}".format(cmd))
    os.system(cmd)


def shut_py(py_name):
    """
    后台执行py_name.py的停止命令
    """
    cmd = "ps aux | grep {} | grep -v grep".format(py_name)
    outline = os.popen(cmd).read()

    for line in outline.splitlines():
        pid = int(line.split()[1])
        print("Here is shut_py line {}".format(line))
        cmd = "kill %d"%(pid)
        os.system(cmd)


def clean_log(*logs_path):
    for log_dir in logs_path:
        clean_cmd = "rm {}".format(log_dir)
        os.system(clean_cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clean', action = 'store_true')
    parser.add_argument('-r','--run', action='store_true')
    parser.add_argument('-s','--shut', action='store_true')
    config = parser.parse_args()
    #防止同时传入多个参数
    k = int(config.clean) + int(config.run) + int(config.shut)
    #assert k == 1, "choose one and only one task to run!"
    
    PY_FILE1 = "./utils/clear_files_on_time.py"
    PY_FILE2 = "main_work.py"

    LOG_FILE1 = "./logs/main_work.log"
    LOG_FILE2 = "./logs/api_start.log"

    LOG_INFO = ("logs1", "logs2")


    if config.clean:
        clean_log(LOG_INFO)
    
    if config.run:
        run_py(PY_FILE1, LOG_FILE1)
        run_py(PY_FILE2, LOG_FILE1)
    
    if config.shut:
        shut_py(PY_FILE1)
        shut_py(PY_FILE2)


    