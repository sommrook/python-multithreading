from multiprocessing import Process
import time
import logging


def proc_func(name):
    print('Sub-Process {}: starting'.format(name))
    time.sleep(3)
    print('Sub-Process {}: finishing'.format(name))


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))

    logging.info('Main-Process: before creating Process')

    # 프로세스
    p.start()

    logging.info('Main-Process: During Process')

    # logging.info('Main-Process: Terminated Process')
    # p.terminate()

    logging.info('Main-Process: Joined Process')
    # sub process가 끝날때 까지 기다림
    p.join()

    print(f'Process p is alive: {p.is_alive()}')


if __name__ == "__main__":
    main()