from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from FileOperations.reader import readFromFile,readFootballPlayerData
from FileOperations.writer import remove_row_by_name,add_row
from Util.image import loadImage
from Util.directories import *
from datetime import datetime
from tkinter import messagebox




image_file="My team.png"
text_file=getDirectoryTwoBack()+"/Files/Marketplace.txt"
marketplace_file="Marketplace.txt"
my_team_file=getDirectoryTwoBack()+"/Files/MyTeam.txt"
transaction_file=getDirectoryTwoBack()+"/Files/Transactions.txt"


print(text_file)
print(text_file)
print(text_file)
print(text_file)



def openMarketPlace(self):
    new_window = Toplevel(self)
    new_window.title("New Window")
    width = 750
    height = 700
    screenwidth = new_window.winfo_screenwidth()
    screenheight = new_window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    new_window.geometry(alignstr)
    new_window.resizable(width=False, height=False)

    
    image_file = "/Files/Images/My Team.png"
    loadImage(new_window,image_file)

    label = Label(new_window)
    label.pack()

    def GButton_198_command():
        selected_name=GListBox_710.get(GListBox_710.curselection())
        print(selected_name)

        player_data=readFootballPlayerData(marketplace_file,selected_name)

        player_data_str=", ".join(str(item) for item in player_data)
        add_row(my_team_file,player_data_str)
        full_name = player_data[0]
        team = player_data[2]
        price =player_data[3]
        position=player_data[6]
        current_date = datetime.now().strftime("%d-%m-%Y")
        status ="In"
        transfer_data = []
        transfer_data.append(full_name)
        transfer_data.append(team)
        transfer_data.append(price)
        transfer_data.append(position)
        transfer_data.append(current_date)
        transfer_data.append(status)
        transfer_string = ", ".join(str(item) for item in transfer_data)

        transfer_log=readFootballPlayerData("Transactions.txt",full_name)
        if len(transfer_log) >=1:
            remove_row_by_name(transaction_file,full_name)
        add_row(transaction_file,transfer_string)
        remove_row_by_name(text_file,selected_name)

        GListBox_710.delete(GListBox_710.curselection())
        messagebox.showinfo("Success", f"{full_name} has been sold.")




    def on_listbox_click(event):
        selected_item = GListBox_710.get(GListBox_710.curselection())
        print("Selected item:", selected_item)
        data=readFootballPlayerData("Marketplace.txt",selected_item)
        # full_name=data[0]
        year=data[1]
        team=data[2]
        price=data[3]
        height=data[4]
        weight=data[5]
        position=data[6]
        GLabel_887["text"]=year
        GLabel_234["text"]=team
        GLabel_791["text"]=price
        GLabel_973["text"]=height
        GLabel_512["text"]=weight
        GLabel_751["text"]=position
        

    GListBox_710=tk.Listbox(new_window)
    GListBox_710["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GListBox_710["font"] = ft
    GListBox_710["fg"] = "#333333"
    GListBox_710["justify"] = "center"
    GListBox_710.place(x=10,y=150,width=150,height=400)
    GListBox_710.bind("<<ListboxSelect>>", on_listbox_click)
    
    footballers = readFromFile("Marketplace.txt")
    def createListBox(data):
        for footballer in data:
            GListBox_710.insert(tk.END, footballer.strip())
    
    createListBox(footballers)

    def on_lineEdit_search(event):
        selected_item = GLineEdit_335.get()
        GListBox_710.delete(0, tk.END)

        footballers = readFromFile("Marketplace.txt")
        for key in footballers:
            if selected_item.lower() in key.lower():
                GListBox_710.insert(tk.END, key)

        

    GLineEdit_335=tk.Entry(new_window)
    GLineEdit_335["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_335["font"] = ft
    GLineEdit_335["fg"] = "#333333"
    GLineEdit_335["justify"] = "center"
    GLineEdit_335["text"] = "Entry"
    GLineEdit_335.place(x=10,y=100,width=200,height=40)
    GLineEdit_335.bind("<Return>",on_lineEdit_search)

    GLabel_887=tk.Label(new_window)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_887["font"] = ft
    GLabel_887["fg"] = "#333333"
    GLabel_887["justify"] = "center"
    GLabel_887["text"] = "Year of Birth"
    GLabel_887.place(x=160,y=150,width=70,height=40)

    GLabel_234=tk.Label(new_window)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_234["font"] = ft
    GLabel_234["fg"] = "#333333"
    GLabel_234["justify"] = "center"
    GLabel_234["text"] = "Team"
    GLabel_234.place(x=230,y=150,width=70,height=40)


    GLabel_791=tk.Label(new_window)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_791["font"] = ft
    GLabel_791["fg"] = "#333333"
    GLabel_791["justify"] = "center"
    GLabel_791["text"] = "Price"
    GLabel_791.place(x=300,y=150,width=70,height=40)


    GLabel_973=tk.Label(new_window)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_973["font"] = ft
    GLabel_973["fg"] = "#333333"
    GLabel_973["justify"] = "center"
    GLabel_973["text"] = "Height"
    GLabel_973.place(x=370,y=150,width=70,height=40)

    GLabel_512=tk.Label(new_window)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_512["font"] = ft
    GLabel_512["fg"] = "#333333"
    GLabel_512["justify"] = "center"
    GLabel_512["text"] = "Weight"
    GLabel_512.place(x=440,y=150,width=70,height=40)


    GLabel_751=tk.Label(new_window)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_751["font"] = ft
    GLabel_751["fg"] = "#333333"
    GLabel_751["justify"] = "center"
    GLabel_751["text"] = "Position"
    GLabel_751.place(x=510,y=150,width=70,height=40)

    GListBox_130=tk.Listbox(new_window)
    GListBox_130["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GListBox_130["font"] = ft
    GListBox_130["fg"] = "#333333"
    GListBox_130["justify"] = "center"
    GListBox_130.place(x=240,y=20,width=120,height=70)

    GButton_198=tk.Button(new_window)
    GButton_198["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    GButton_198["font"] = ft
    GButton_198["fg"] = "#000000"
    GButton_198["justify"] = "center"
    GButton_198["text"] = "Buy"
    GButton_198.place(x=240,y=320,width=120,height=70)
    GButton_198["command"] = GButton_198_command




