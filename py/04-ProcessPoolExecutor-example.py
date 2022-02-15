import sys

def fibonacci(n):
    a,b = 0, 1
    for _ in range(n):
        a, b = b, b+a
    else :
        return a

import os
import time
def time_checker(f) :
    def wrapper(*args, **kwargs) :
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - st}')
        return v
    return wrapper

@time_checker
def get_sequential(nums):
    for num in nums :
        fibonacci(num)


from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

@time_checker
def get_multi_process(nums):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            future.result()

@time_checker
def get_multi_thread(nums):
    with ThreadPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            future.result()

def main():
    n=int(sys.argv[1])
    print( f'{os.cpu_count()=}' )
    nums = [n] * os.cpu_count()
    get_sequential(nums)
    get_multi_process(nums)
    get_multi_thread(nums)

    # os.cpu_count()=6
    # get_sequential: 52.62162899971008
    # get_multi_process: 9.628000974655151
    # get_multi_thread: 53.63084650039673

if __name__ == '__main__' :
    main()
    
