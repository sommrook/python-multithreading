import logging
from concurrent.futures import ThreadPoolExecutor
import time


class FakeDataStore:
    # 스택 영역, 공유 변수(value)
    def __init__(self):
        # 데이터 영역
        self.value = 0

    # 변수 업데이트 함수
    def update(self, n):
        logging.info('Thread %s: starting update', n)

        #뮤텍스 & Lock 등 동기화(Thread synchronization 필요) -> 스레드가 동시에 접근하면 의도한대로 프로그램 결과가 나오지 않음
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info('Thread %s: finishing update', n)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    store = FakeDataStore()

    logging.info('Testing update. Starting value is %d', store.value)

    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info('Testing update. Finishing value is %d', store.value)