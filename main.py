from tkinter import *
import tkinter.font as tkFont
import os
import time
from FileOperations.reader import readFromFile
from Views.MyTeam import *
from Views.Marketplace import *
from Views.Transactions import *
from tkinter import ttk,Tk
from Util.directories import *


class App:
    def __init__(self, root):
        self.root = root
        def loadImage(self):
            image_file = "/Files/Images/Background.png"
            image_path = getImage(image_file)

            self.bg = PhotoImage(file=image_path)
            print(image_path)
            print(image_path)
            print(image_path)
            print(image_path)

            background_label = Label(root, image=self.bg)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            my_text=Label(root,text="Welcome to my team manager")
            my_text.pack(pady=50)


        root.title("My football manager")
        width = 600
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 1.5)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        loadImage(self)

    def GButton_922_command(self):
        print("My team command")
        openMyTeam(self.root)

       
    def GButton_467_command(self):
        print("Marketplace command")
        openMarketPlace(self.root)

    def GButton_788_command(self):
        print("Deals history command")
        openTransactions(self.root)

    def loadButtons(self):
        button_1 = Button(root, text="My Team", bg="#f0f0f0", font=('Times', 10), fg="#000000", justify="center",command=self.GButton_922_command)
        button_1.place(x=50, y=80, width=125, height=100)

        button_2 = Button(root, text="Marketplace", bg="#f0f0f0", font=('Times', 10), fg="#000000", justify="center",command=self.GButton_467_command)
        button_2.place(x=240, y=80, width=125, height=102)

        button_3 = Button(root, text="Deals history", bg="#f0f0f0", font=('Times', 10), fg="#000000", justify="center",command=self.GButton_788_command)
        button_3.place(x=440, y=80, width=125, height=101)



if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.loadButtons()
    file_data = readFromFile("MyTeam.txt")
    root.mainloop()
   
