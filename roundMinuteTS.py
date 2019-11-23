import time,datetime
from datetime import datetime as dtM #datetime module

'''
This Python function takes a timestamp and returns it
rounded to the nearest minute.

by eutoApps / Eric Utomo
November 2019
'''
def roundMinuteTS(timeStamp0):
    #Make a datetime from the timestamp
    dt = dtM.fromtimestamp(timeStamp0)
    #Round to the nearest minute
    if dt.second < 30:
        dt -= datetime.timedelta(0,dt.second)
    else: dt += datetime.timedelta(0,60-dt.second)
    #Convert datetime back to timestamp
    timeStamp = dtM.timestamp(dt)
    return timeStamp


#To test the function
def test_roundMinuteTS():
    currentTS = time.time()
    print('Current timestamp: {}'.format(currentTS))
    currentDT = dtM.fromtimestamp(currentTS).strftime('%H-%M-%S')
    print('Current datetime: {}'.format(currentDT))
    roundedTS = roundMinuteTS(currentTS)
    print('Rounded timestamp: {}'.format(roundedTS))
    roundedDT = dtM.fromtimestamp(roundedTS).strftime('%H-%M-%S')
    print('Rounded datetime: {}'.format(roundedDT))                               

#Eric Utomo
#test_roundMinuteTS()
