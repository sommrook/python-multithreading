import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event):
    """ 네트워크 대기 상태라 가정(서버) """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info('Producer got message: %s', message)
        queue.put(message)

    logging.info('Producer received event Exiting')

# 소비자
def consumer(queue, event):
    """ 응답 받고 소비하는 것으로 가정 or DB 저장 """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info('Consumer storing message: %s (size=%d)', message, queue.qsize())

    logging.info('Consumer received event Exiting')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # With Context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # 실행 시간 조정
        time.sleep(0.1)

        logging.info('Main : about to set event')

        # 프로그램 종료
        event.set()


