from pykafka import KafkaClient
import os, configparser


class Config(object):

    def __init__(self, conf_name='kafka_conf.ini'):
        file_path = os.path.join(os.path.dirname(__file__), conf_name)
        self.cp = configparser.ConfigParser()
        self.cp.read(file_path)

    def _get_content(self, section):
        result = {}
        for each in self.cp.options(section):
            value = self.cp.get(section=section, option=each)
            result[each] = int(value) if value.isdigit() else value
        return result

    pass


class MyKafkaClient(object):

    def __init__(self, section):
        self.conf = Config()._get_content(section)
        self.client = KafkaClient(self.conf['hosts'])

    def get_client(self):
        return self.client

    def get_topic(self, topic):
        return self.client.topics[topic]


if __name__ == '__main__':
    topic = MyKafkaClient('kafka1').get_topic('test')
    with topic.get_sync_producer() as producer:
        for i in range(10):
            producer.produce(('test' + str(i)).encode())
            print(i)
