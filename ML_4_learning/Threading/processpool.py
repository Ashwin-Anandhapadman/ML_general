#process pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def sqaure_num(num):
    time.sleep(1)
    return f"sqaure: {num * num}"

num= [1,2,3,4,5,6,9]

if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3)as executor:
        results= executor.map(sqaure_num, num)

    for results in results:
        print(results)