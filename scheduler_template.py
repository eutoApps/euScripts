import sched
import time

'''
This Python script uses a sched.scheduler to print 5 seconds in the future.
enter vs enterabs: https://docs.python.org/3/library/sched.html

by eutoApps / Eric Utomo
November 2019
'''

s = sched.scheduler(time.time,time.sleep)
e = s.enterabs(time.time()+5,1,print,('...printed 5 seconds later',))
s.run()
#s.cancel() #to cancel a scheduled task

#Eric Utomo
