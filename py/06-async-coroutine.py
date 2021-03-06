import asyncio
import random

async def call_web_api(url):
    sleeptime = random.randrange(1,5)
    print(f'send a request {url} {sleeptime=}')
    await asyncio.sleep(sleeptime)
    print(f'got a response:{url} {sleeptime=}')
    return url

async def async_download(url):
    response = await call_web_api(url)
    return response

async def main():
    task = await asyncio.gather(
        async_download('https://www.naver.com'),
        async_download('https://www.daum.net'),
        async_download('https://www.google.com')
    )
    return task

result = asyncio.run(main())
print(result)