#encoding = utf-8

import random
import string
import threading
import time
import multiprocessing

queue = multiprocessing.Queue()


def get_str():
    s = string.digits + string.ascii_letters
    while True:
        if queue.qsize() < 10000:
            for _ in range(10000):
                aaa = ''.join([random.choice(s) for _ in range(random.randint(20, 50))])
                queue.put(aaa)


def get_data(queue):
    print('insert')
    while True:
        if queue.qsize() == 0:
            time.sleep(2)
            continue
        start = time.time()
        temp = []
        for _ in range(1000):
            temp.append(queue.get())
        print(f'获取 1000 条数据需要的时间为：{time.time() - start:.2f}')
        time.sleep(2)


def get_size(queue):
    print('size')
    while True:
        print(f'队列大小为：{queue.qsize()}')
        time.sleep(1)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    multiprocessing.Process(args=(queue,), target=get_data).start()
    threading.Thread(args=(), target=get_str).start()
    threading.Thread(args=(queue,), target=get_size).start()
