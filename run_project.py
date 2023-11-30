'''
@Description: 使用flask启服务,提供AI的API接口
@Author: Panbo Hey
@Date: 2023-11-24 14:41:22
@LastEditTime: 2023-11-30 16:56:50
@LastEditors: Panbo Hey
'''
from flask import Flask, request, jsonify
import logging
import logging.config



from core.configs.aiconfig import config
from main import main

# 加载日志配置
logging.config.fileConfig(config.LOGGING_CONF)
# 创建 logger
logger = logging.getLogger('root')

# flask函数
app = Flask(__name__)


@app.route('/aitest', methods=['POST','GET'])
def ai_api_test():
    api_result = "AI API is Working!"
    return api_result


@app.route('/aiinsight', methods=['POST','GET'])
def ai_insight():
    try:
        # 获取 JSON 数据
        json_data = request.json        
        ai_result = main(json_data)
        ai_result["code"] = 200
        return jsonify(ai_result)
    except Exception as e:
        # 处理异常
        error_message = f'Error processing JSON: {str(e)}'

        Error_time = get_now_time
        logger.info("="*60)       
        logger.info(f"log Error infor time:{Error_time} ,request error data infor :{e}")
        logger.info("="*60)
      
        return jsonify({'error': error_message,
                        'code': 400}), 400


if __name__ == '__main__':
    app.run(host = config.HOST_IP_ADRESS, debug=True)

