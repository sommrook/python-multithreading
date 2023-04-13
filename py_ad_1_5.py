import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info("Sub-Thread %s: starting", name)

    result = 0
    for i in range(10001):
        result = result + i

    logging.info("Sub-Thread %s: finishing result %d", name, result)

    return result


def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M%S")

    logging.info("Main-Thread: before creating and running thread")
    # 실행 방법1
    # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리
    # excutor = ThreadPoolExecutor(max_workers=3)

    # 실행 방법1
    # task1 = excutor.submit(task, ('First',))
    # task2 = excutor.submit(task, ('Two',))

    # 결과 값 있을 경우
    # print(task1.result())
    # print(task2.result())

    # 실행 방법2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ['First', 'Second'])

        # 결과 확인
        print(list(tasks))


# 메인 영역
if __name__ == "__main__":
    main()

