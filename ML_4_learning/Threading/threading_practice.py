## MULTI THREADING
#USED WHEN: 
# 1. tasks that spend more time for I/O kinda operations
# 2. Concurrent executions of multiple operations

import threading
import time

def print_no():
    for i in range (5):
        time.sleep(2)
        print (f" number : :{i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f" letters: {letter}")

#t= time.time()
#print_no()
#print_letters()

#finished_time= time.time() -t
#print(finished_time)

'''
OUTPUT: 
 number : :0
 number : :1
 number : :2
 number : :3
 number : :4
 letters: a
 letters: b
 letters: c
 letters: d
 letters: e
20.01395082473755

'''

#Implementing the threading on the above code to exceute both functions at same time on different threads
t1=threading.Thread(target= print_no)
t2=threading.Thread(target=print_letters)

t= time.time()
#print_no()
#print_letters()
#INSTEAD OF THE ABOVE FUNCTION CALLS, WE CALL THREADS
t1.start()
t2.start()

## wait for the threads to completeto synchronize threads.
#  It guarantees that certain operations are completed before moving on to others,
t1.join()
t2.join()

finished_time= time.time() -t
print(finished_time)
'''
OUTPUT:
number : :0
 letters: a
 number : :1
 letters: b
 number : :2
 letters: c
 number : :3
 letters: d
 number : :4
 letters: e
10.009323120117188

'''