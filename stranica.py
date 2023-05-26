import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("My football manager")
        #setting window size
        width=600
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_922=tk.Button(root)
        GButton_922["bg"] = "#f0f0f0"
        GButton_922["cursor"] = "watch"
        ft = tkFont.Font(family='Times',size=10)
        GButton_922["font"] = ft
        GButton_922["fg"] = "#000000"
        GButton_922["justify"] = "center"
        GButton_922["text"] = "My team"
        GButton_922.place(x=50,y=80,width=125,height=100)
        GButton_922["command"] = self.GButton_922_command

        GButton_467=tk.Button(root)
        GButton_467["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_467["font"] = ft
        GButton_467["fg"] = "#000000"
        GButton_467["justify"] = "center"
        GButton_467["text"] = "Marketplace"
        GButton_467.place(x=240,y=80,width=125,height=102)
        GButton_467["command"] = self.GButton_467_command

        GButton_788=tk.Button(root)
        GButton_788["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_788["font"] = ft
        GButton_788["fg"] = "#000000"
        GButton_788["justify"] = "center"
        GButton_788["text"] = "Deals history"
        GButton_788.place(x=440,y=80,width=125,height=101)
        GButton_788["command"] = self.GButton_788_command

    def GButton_922_command(self):
        print("command")


    def GButton_467_command(self):
        print("command")


    def GButton_788_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
