'''
@Description: 基于kafka部署消息通讯
@Author: Panbo Hey
@Date: 2023-12-05 14:45:24
@LastEditTime: 2023-12-05 15:51:52
@LastEditors: Panbo Hey
'''


from flask import  jsonify
from kafka import KafkaProducer, KafkaConsumer
from main_work import main
import json

# Kafka集群的配置
bootstrap_servers = 'yourIP:yourPort'  # 你的Kafka服务器地址



def get_kafka_data():
    print("get kafka data start")

    rec_topic = 'your_topic_id'  # 指定要发送到的主题
    # 创建Kafka消费者
    consumer = KafkaConsumer(
        rec_topic,
        bootstrap_servers=bootstrap_servers,
        group_id='your_group_id' , # 消费者组ID，通常用于协调多个消费者
        api_version=(2, 0, 2)
    )
    # 循环消费消息
    for message in consumer:
        json_string = message.value.decode('utf-8')  # 将字节序列解码为字符串
        json_data = json.loads(json_string)  # 解析字符串为JSON
        ai_result = main(json_data)
        ai_result["code"] = 200
        
        print(f"Received message: {message.value}")
        print("*"*50)
        send_kafka_data(ai_result)
    # 最后，别忘了关闭消费者连接
    consumer.close()
    print("get kafka data down")


def send_kafka_data(aimessage):
    print("*"*50)
    topic = 'your_send_topic_id'  # 指定要发送到的主题
    # 创建Kafka生产者
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers, api_version=(2, 0, 2))
    # 生产者代码    
    #message = "here is panbo information, receive it, datatime 231205 1339"
    message = json.dumps(aimessage)
    # Encode the message as bytes before sending it
    producer.send(topic, value=message.encode('utf-8'))
    producer.close()
    print("*"*50)
    print("信息已发送！")
    

def depoly_main():
    pass

if __name__ == "__main__":
    get_kafka_data()










