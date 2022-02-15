from multiprocessing.dummy import freeze_support
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ProcessPoolExecutor, as_completed

import os

def open_browser(site):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(site)
    res = driver.find_element(By.CSS_SELECTOR, '#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(5) > a')
    return [res.text]

def get_multi_process(sites):
    res = []
    with ProcessPoolExecutor() as e:
        futures = [e.submit(open_browser, site) for site in sites ]
        for future in as_completed(futures):
            res.extend(future.result())

    print(res)
    
if __name__ == '__main__':
    freeze_support()
    sites = ['https://www.naver.com'] * os.cpu_count()
    get_multi_process( sites )
