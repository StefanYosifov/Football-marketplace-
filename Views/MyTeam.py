import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label
from FileOperations.reader import readFromFile

def openMyTeam(self):
    new_window = Toplevel(self)
    new_window.title("My Team")
    width = 600
    height = 400
    screenwidth = new_window.winfo_screenwidth()
    screenheight = new_window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    new_window.geometry(alignstr)
    new_window.resizable(width=False, height=False)
    createTable(new_window)

def createTable(parent):
    data = readFromFile("Myteam.txt")

    tree = ttk.Treeview(parent)

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

    for player, details in data.items():
        tree.insert("", tk.END, text=player, values=[player] + details)  # Include the key in the values

    tree.pack()





