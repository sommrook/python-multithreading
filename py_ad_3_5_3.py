import time
import asyncio

# async io basic 예제

"""
동시 프로그래밍 패러다임 변화
싱글 코어 -> 처리 향상 미미, 저하 -> 비동기 프로그래밍 -> CPU연산, DB연동, API 호출 대기 시간 늘어남
파이썬 3.4 -> 비동기(asyncio) 표준 라이브러리 등장
"""

async def exe_calcurate_async(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        await asyncio.sleep(1)
    print(f'{name} - {n} working done!')


async def process_async():
    start = time.time()

    # await exe_calcurate_async('One', 3)
    # await exe_calcurate_async('Two', 2)
    # await exe_calcurate_async('Three', 1)

    await asyncio.wait([
        exe_calcurate_async('One', 3),
        exe_calcurate_async('Two', 2),
        exe_calcurate_async('Three', 1)
    ])

    end =  time.time()

    print(f'>>> total seconds : {end - start}')

def exe_calcurate_sync(name, n):
    for i in range(1, n + 1):
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} working done!')

def process_sync():
    start = time.time()

    exe_calcurate_sync('One', 3)
    exe_calcurate_sync('Two', 2)
    exe_calcurate_sync('Three', 1)

    end =  time.time()

    print(f'>>> total seconds : {end - start}')


if __name__ == '__main__':
    # Sync 실행
    # process_sync()

    # Async 실행
    # 파이썬 3.7 이상
    asyncio.run(process_async())
    # asyncio.get_event_loop().run_until_complete(process_async())