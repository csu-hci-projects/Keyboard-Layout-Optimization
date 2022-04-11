import tkinter as tk
from tkinter import Entry, Label
from tkinter import ttk

import layouts.Dvorak as layout
import utils.time as time

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.title('Keyboard Layout Optimization')
    keyboardApp.iconbitmap('src/utils/images/hciLogo.ico')
    
    readTextBox = Label(keyboardApp, text='Waxy and quivering jocks fumble the pizza', font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11)
    
    entry = Entry(keyboardApp, text='', font=('sans', 20))
    entry.grid(row = 1, columnspan=11)
    
    layout.Dvorak(entry)
    
    start = ttk.Button(text='START', width=8, command= lambda : time.start(entry))
    start.grid(row=6, column=3)
    
    done = ttk.Button(text='DONE', width=8, command= lambda : time.end(keyboardApp, 'Dvorak'))
    done.grid(row=6, column=5)
    
    keyboardApp.mainloop()