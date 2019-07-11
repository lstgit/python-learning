# -* coding:utf8 *-
import json, kafka_test.kafka_client as kafka_client

if __name__ == '__main__':
    topic = kafka_client.MyKafkaClient('kafka1').get_topic('test')
    data = {}
    data['name'] = 'lsy'
    with topic.get_sync_producer() as producer:
        for i in range(100):
            producer.produce((json.dumps(data)).encode())
            print(i)
