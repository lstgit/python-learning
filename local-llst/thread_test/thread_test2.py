# -*- coding:utf-8 -*-
# Author: nulige

import threading
import time


def sub():
    global num

    # num -= 1
    temp = num
    time.sleep(0.00000009)  # 别外75个线程，拿到100了，时间不固定。
    num = temp - 1


num = 100

l = []

for i in range(100):
    t = threading.Thread(target=sub)
    t.start()
    print('num is %d' % num)
    l.append(t)

for t in l:
    t.join()

print(num)
