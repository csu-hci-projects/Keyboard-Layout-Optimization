import tkinter as tk
from tkinter import Entry, Label
from tkinter import ttk

import layouts.QWERTY as layout
import utils.time as time

testTxt = 'THE FIVE BOXING WIZARDS JUMP QUICKLY'

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.title('Keyboard Layout Optimization')
    keyboardApp.iconbitmap('src/utils/images/hciLogo.ico')
    
    readTextBox = Label(keyboardApp, text=testTxt, font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11)
    
    entry = Entry(keyboardApp, text='', font=('sans', 20))
    entry.grid(row = 1, columnspan=11, ipadx=140, pady=20)
    
    layout.QWERTY(entry, False)
    
    start = ttk.Button(text='START', width=8, command= lambda : startClickEvent(entry, keyboardApp))
    start.grid(row=6, column=3)
    
    
    keyboardApp.mainloop()
    
def startClickEvent(entry, keyboardApp):
    time.start(entry)
    done = ttk.Button(text='DONE', width=8, command= lambda : time.end(keyboardApp, 'QWERTY', layout.getInputTxt(), testTxt))
    done.grid(row=6, column=5)