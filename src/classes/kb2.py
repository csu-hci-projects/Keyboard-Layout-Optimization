import tkinter as tk
from tkinter import ttk

import layouts.Opti as layout


class GUI(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Keyboard Layout Optimization')
        self.iconbitmap('src/utils/images/hciLogo.ico')
        self.geometry('1080x720')
        
        self.textBox = tk.StringVar()
        
        self.readBox()
        self.typeBox()
        self.keyboard()
        
    def readBox(self):
        read = tk.Text(self, height=1, width=50)
        read.config(state='normal')
        read.insert(tk.INSERT, "A wizard's job is to vex chumps quickly in fog")
        read.grid(row=1, columnspan= 60, ipadx= 999, ipady=1)
        
    def typeBox(self):
        entry = ttk.Entry(self, state='readonly', textvariable=self.typeBox)
        entry.grid(row=2, columnspan= 100, ipadx= 999, ipady=5)
        
    def keyboard(self):
        layout.Opti()