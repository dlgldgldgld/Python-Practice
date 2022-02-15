from concurrent.futures import ThreadPoolExecutor, wait
import threading

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count + 1

class ThreadSafeCounter:
    # Preparing lock
    lock = threading.Lock()
    def __init__(self):
        self.count = 0
    def increment(self):
        with self.lock:
            # 베타 제어할 처리를 록안에 씀
            self.count = self.count + 1     
    
def count_up(counter):
    for _ in range(1000000):
        counter.increment()

def exec_thread( in_counter ) :
    counter = in_counter
    threads = 2
    with ThreadPoolExecutor() as e:
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        done, not_done = wait(futures)

    print(f'{counter.count=:,}')


# Expected result 
# >> counter.count=2,000,000

exec_thread( Counter( ) )
# >> counter.count=1,790,520 ( Fail )
exec_thread( ThreadSafeCounter( ) )
# >> counter.count=2,000,000 ( Succ ) 