import tkinter as tk
from tkinter import ttk

inputTxt = ''

def getInputTxt():
    global inputTxt
    
    return inputTxt

def press(click, entry):
    global inputTxt
    inputTxt += click
    
    if (click == ' '):
        entry.insert(tk.END, ' ')
    else:
        entry.insert(tk.END, click)

def QWERTYT(entry):
    Q = ttk.Button(text = 'Q' , width = 6, command = lambda : press('Q', entry))
    Q.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)

    W = ttk.Button(text = 'W' , width = 6, command = lambda : press('W', entry))
    W.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

    E = ttk.Button(text = 'E' , width = 6, command = lambda : press('E', entry))
    E.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

    R = ttk.Button(text = 'R' , width = 6, command = lambda : press('R', entry))
    R.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)

    T = ttk.Button(text = 'T' , width = 6, command = lambda : press('T', entry))
    T.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)

    Y = ttk.Button(text = 'Y' , width = 6, command = lambda : press('Y', entry))
    Y.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)

    U = ttk.Button(text = 'U' , width = 6, command = lambda : press('U', entry))
    U.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)

    I = ttk.Button(text = 'I' , width = 6, command = lambda : press('I', entry))
    I.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

    O = ttk.Button(text = 'O' , width = 6, command = lambda : press('O', entry))
    O.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)

    P = ttk.Button(text = 'P' , width = 6, command = lambda : press('P', entry))
    P.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)
    
    # SECOND ROW
    A = ttk.Button(text = 'A' , width = 6, command = lambda : press('A', entry))
    A.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)

    S = ttk.Button(text = 'S' , width = 6, command = lambda : press('S', entry))
    S.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)

    D = ttk.Button(text = 'D' , width = 6, command = lambda : press('D', entry))
    D.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)

    F = ttk.Button(text = 'F' , width = 6, command = lambda : press('F', entry))
    F.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)

    G = ttk.Button(text = 'G' , width = 6, command = lambda : press('G', entry))
    G.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)

    H = ttk.Button(text = 'H' , width = 6, command = lambda : press('H', entry))
    H.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)

    J = ttk.Button(text = 'J' , width = 6, command = lambda : press('J', entry))
    J.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)

    K = ttk.Button(text = 'K' , width = 6, command = lambda : press('K', entry))
    K.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)

    L = ttk.Button(text = 'L' , width = 6, command = lambda : press('L', entry))
    L.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)
    
    # THIRD ROW
    Z = ttk.Button(text = 'Z' , width = 6, command = lambda : press('Z', entry))
    Z.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)

    X = ttk.Button(text = 'X' , width = 6, command = lambda : press('X', entry))
    X.grid(row = 4 , column = 2, ipadx = 6 , ipady = 10)

    C = ttk.Button(text = 'C' , width = 6, command = lambda : press('C', entry))
    C.grid(row = 4 , column = 3, ipadx = 6 , ipady = 10)

    V = ttk.Button(text = 'V' , width = 6, command = lambda : press('V', entry))
    V.grid(row = 4 , column = 4, ipadx = 6 , ipady = 10)

    B = ttk.Button( text= 'B' , width = 6 , command = lambda : press('B', entry))
    B.grid(row = 4 , column = 5 , ipadx = 6 ,ipady = 10)

    N = ttk.Button(text = 'N' , width = 6, command = lambda : press('N', entry))
    N.grid(row = 4 , column = 6, ipadx = 6 , ipady = 10)

    M = ttk.Button(text = 'M' , width = 6, command = lambda : press('M', entry))
    M.grid(row = 4 , column = 7, ipadx = 6 , ipady = 10)
    
    
    #SIXTH ROW
    space = ttk.Button(text = 'Space' , width = 40, command = lambda : press(' ', entry))
    space.grid(row = 5 , columnspan= 10, ipadx = 6 , ipady = 10)