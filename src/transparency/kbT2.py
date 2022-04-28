import tkinter as tk
from tkinter import Entry, Label
from tkinter import ttk

import layouts.Opti as layout
import utils.time as time

testTxt = 'A WIZARDS JOB IS TO VEX CHUMPS QUICKLY IN FOG'

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.title('Keyboard Layout Optimization')
    keyboardApp.iconbitmap('src/utils/images/hciLogo.ico')
    keyboardApp.attributes('-alpha', 0.7)
    
    readTextBox = Label(keyboardApp, text=testTxt, font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11)
    
    entry = Entry(keyboardApp, text='', font=('sans', 20))
    entry.grid(row = 1, columnspan=11, ipadx=205, pady=20)
    
    layout.Opti(entry, True)
    
    start = ttk.Button(text='START', width=8, command= lambda : time.start(entry))
    start.grid(row=8, column=2)
    
    done = ttk.Button(text='DONE', width=8, command= lambda : time.end(keyboardApp, 'Opti Transparent', layout.getInputTxt(), testTxt))
    done.grid(row=8, column=4)
    
    keyboardApp.mainloop()