import tkinter as tk
from tkinter import Entry, Label, Text, Label, Button
from tkinter import ttk

import layouts.Chubon as layout
import utils.time as time


testTxt = 'Please enter your name'
testTxt1 = 'Keyboard Layout Optimization Expirement'

def GUI():    
    keyboardApp = tk.Tk()
    keyboardApp.geometry("800x500")
  

    readTextBox = Label(keyboardApp, text=testTxt1, font=('sans', 20))
    readTextBox.grid(row=0, columnspan=11,ipadx=210, pady=20)

    readTextBox = Label(keyboardApp, text=testTxt, font=('sans', 20))
    readTextBox.grid(row=1, columnspan=11,ipadx=210, pady=20)
    
    textBox=Text(keyboardApp, height=2, width=10)
    textBox.grid(row=2, columnspan=11,ipadx=210, pady=20)
