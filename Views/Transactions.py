from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from FileOperations.reader import readFromFile 
from Util.image import loadImage



def openTransactions(self):
    new_window = Toplevel(self)
    image_file = "/Files/Images/Transferwindow.png"
    loadImage(new_window,image_file)

    
    new_window.title("Transactions")
    width = 1000
    height = 670
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
    tree["columns"] = ("Football player", "Club", "Price", "Position", "Date of Transfer", "In/Out", )

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Football player", width=200)  
    tree.column("Club", width=100)
    tree.column("Price", width=50)
    tree.column("Position", width=150)
    tree.column("Date of Transfer", width=100)
    tree.column("In/Out", width=50)

    tree.heading("#0", text="Football player") 
    tree.heading("Football player", text="Football player") 
    tree.heading("Club", text="Club")
    tree.heading("Price", text="Price")
    tree.heading("Position", text="Position")
    tree.heading("Date of Transfer", text="Date of Transfer")
    tree.heading("In/Out", text="In/Out")

    for element in data:
        tree.insert("", tk.END,values=element)

    tree.place(x=80, y=280)

