import tkinter as tk
from tkinter import Entry, Label
from tkinter import ttk

import layouts.SquareAlphabetic as layout
import utils.time as time

testTxt = 'SYMPATHIZING WOULD FIX QUAKER OBJECTIVES'

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.title('Keyboard Layout Optimization')
    keyboardApp.iconbitmap('src/utils/images/hciLogo.ico')
    
    readTextBox = Label(keyboardApp, text=testTxt, font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11)
    
    entry = Entry(keyboardApp, text='', font=('sans', 20))
    entry.grid(row = 1, columnspan=11, ipadx=180, pady=20)
    
    layout.SquareAlphabetic(entry)
    
    start = ttk.Button(text='START', width=8, command= lambda : time.start(entry))
    start.grid(row=8, column=2)
    
    done = ttk.Button(text='DONE', width=8, command= lambda : time.end(keyboardApp, 'Square Alphabetic', layout.getInputTxt(), testTxt))
    done.grid(row=8, column=4)
    
    keyboardApp.mainloop()