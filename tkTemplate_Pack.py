from tkinter import *

if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    #gui.configure(background="light green") 
  
    # set the title of GUI window 
    gui.title("Wesley Coding Class Example")

    # set the GUI window size
    gui.geometry("400x400")

    # Create a Label
    # Remember, you can set side = CONSTANT as arguments in pack
    label1 = Label(gui, text="Hello, world!", bg='light blue')
    label1.pack(padx=10, pady=10) #if you .pack(), you don't need .grid(), and ViceVersa
    #label1.grid(row=0, column=0, padx=10, pady=10)

    # StringVar() is the variable class for Tkinter
    equation = StringVar()
    # Create an Entry Field
    ef1 = Entry(gui, textvariable=equation) 
    ef1.pack(padx=10, pady=10)
    equation.set('enter your expression')
    
    def create_window():
        window = Toplevel(gui)
        
    # Create a Button
    btn1 = Button(gui, text='Open New Window', command=create_window)
    btn1.pack(padx=10, pady=10)

    # Calling mainloop is always the last line
    gui.mainloop()
