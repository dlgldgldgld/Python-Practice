# 시간 측정용 time_checker 
import time
def time_checker(f) :
    def wrapper(*args, **kwargs) :
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - st}')
        return v
    return wrapper


# down 받을 url + download function
urls = [
    'https://twitter.com',
    'https://facebook.com',
    'https://instagram.com',
]

from hashlib import md5
from pathlib import Path
from urllib import request
def download(url):
    req = request.Request(url)
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path

# 순차 실행
@time_checker
def get_sequential():
    for url in urls :
        print(download(url))

# 다중 스레드
from concurrent.futures import ThreadPoolExecutor, as_completed
@time_checker
def get_multi_thread():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download, url) for url in urls]
        for future in as_completed(futures):
            print(future.result())

get_sequential()
get_multi_thread()