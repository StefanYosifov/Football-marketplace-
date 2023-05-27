from tkinter import *
import tkinter.font as tkFont
import tkinter as tk

def openMarketPlace(root):
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

    GListBox_710 = tk.Listbox(new_window)  # Use new_window instead of root
    GListBox_710["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    GListBox_710["font"] = ft
    GListBox_710["fg"] = "#333333"
    GListBox_710["justify"] = "center"
    GListBox_710.place(x=10, y=40, width=150, height=40)

    def readFromFile(filename):
        with open(filename, "r") as file:
            footballers = file.readlines()
        return footballers

    Footballers = readFromFile("Marketplace.txt")

    for footballer in Footballers:
        GListBox_710.insert(tk.END, footballer.strip())

    GLabel_887 = tk.Label(new_window)  # Use new_window instead of root
    ft = tkFont.Font(family='Times', size=10)
    GLabel_887["font"] = ft
    GLabel_887["fg"] = "#333333"
    GLabel_887["justify"] = "center"
    GLabel_887["text"] = "label"
    GLabel_887.place(x=160, y=40, width=70, height=40)

    GLabel_234 = tk.Label(new_window)  # Use new_window instead of root
    ft = tkFont.Font(family='Times', size=10)
    GLabel_234["font"] = ft
    GLabel_234["fg"] = "#333333"
    GLabel_234["justify"] = "center"
    GLabel_234["text"] = "label"
    GLabel_234.place(x=230, y=40, width=70, height=40)

    GLabel_791 = tk.Label(new_window)  # Use new_window instead of root
    ft = tkFont.Font(family='Times', size=10)
    GLabel_791["font"] = ft
    GLabel_791["fg"] = "#333333"
    GLabel_791["justify"] = "center"
    GLabel_791["text"] = "label"
    GLabel_791.place(x=300, y=40, width=70, height=40)

    GLabel_973 = tk.Label(new_window)  # Use new_window instead of root
    ft = tkFont.Font(family='Times', size=10)
    GLabel_973["font"] = ft
    GLabel_973["fg"] = "#333333"
    GLabel_973["justify"] = "center"
    GLabel_973["text"] = "label"
    GLabel_973.place(x=370, y=40, width=70, height=40)

    GLabel_512 = tk.Label(new_window)  # Use new_window instead of root
    ft = tkFont.Font(family='Times', size=10)
    GLabel_512["font"] = ft
    GLabel_512["fg"] = "#333333"
    GLabel_512["justify"] = "center"
    GLabel_512["text"] = "label"
    GLabel_512.place(x=440, y=40, width=70, height=40)

    GLabel_751 = tk.Label(new_window)  # Use new_window instead of root
    ft = tkFont.Font(family='Times', size=10)
    GLabel_751["font"] = ft
    GLabel_751["fg"] = "#333333"
    GLabel_751["justify"] = "center"
    GLabel_751["text"] = "label"
    GLabel_751.place(x=510, y=40, width=70, height=40)

# Create the main window
root = tk.Tk()
openMarketPlace(root)
root.mainloop()
