import logging
import threading
import time


# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)

    for i in d:
        print(i)

    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역
if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    # deamon : default false
    # deamon thread는 메인 스레드 종료시 종 ex)만약 크롬 브라우저 창 닫으면 모든 스레드 다 닫음
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Two', range(10000)), daemon=True)

    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()
    y.start()

    # deamonthread 확인
    print(x.isDaemon())

    # deamon 스레드인데 join을 쓰는것은 좋지 못한 코드이다..!
    # x.join()
    # y.join()

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: all done")

