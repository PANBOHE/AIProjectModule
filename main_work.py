# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 15:24
# @Author  : Pl
# @File    : main_work.py.py



from datetime import datetime
import json
from multiprocessing import Process
import os
import threading
from time import time
from typing import OrderedDict
import cv2
import requests
from flask import Flask,request,jsonify


from utils.project_config import config
app = Flask(__name__)

def logging(file_name):
    def decorator(func):
        def wrapper(*args):
            info = "\n" + args[0]
            with open(file_name, 'a') as f:
                f.write(info)
        return wrapper
    return decorator

if config.USE_LOGGING:
    @logging(config.MAIN_WORK_LOG)
    def print(info):
        return 0

def apply_common_detect_api(request_data, API_URL):
    request_data = json.dumps(request_data)
    header = {'Content-Type': 'application/json'}
    response = requests.request("POST", API_URL, headers =header, data = request_data)
    response = response.json()
    return response

def time_limiter(timeout):
    def functions(func):
        def run(*args):
            p = Process(target = func, args = args)
            p.start()
            p.join(timeout)
            p.terminate()
            return p.exitcode == 0
        return run
    return functions

@time_limiter(config.MAX_RTMP_TIME)
def try_save_img(rtmp, save_path):
    cap = cv2.VideoCapture(rtmp)
    ret, img = cap.read()
    if ret:
        cv2.imwrite(save_path, img)
    return ret


class MyThread(threading.Thread):
    """
    核心代码
    通过重写Thread函数,实现单个线程传参和返回一一匹配,
    使用threading来控制最大线程数,

        注意:
        (01)
        2022年7月19日:多线程用到了,多进程还没用到,和AI-vision是两套思路

    """
    def __init__(self, camera_id, rtmp_path, img_folder, result_foledr):
        threading.Thread.__init__(self)
        self.camera_id = camera_id
        self.rtmp_path = rtmp_path
        self.img_folder = img_folder
        self.result_folder = img_folder
        self.ret = -1
        self.info = None

    def run(self):
        os.makedirs(os.path.join(self.img_folder, self.camera_id), exist_ok=True)

        now_time = datetime.now().strftime('%Y%m%d%H%M%S')
        img_path=os.path.join(self.img_folder,self.camera_id,"{}.jpg".format(now_time))

        ret = try_save_img(self.rtmp_path, img_path)

        if ret:
            data = {
                "input_path": img_path,
                "camera_id": self.camera_id
            }
            api = "http://{}:{}/object_detect_api".format(config.LOCAL_IP, config.DETECT_PORT)
            response = apply_common_detect_api(data, api)

            if response["_respMsg_"] == "Success":
                self.ret = response["total_num"]
            else:
                self.info = response["_respMsg_"]
        else:
            self.ret=-2
            self.info="Warning, this playurl is not available.{}".format(self.rtmp_path)

@app.route("/ai/start_common", methods = ["POST"])
def main_fuction():
    data = {}
    try:
        MAX_THREAD_NUM = config.MAX_THREAD_NUM
        TEST_FOLDER = "input/inputfile"
        RESULT_FOLDER = "output/outputfile"

        params = request.get_json()

        print("=== api-start_common recive paramters: {}===".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        for item in params:
            print("    {}:{}".format(item,params[item]))

        thread_list = []
        for item in params["paramter"]:
            camera_id = item["diviceId"]
            rtmp_path = item["rtmp"]
            thread_list.append(MyThread(camera_id, rtmp_path, TEST_FOLDER, RESULT_FOLDER))

        for thread in thread_list:
            while threading.active_count > MAX_THREAD_NUM:
                time.sleep(0.5)
            thread.start()
        for thread in thread_list():
            thread.join()

        result = []
        for thread in thread_list:
            temp = OrderedDict({'deviceId':thread.camera_id,'areaNum':thread.ret})
            result.append(temp)
        data['RespMsg']="Success"
        data['count_result']=result
    except Exception as e:
        data["RespMsg"] = "Fail, The Problem is {}".format(e)
    print("=== prepare return: {} ===".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    for item in data:
        print("    {}:{}".format(item,data[item]))
    return jsonify(data)

if __name__ == '__main__':
    app.run(
        threaded = True,
        processes = False,
        host = config.LOCAL_IP,
        port = config.MAIN_API_PORT,
        debug = False)
