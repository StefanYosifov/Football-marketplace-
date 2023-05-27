import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GRadio_300=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_300["font"] = ft
        GRadio_300["fg"] = "#333333"
        GRadio_300["justify"] = "center"
        GRadio_300["text"] = "In"
        GRadio_300.place(x=30,y=100,width=85,height=25)
        GRadio_300["command"] = self.GRadio_300_command

        GRadio_164=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_164["font"] = ft
        GRadio_164["fg"] = "#333333"
        GRadio_164["justify"] = "center"
        GRadio_164["text"] = "Out"
        GRadio_164.place(x=120,y=100,width=85,height=25)
        GRadio_164["command"] = self.GRadio_164_command

        GRadio_638=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_638["font"] = ft
        GRadio_638["fg"] = "#333333"
        GRadio_638["justify"] = "center"
        GRadio_638["text"] = "All"
        GRadio_638.place(x=220,y=100,width=85,height=25)
        GRadio_638["command"] = self.GRadio_638_command

    def GRadio_300_command(self):
        print("command")


    def GRadio_164_command(self):
        print("command")


    def GRadio_638_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
