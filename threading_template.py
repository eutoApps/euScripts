import threading

'''
This Python script starts a thread, freeing the main program while handling a
time-consuming task in the background. Threads auto-stop when their task is done.

by eutoApps / Eric Utomo
November 2019
'''
def startThread():
    '''
    #Try calling task here instead of while threading, to see the difference
    task()
    '''
    t = threading.Thread(target=task)
    t.start()

#an example, time-consuming task
def task():
    x=200000000
    while x>0:
        x-=1

#Eric Utomo
#startThread()
