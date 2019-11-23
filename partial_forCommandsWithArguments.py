from functools import partial
from tkinter import Tk,StringVar,Button,Label

'''
partial allows passing arguments along with function calls, as one command.

by eutoApps / Eric Utomo
November 2019
'''
mw = Tk()
labelSV = StringVar()

def smileBecause(reason):
    labelSV.set(reason)

    #partial allows us to send arguments to our commanded function
button = Button(mw,text='Smile because...',
                command=partial(smileBecause,'Jesus loves you!'))
button.pack()

label = Label(mw,textvariable=labelSV)
label.pack()

mw.mainloop()

#Eric Utomo
