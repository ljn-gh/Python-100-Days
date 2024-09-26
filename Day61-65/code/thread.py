import random
import time
from threading import Thread, RLock
from concurrent.futures import ThreadPoolExecutor


def download(filename):
    print('开始下载%s...' % filename)
    time.sleep(random.randint(3, 6))
    print('%s下载完成' % filename)


def threadPoolExecutorTest():
    threads = [
        Thread(target=download, kwargs={'filename': 'Python从入门到住院.pdf'}),
        Thread(target=download, kwargs={'filename': 'Peking Hot.avi'}),
        Thread(target=download, kwargs={'filename': '深入Python3.pdf'}),
    ]
    # 开始多线程
    for thread in threads:
        thread.start()
    # 等待所有线程结束
    for thread in threads:
        thread.join()
    print('线程池下载...')
    with ThreadPoolExecutor(max_workers=3) as executor:
        list = ['Python从入门到住院.pdf', 'Peking Hot.avi', '深入Python3.pdf'];
        for filename in list:
            executor.submit(download, filename)
    print('线程池下载结束')


def display(content):
    while True:
        print(content, end='', flush=True)
        time.sleep(random.randint(0, 1))


def daemonThreadTest():
    # 其他非daemon线程未结束时,守护线程也不会结束
    # t1 = Thread(target=display,args=('hello'))
    t1 = Thread(target=display, args=('hello',), daemon=True)
    t2 = Thread(target=display, args=('world',), daemon=True)
    t1.start()
    t2.start()
    time.sleep(random.randint(5, 10))


class MyAccount():
    def __init__(self):
        self.balance = 0
        self.lock = RLock()

    # def deposit(self, money):
    #     self.lock.acquire()
    #     try:
    #         self.bal += money
    #     finally:
    #         self.lock.release()
    def deposit(self, money):
        with self.lock:
            self.balance += money


def lockTest():
    account = MyAccount()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for i in range(100):
            pool.submit(account.deposit, 1)
    print(account.balance)
