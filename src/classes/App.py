import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Keyboard Layout Optimization')
        self.iconbitmap('src/utils/images/hciLogo.ico')
        self.geometry('1080x720')
        
        self.textBox = tk.StringVar()
        
        self.readBox()
        self.typeBox()
        
    def readBox(self):
        entry = ttk.Entry(self, state='readonly', textvariable=self.readBox)
        entry.grid(rowspan=1, columnspan= 100, ipadx= 999, ipady=5)
        
    def typeBox(self):
        entry = ttk.Entry(self, state='readonly', textvariable=self.typeBox)
        entry.grid(rowspan=1, columnspan= 100, ipadx= 999, ipady=5)