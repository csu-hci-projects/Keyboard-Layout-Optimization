import tkinter as tk
from tkinter import ttk

hold = " "

def press(char):
    global hold
    hold += char

class Chubon(tk.Tk):
    
    def __init__(self):
        self.layout()
        
        
    def layout(self):
        V = ttk.Button(text = 'V' , width = 6, command = lambda : press('V'))
        V.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)
        
        U = ttk.Button(text = 'U' , width = 6, command = lambda : press('U'))
        U.grid(row = 3 , column = 9, ipadx = 6 , ipady = 10)
        
        P = ttk.Button(text = 'P' , width = 6, command = lambda : press('P'))
        P.grid(row = 3 , column = 10, ipadx = 6 , ipady = 10)
        
        
        # SECOND ROW
        Q = ttk.Button(text = 'Q' , width = 6, command = lambda : press('Q'))
        Q.grid(row = 4 , column = 5, ipadx = 6 , ipady = 10)
        
        M = ttk.Button(text = 'M' , width = 6, command = lambda : press('M'))
        M.grid(row = 4 , column = 6, ipadx = 6 , ipady = 10)
        
        I = ttk.Button(text = 'I' , width = 6, command = lambda : press('I'))
        I.grid(row = 4 , column = 7, ipadx = 6 , ipady = 10)
        
        T = ttk.Button(text = 'T' , width = 6, command = lambda : press('T'))
        T.grid(row = 4 , column = 8, ipadx = 6 , ipady = 10)
        
        S = ttk.Button(text = 'S' , width = 6, command = lambda : press('S'))
        S.grid(row = 4 , column = 9, ipadx = 6 , ipady = 10)
        
        C = ttk.Button(text = 'C' , width = 6, command = lambda : press('C'))
        C.grid(row = 4 , column = 10, ipadx = 6 , ipady = 10)
        
        K = ttk.Button(text = 'K' , width = 6, command = lambda : press('K'))
        K.grid(row = 4 , column = 11, ipadx = 6 , ipady = 10)
        
        Z = ttk.Button(text = 'Z' , width = 6, command = lambda : press('Z'))
        Z.grid(row = 4 , column = 12, ipadx = 6 , ipady = 10)
        
        
        # THIRD ROW
        J = ttk.Button(text = 'J' , width = 6, command = lambda : press('J'))
        J.grid(row = 5 , column = 4, ipadx = 6 , ipady = 10)
        
        G = ttk.Button(text = 'G' , width = 6, command = lambda : press('G'))
        G.grid(row = 5 , column = 5, ipadx = 6 , ipady = 10)
        
        N = ttk.Button(text = 'N' , width = 6, command = lambda : press('N'))
        N.grid(row = 5 , column = 6, ipadx = 6 , ipady = 10)     
        
        R = ttk.Button(text = 'R' , width = 6, command = lambda : press('R'))
        R.grid(row = 5 , column = 7, ipadx = 6 , ipady = 10)
        
        E = ttk.Button(text = 'E' , width = 6, command = lambda : press('E'))
        E.grid(row = 5 , column = 8, ipadx = 6 , ipady = 10)
        
        H = ttk.Button(text = 'H' , width = 6, command = lambda : press('H'))
        H.grid(row = 5 , column = 9, ipadx = 6 , ipady = 10)
        
        B = ttk.Button( text= 'B' , width = 6 , command = lambda : press('B'))
        B.grid(row = 5 , column = 10 , ipadx = 6 ,ipady = 10)
        
        Y = ttk.Button(text = 'Y' , width = 6, command = lambda : press('Y'))
        Y.grid(row = 5 , column = 11, ipadx = 6 , ipady = 10)
        
        X = ttk.Button(text = 'X' , width = 6, command = lambda : press('X'))
        X.grid(row = 5 , column = 12, ipadx = 6 , ipady = 10)
        
        
        # FOURTH ROW
        F = ttk.Button(text = 'F' , width = 6, command = lambda : press('F'))
        F.grid(row = 6 , column = 5, ipadx = 6 , ipady = 10)
        
        O = ttk.Button(text = 'O' , width = 6, command = lambda : press('O'))
        O.grid(row = 6 , column = 6, ipadx = 6 , ipady = 10)
        
        A = ttk.Button(text = 'A' , width = 6, command = lambda : press('A'))
        A.grid(row = 6 , column = 7, ipadx = 6 , ipady = 10)
        
        D = ttk.Button(text = 'D' , width = 6, command = lambda : press('D'))
        D.grid(row = 6 , column = 8, ipadx = 6 , ipady = 10)
        
        L = ttk.Button(text = 'L' , width = 6, command = lambda : press('L'))
        L.grid(row = 6 , column = 9, ipadx = 6 , ipady = 10)
        
        W = ttk.Button(text = 'W' , width = 6, command = lambda : press('W'))
        W.grid(row = 6 , column = 10, ipadx = 6 , ipady = 10)
        
        period = ttk.Button(text = '.' , width = 6, command = lambda : press('.'))
        period.grid(row = 6 , column = 11, ipadx = 6 , ipady = 10)
        
        comma = ttk.Button(text = ',' , width = 6, command = lambda : press(','))
        comma.grid(row = 6 , column = 12, ipadx = 6 , ipady = 10)