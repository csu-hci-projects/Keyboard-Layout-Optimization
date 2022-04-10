import tkinter as tk
from tkinter import ttk

import layouts.Chubon as layout

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
        read.insert(tk.INSERT, "The quick brown fox jumps over the lazy dog")
        read.config(state='disable')
        read.grid(row=1, columnspan= 60, ipadx= 999, ipady=1)
        
    def typeBox(self):
        read = tk.Text(self, height=1, width=50)
        read.config(state='normal')
        read.insert(tk.INSERT, layout.participantInput())
        read.grid(row=2, columnspan= 60, ipadx= 999, ipady=1)
        # entry = ttk.Entry(self, state='readonly', textvariable=self.typeBox)
        # entry.grid(row=2, columnspan= 60, ipadx= 1140, ipady=5)
        
    def keyboard(self):
        layout.Chubon()