import multiprocessing
from datetime import datetime
import threading


def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')
    all_data += file.readlines()
    file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    time_start = datetime.now()
    for i in filenames:
        read_info(i)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)

    time_start = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as multproc:
        multproc.map(read_info, filenames)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)
