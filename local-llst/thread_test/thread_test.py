import threading, time, log_test.logUtils as logger

log = logger.Logger(file_name='thread_test.log', level='debug').log

num = 150


def sayhi():
    global num
    log.info('%s running number: %d ' % (threading.currentThread().getName(), num))
    time.sleep(0.005)
    num -= 1
    log.info('%s ***sayhi  end*** and num = %d' % (threading.currentThread().getName(), num))


def say_hello():
    global num
    log.info('%s running number: %d ' % (threading.currentThread().getName(), num))
    time.sleep(0.001)
    num += 1
    log.info('%s ***say hello  end***  and num = %d' % (threading.currentThread().getName(), num))


class My_thread(threading.Thread):

    def __init__(self, thread_name=None, target=None, daemon=False, args=()):
        super(My_thread, self).__init__(target=target, daemon=daemon, args=args)
        log.debug('current thread name is %s' % (threading.currentThread().getName()))
        self._thread_name = thread_name

    def run(self):
        self.setName(self._thread_name)
        super(My_thread, self).run()
        log.info('%s run ...' % (threading.currentThread().getName()))
        # time.sleep(5)
    pass


def thread_run():
    t1 = threading.Thread(target=sayhi, args=[num])
    t2 = threading.Thread(target=say_hello, args=[num])
    t1.start()
    t2.start()
    log.info('%s-----end' % (threading.currentThread().getName()))


if __name__ == '__main__':
    # thread_run()
    threads = []
    for i in range(100):
        my_thread = My_thread(thread_name='test-%d' % i, target=sayhi, args=[])
        my_thread.start()
        threads.append(my_thread)
        del my_thread
    for each in threads:
        each.join()
    log.info('main thread end...num = %d' % num)
