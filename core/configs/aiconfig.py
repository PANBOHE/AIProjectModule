'''
@Description: 项目的config命名方式
@Author: Panbo Hey
@Date: 2023-11-23 16:17:37
@LastEditTime: 2023-11-27 14:59:10
@LastEditors: Panbo Hey
'''
from typing import Any


class Config(object):
    class ConstError(TypeError):
        pass


    class ConstCaseError(ConstError):
        pass


    def __setattr__(self, __name: str, __value: Any) -> None:
        #存在性验证，是否已经设置过了
        if __name in self.__dict__.keys():
            raise self.ConstCaseError("Can't change a const variable: '%s'" % __name)
        #合法性验证，是否是大写
        if not __name.isupper():
            #语法规范验证
            raise self.ConstCaseError("Const variable must be combined with upper letters:'%s'" % __name)
        self.__dict__[__name] = __value


    def __str__(self) -> str:
        _str = '<====== Configs information ======>\n'
        for name, value in self.__dict__.items():
            _str += '  {}  \t{}\n'.format(name, value)
        return _str
        
#=============================================#
config = Config()
#=============================================#

"""
Base project information
"""
config.LOGGING_CONF = "./logs/logging.conf"
config.HOST_IP_ADRESS = "0.0.0.0"



"""
Use by ./funciton/get_trigger.py
"""
config.TEMP_HIGH = 0.5
config.TEMP_LOW  = 0.5
config.TEMPERATURE_UNIT_CONVERSION = 9 / 5
config.HUMUNIT = 2
config.TEMPZERO = 0

"""
Use by ./funciton/getTrigger.py
"""







"""
Use by ./clear_files_on_time.py

"""

config.OUTPUT_FOLDER = "./inference/output"
config.MAIN_WORK_LOG = "./logs/main_work_log"
config.RUN_WORK_LOG = "./logs/run_work_log"
config.INPUT_FOLDER = "./inference/input"
config.CMD_LIST = ["rm -rf {}/*".format(config.INPUT_FOLDER),
                    "rm -rf {}".format(config.MAIN_WORK_LOG),
                    "rm -rf {}".format(config.RUN_WORK_LOG)
                ]
config.SLEEP_TIME = 24*60*60


"""
Use by ../mainwork.py

"""



config.USE_LOGGING = True
config.API_URL = ""
config.MAX_RTMP_TIME = 10
config.LOCAL_IP = "192.168.0.153"
config.MAIN_API_PORT = 5005
config.DETECT_PORT = 5001
config.MAX_THREAD_NUM = 50
config.FILE_PATH = "./data/oridata/20230227033739.xls"
config.LOG_PATH = "./logs/main_log.log"
config.LOG_AIINSIGHT = "./logs/aiinsight_log.log"
config.LOG_AICONTROL = "./logs/aicontol_log.log"
config.EXCEL_PATH = "./data/AIinsightV1117.xlsx"


if __name__ == "__main__":
    config = Config()
