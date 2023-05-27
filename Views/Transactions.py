from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from FileOperations.reader import readFromFile 


def openTransactions(self):
    new_window = Toplevel(self)
    new_window.title("New Window")
    width = 600
    height = 400
    screenwidth = new_window.winfo_screenwidth()
    screenheight = new_window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    new_window.geometry(alignstr)
    new_window.resizable(width=False, height=False)

    label = Label(new_window, text="This is a new window")
    label.pack()

    new_window.title("Transactions")
    width = 800
    height = 750
    screenwidth = new_window.winfo_screenwidth()
    screenheight = new_window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    new_window.geometry(alignstr)
    new_window.resizable(width=False, height=False)

    def GRadio_300_command():
        print("in")
        dictionaryFromFile=readFromFile("Transactions.txt")
        data = [[key] + values for key, values in dictionaryFromFile.items()]
        data = [arr for arr in data if "In" in arr]
        createTree(new_window,data)
    
    def GRadio_164_command():
        print("out")
        dictionaryFromFile=readFromFile("Transactions.txt")
        data = [[key] + values for key, values in dictionaryFromFile.items()]
        data = [arr for arr in data if "Out" in arr]
        createTree(new_window,data)

    def GRadio_638_command():
        print("all")
        dictionaryFromFile=readFromFile("Transactions.txt")
        data = [[key] + values for key, values in dictionaryFromFile.items()]
        createTree(new_window,data)

    def createDesign(new_window):
        selected_option = StringVar()  

        GRadio_300 = tk.Radiobutton(new_window)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_300["font"] = ft
        GRadio_300["fg"] = "#333333"
        GRadio_300["justify"] = "center"
        GRadio_300["text"] = "In"
        GRadio_300.place(x=30, y=100, width=85, height=25)
        GRadio_300["command"] = GRadio_300_command
        GRadio_300["variable"] = selected_option
        GRadio_300["value"] = "In"

        GRadio_164 = tk.Radiobutton(new_window)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_164["font"] = ft
        GRadio_164["fg"] = "#333333"    
        GRadio_164["justify"] = "center"
        GRadio_164["text"] = "Out"
        GRadio_164.place(x=120, y=100, width=85, height=25)
        GRadio_164["command"] = GRadio_164_command
        GRadio_164["variable"] = selected_option
        GRadio_164["value"] = "Out"

        GRadio_638 = tk.Radiobutton(new_window)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_638["font"] = ft
        GRadio_638["fg"] = "#333333"
        GRadio_638["justify"] = "center"
        GRadio_638["text"] = "All"
        GRadio_638.place(x=220, y=100, width=85, height=25)
        GRadio_638["command"] = GRadio_638_command
        GRadio_638["variable"] = selected_option
        GRadio_638["value"] = "All"

        selected_option.set(None)  

    createDesign(new_window)

def createTree(new_window,data):
    tree = ttk.Treeview(new_window)
    tree["columns"] = ("Football player", "Birth Year", "Club", "Height", "Weight", "Age", "Position")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Football player", width=120)  
    tree.column("Birth Year", width=100)
    tree.column("Club", width=150)
    tree.column("Height", width=50)
    tree.column("Weight", width=50)
    tree.column("Age", width=50)
    tree.column("Position", width=100)

    tree.heading("#0", text="Football player") 
    tree.heading("Football player", text="Football player") 
    tree.heading("Birth Year", text="Birth Year")
    tree.heading("Club", text="Club")
    tree.heading("Height", text="Height")
    tree.heading("Weight", text="Weight")
    tree.heading("Age", text="Age")
    tree.heading("Position", text="Position")

    for element in data:
        tree.insert("", tk.END,values=element)

    tree.place(x=0, y=330)

