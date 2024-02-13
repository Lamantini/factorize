from multiprocessing import Pipe, Process, current_process
from time import sleep
import time
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

a, sender1 = Pipe()
b, sender2 = Pipe()
c, sender3 = Pipe()
d, sender4 = Pipe()

def factorize(*number):
    # YOUR CODE HERE
    factor_list = []

    for num in number:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        factor_list.append(factors)

    return factor_list

start_time = time.time()

def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = pipe.recv()
    logger.debug(factorize(val))
    sys.exit(0)

end_time = time.time()
execution_time = end_time - start_time

'''assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]'''

if __name__ == '__main__':
    w1 = Process(target=worker, args=(a, ))
    w2 = Process(target=worker, args=(b, ))
    w3 = Process(target=worker, args=(c, ))
    w4 = Process(target=worker, args=(d, ))

    w1.start()
    w2.start()
    w3.start()
    w4.start()

    sender1.send(128)
    sleep(1)
    sender2.send(255)
    sleep(1)
    sender3.send(99999)
    sleep(1)
    sender4.send(10651060)

print(a)
print(b)
print(c)
print(d)
print("Час виконання функції: ", execution_time, "секунд")
#Час виконання 9 сек