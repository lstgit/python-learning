import threading, time, log_test.logUtils as logger

log = logger.Logger(file_name='thread_test.log', level='debug').log


def sayhi(num):
    log.info('running number: %d' % num)
    time.sleep(4)
    log.info('%s ***sayhi  end***' % (threading.currentThread().getName()))


class My_thread(threading.Thread):

    def __init__(self, thread_name=None, target=None, daemon=False):
        super(My_thread, self).__init__(target=target, daemon=daemon)
        log.debug('current thread name is %s' % (threading.currentThread().getName()))
        self._thread_name = thread_name

    def run(self):
        super(My_thread, self).run()
        self.setName(self._thread_name)
        time.sleep(5)
        log.info('%s run ...' % (threading.currentThread().getName()))
    pass


def thread_run():
    t1 = threading.Thread(target=sayhi, args=[22])
    t2 = threading.Thread(target=sayhi, args=[33])
    t1.start()
    t2.start()
    log.info('%s-----end' % (threading.currentThread().getName()))


if __name__ == '__main__':
    # thread_run()
    for i in range(2):
        my_thread = My_thread(thread_name='test-%d' % i)
        my_thread.start()
