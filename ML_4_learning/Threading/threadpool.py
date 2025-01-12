# multi threading with thread pool exector

from concurrent.futures import ThreadPoolExecutor
import time

def print_no(num):
    time.sleep(1)
    return f"number: {num}"

num= [1,2,3,4,5,6]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_no, num)

for results in results:
    print (results)
