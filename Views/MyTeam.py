from tkinter import *
import tkinter.font as tkFont


def openMyTeam(root):
    new_window = Toplevel(root)
    new_window.title("New Window")
    width = 600
    height = 400
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    new_window.geometry(alignstr)
    new_window.resizable(width=False, height=False)

    label = Label(new_window, text="This is a new window")
    label.pack()

