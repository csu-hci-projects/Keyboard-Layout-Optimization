import tkinter as tk
from tkinter import Entry, Label, Text, Label, Button
from tkinter import ttk

import layouts.Chubon as layout
import utils.time as time


testTxt = 'Please enter your name'
testTxt1 = 'Keyboard Layout Optimization Expirement'

def retrieve_input(textBox, keyboardApp):
    inputValue=textBox.get("1.0","end-1c")
    time.setUser(inputValue)
    keyboardApp.destroy()
    

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.geometry("800x500")
  

    readTextBox = Label(keyboardApp, text=testTxt1, font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11,ipadx=210, pady=20)

    readTextBox = Label(keyboardApp, text=testTxt, font=('sans', 20))
    readTextBox.grid(row=1, columnspan=11,ipadx=210, pady=20)
    
    textBox=Text(keyboardApp, height=2, width=10)
    textBox.grid(row=2, columnspan=11,ipadx=210, pady=20)
    
    buttonCommit=Button(keyboardApp, height=1, width=10, text="Start", 
                    command=lambda: retrieve_input(textBox, keyboardApp))
    buttonCommit.grid(row=3, columnspan=11)

    keyboardApp.mainloop()