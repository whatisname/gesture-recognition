# -*- coding: utf-8 -*-
"""
Created on Sat May 25 05:34:23 2019
@author: XX
Reference: https://www.geeksforgeeks.org/python-gui-tkinter/
"""

import tkinter as tk

def fetch(entry):
    print('%s: "%s"' % (entry[0], entry[1].get()))

field = 'number'

def makeform(root):
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text=field, anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    return (field, ent)

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root)
    root.bind('aaa', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.destroy)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()