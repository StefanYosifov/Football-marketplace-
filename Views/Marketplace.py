from tkinter import *
import tkinter.font as tkFont


def openMarketPlace(root):
    new_window = Toplevel(root)
    new_window.title("New Window")

    label = Label(new_window, text="This is a new window")
    label.pack()

