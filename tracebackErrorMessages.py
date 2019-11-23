import traceback
from tkinter import Tk,Message

'''
This Python script shows how to see the most recent exception/error from running
some program.

by eutoApps / Eric Utomo
November 2019
'''
try:
    i = 0
    i += 'string'
except:
    print('The error for run number X was:\n')
    traceback.print_exc()

#Eric Utomo
