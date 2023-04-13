import asyncio
import aiohttp
import time
# py_ad_3_4보다 빠름
# asyncio 예제
# threading 보다 높은 코드 복잡도 -> Async, Await 적절하게 코딩

# 실행함수1(다운로드)
async def request_site(session, url):
    # 세션 확인
    # print(session)
    async with session.get(url) as response:
        print('Read Contents {0}, from {1}'.format(response, url))


# 실행함수2(요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
        # print(*tasks)
        # print(tasks)
        await asyncio.gather(*tasks, return_exceptions=True)


def main():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 5

    # 실행 시간 측정
    start_time = time.time()

    asyncio.run(request_all_sites(urls))
    # asyncio.get_event_loop().run_until_complete(request_all_sites(urls))

    # 실헹 시간 종료
    duration = time.time() - start_time

    print()

    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == "__main__":
    main()