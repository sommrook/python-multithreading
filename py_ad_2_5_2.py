from multiprocessing import Process, current_process, Value, Array
import os

# 프로세스 메모리 공유 예제(공유 O)

# 실행함수
def generate_update_number(v: int):
    for _ in range(50):
        v.value += 1
    print(current_process().name, "data", v.value)

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent process ID {parent_process_id}')

    # 프로세스 리스트 선언
    process = list()

    # 프로세스 메모리 공유 변수
    # from multiprocess import shared_memory 사용 가능(파이썬 3.8)
    # from multiprocess import Manager 사용 가능
    # share_numbers = Array('i', range(50))
    share_value = Value('i', 0)

    for _ in range(1, 10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    # 최종 프로세스 부모 변수 확인
    print('Final Data in parent process', share_value.value)


if __name__ == "__main__":
    main()