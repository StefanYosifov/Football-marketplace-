import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label
from FileOperations.reader import readFromFile
from Util.image import loadImage
from tkinter import messagebox
from FileOperations.reader import readFromFile,readFootballPlayerData
from FileOperations.writer import remove_row_by_name,add_row
from Util.image import loadImage
from Util.directories import *
from datetime import datetime
import tkinter.font as tkFont



text_file="MyTeam.txt"
marketplace_file=getDirectoryTwoBack()+"/Files/Marketplace.txt"
my_team_file=getDirectoryTwoBack()+"/Files/MyTeam.txt"
transaction_file=getDirectoryTwoBack()+"/Files/Transactions.txt"


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


    image_file = "/Files/Images/My team.png"
    loadImage(new_window,image_file)
    createTable(new_window)

def createTable(parent):
    data = readFromFile("Myteam.txt")

    def sellPlayer():
        selected_item = tree.focus()
        player_name = tree.item(selected_item)["text"]

        confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to sell {player_name}?")
        if confirmation:
            player_data=readFootballPlayerData(text_file,player_name)
            player_data_str=", ".join(str(item) for item in player_data)
            add_row(marketplace_file,player_data_str)
            full_name = player_data[0]
            team = player_data[2]
            price =player_data[3]
            position=player_data[6]
            current_date = datetime.now().strftime("%d-%m-%Y")
            status ="Out"
            transfer_data = []
            transfer_data.append(full_name)
            transfer_data.append(team)
            transfer_data.append(price)
            transfer_data.append(position)
            transfer_data.append(current_date)
            transfer_data.append(status)
            transfer_string = ", ".join(str(item) for item in transfer_data)
            remove_row_by_name(transaction_file,player_name)
            remove_row_by_name(my_team_file,player_name)
            add_row(transaction_file,transfer_string)
            tree.delete(selected_item)
            messagebox.showinfo("Success", f"{player_name} has been sold.")


    tree = ttk.Treeview(parent)

    tree["columns"] = ("Football player", "Birth Year", "Club", "Height", "Weight", "Rating", "Position")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Football player", width=120)  
    tree.column("Birth Year", width=100)
    tree.column("Club", width=150)
    tree.column("Height", width=50)
    tree.column("Weight", width=50)
    tree.column("Rating", width=50)
    tree.column("Position", width=100)

    tree.heading("#0", text="Football player") 
    tree.heading("Football player", text="Football player") 
    tree.heading("Birth Year", text="Birth Year")
    tree.heading("Club", text="Club")
    tree.heading("Height", text="Height")
    tree.heading("Weight", text="Weight")
    tree.heading("Rating", text="Rating")
    tree.heading("Position", text="Position")

    for player, details in data.items():
        tree.insert("", tk.END, text=player, values=[player] + details)

    tree.bind("<Double-Button-1>", lambda event: sellPlayer())

    tree.pack()

    GLabel_667=tk.Label(parent)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_667["font"] = ft
    GLabel_667["fg"] = "#333333"
    GLabel_667["justify"] = "center"
    GLabel_667["text"] = "You can sell your team members by double-clicking on them"
    GLabel_667.place(x=135,y=320,width=325,height=15)





