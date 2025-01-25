#to run processes in parallel
#REASONS TO USE:
    #1. CPU-bound computation heavy tasks like mathematical ops. ; data processing
    #2. Parallel exectution with multiple cores of CPU

import multiprocessing
import time

def square_no():
    for i in  range(5):
        time.sleep(1)
        print(f"square is: {i*i}")

def cube_no():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube is: {i*i*i}")

'''
Using if __name__ == "__main__": is a best practice in Python programming that enhances 
ensures that certain parts of your code only run when intended, 
making your scripts more robust and easier to maintain.

In another script...if we want to run a function called my_module that we 
created in some other script, we can import the functio and run:
By explicitly calling my_module.main() in your importing script, 
you can execute the main() function even when the module is imported. 


'''

if __name__=="__main__":

    ## create 2 processes
    p1=multiprocessing.Process(target=square_no)
    p2=multiprocessing.Process(target=cube_no)


    t_p= time.time()
    # start the process
    p1.start()
    p2.start()

    ## wait for completion to add up time
    p1.join()
    p2.join()

    finished_process_time= time.time() - t_p
    print(finished_process_time)

'''
OUTPUT: 
square is: 0
cube is: 0
square is: 1
cube is: 1
square is: 4
square is: 9
cube is: 8
square is: 16
cube is: 27
cube is: 64
7.605961084365845
'''
    