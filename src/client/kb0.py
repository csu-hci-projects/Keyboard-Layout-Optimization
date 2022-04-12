import tkinter as tk
from tkinter import Entry, Label
from tkinter import ttk

import layouts.Chubon as layout
import utils.time as time

testTxt = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.title('Keyboard Layout Optimization')
    keyboardApp.iconbitmap('src/utils/images/hciLogo.ico')
    
    readTextBox = Label(keyboardApp, text=testTxt, font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11)
    
    entry = Entry(keyboardApp, text='', font=('sans', 20))
    entry.grid(row = 1, columnspan=11)
    
    layout.Chubon(entry)
    
    start = ttk.Button(text='START', width=8, command= lambda : time.start(entry))
    start.grid(row=10, column=3)
    
    done = ttk.Button(text='DONE', width=8, command= lambda : time.end(keyboardApp, 'Chubon', layout.getInputTxt(), testTxt))
    done.grid(row=10, column=5)
    
    keyboardApp.mainloop()