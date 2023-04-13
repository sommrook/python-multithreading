from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS = [
    'http://www.daum.net/',
    'http://www.cnn.com/',
    'http://naver.com',
    'http://ruliweb.com',
    'http://some-made-up-domain.com'
]

# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    # 프로세스풀 Context 영역
    # with 구문 안에서 실행할 작업물들에 대해 하나하나 loop를 돌면서 익스큐터의 submit메소드로 Futures객체를 만들어줌
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드 (실행x)
        # submit -> 해당 작업이 실행되도록 예약하고 객체의 실행을 나타내는 Future객체를 만들어주는 역할
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}

        print(future_to_url)

        # 실행, dictionary 반복문 시 future은 key값
        # 정의한 작업물들 순서에 상관없이 시간이 적게 걸리는 작업들부터 수행
        for future in as_completed(future_to_url): # timeout=1
            # Key값이 Future객체
            url = future_to_url[future]

            try:
                # 결과
                data = future.result()
            except Exception as exc:
                # 예외 처리
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


if __name__ == '__main__':
    main()