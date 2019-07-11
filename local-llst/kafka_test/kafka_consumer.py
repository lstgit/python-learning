# -* coding:utf8 *-
import kafka_test.kafka_client as kafka_client, logging
import log_test.logUtils as logutils

log = logutils.Logger().log


if __name__ == '__main__':
    topic = kafka_client.MyKafkaClient('kafka1').get_topic('test')
    consumer = topic.get_balanced_consumer(consumer_group=b'test_group',
                                           # 设置为False的时候不需要添加consumer_group，直接连接topic即可取到消息
                                           # auto_commit_enable=False,
                                           # 这里就是连接多个zk
                                           zookeeper_hosts='zookeeper01:2181, zookeeper02:2181, zookeeper03:2181, zookeeper04:2181'
                                           )
    partition = consumer._get_participants()
    log.info(format(partition))
    earliest_offsets = topic.earliest_available_offsets()
    log.info(earliest_offsets)
    last_offsets = topic.latest_available_offsets()
    log.info(last_offsets)
    offset = consumer.held_offsets
    log.info("当前消费者分区offset情况{}".format(offset))
    log.info(123123)
    while True:
        msg = consumer.consume()
        offset = consumer.held_offsets
        print("{}, 当前消费者分区offset情况{}".format(msg.value.decode(), offset))
        consumer.commit_offsets()
