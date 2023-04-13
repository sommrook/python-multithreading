# 프로세스 통신 구현 Pipe

from multiprocessing import Process, Pipe, current_process
import time
import os

# 실행함수
def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0

    for i in range(baseNum):
        sub_total += 1

    conn.send(sub_total)
    conn.close()

    print(f'Process ID: {process_id}, Process Name: {process_name}, ID: {id}')
    print(f'Result: {sub_total}')


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent process ID{parent_process_id}')

    # 시작 시간
    start_time = time.time()

    # Pipe 선언
    parent_conn, child_conn = Pipe()

    t = Process(name=str(1), target=worker, args=(1, 100000000, child_conn))

    t.start()

    t.join()

    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))

    print('Main-Processing Total Count={}'.format(parent_conn.recv()))
    print('Main-Processing Done!')


if __name__ == "__main__":
    main()