from multiprocessing import Process,current_process,Queue
from time import sleep

def sub_task(content,nums):
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')
    # 通过下面的输出不难发现，每个进程都有自己的nums列表，进程之间本就不共享内存
    # 在创建子进程时复制了父进程的数据结构，三个进程从列表中pop(0)得到的值都是20
    counter, total = 0, nums.pop(0)
    print(f'Loop count: {total}')
    sleep(0.5)
    while counter < total:
        counter += 1
        print(f'{counter}: {content}')
        sleep(0.01)
def sub_task2(content, queue):
    counter = queue.get()
    while counter < 50:
        print(content, end='', flush=True)
        counter += 1
        queue.put(counter)
        sleep(0.01)
        counter = queue.get()

def main1():
    nums = [20, 20, 20]
    Process(target=sub_task, args=('Hello', nums), name='A').start()
    Process(target=sub_task, args=('World', nums), name='B').start()
    sub_task('Good', nums)

def main2():
    queue = Queue()
    queue.put(0)
    p1 = Process(target=sub_task2, args=('Ping', queue))
    p1.start()
    p2 = Process(target=sub_task2, args=('Pong', queue))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    queue.put(50)
if __name__=='__main__':
    #main1()
    main2()
