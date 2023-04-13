import concurrent.futures
import threading
import requests
import time
# py_ad_3_4보다 빠름
# multi thread 예제

# 각 스레드에 생성되는 객체(독립된 네임스페이스)
thread_local = threading.local()

def get_session():
    # 애트리뷰트가 있는지 확인
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


# 실행함수1(다운로드)
def request_site(url):
    # 세션 획득
    session = get_session()

    # 세션 확인
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Ststus Code : {response.status_code} from {url}]')


# 실행함수2(요청)
def request_all_sites(urls):
    # 멀티스레드 실행
    # 반드시 max_worker 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executer:
        executer.map(request_site, urls)


def main():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 5

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 실헹 시간 종료
    duration = time.time() - start_time

    print()

    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == "__main__":
    main()