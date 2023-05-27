from tkinter import *
import tkinter.font as tkFont
import tkinter as tk


def GRadio_300_command():
    print("command")


def GRadio_164_command():
    print("command")


def GRadio_638_command():
    print("command")


def openTransactions():
    root = Tk()
    root.title("Main Window")

    # setting window size
    width = 600
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    def openNewWindow():
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

        GRadio_300 = tk.Radiobutton(new_window)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_300["font"] = ft
        GRadio_300["fg"] = "#333333"
        GRadio_300["justify"] = "center"
        GRadio_300["text"] = "In"
        GRadio_300.place(x=30, y=100, width=85, height=25)
        GRadio_300["command"] = GRadio_300_command

        GRadio_164 = tk.Radiobutton(new_window)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_164["font"] = ft
        GRadio_164["fg"] = "#333333"
        GRadio_164["justify"] = "center"
        GRadio_164["text"] = "Out"
        GRadio_164.place(x=120, y=100, width=85, height=25)
        GRadio_164["command"] = GRadio_164_command

        GRadio_638 = tk.Radiobutton(new_window)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_638["font"] = ft
        GRadio_638["fg"] = "#333333"
        GRadio_638["justify"] = "center"
        GRadio_638["text"] = "All"
        GRadio_638.place(x=220, y=100, width=85, height=25)
        GRadio_638["command"] = GRadio_638_command

    open_button = Button(root, text="Open New Window", command=openNewWindow)
    open_button.pack()

    root.mainloop()


openTransactions()