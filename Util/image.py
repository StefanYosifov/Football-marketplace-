from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from FileOperations.reader import readFromFile 
from Util.directories import getImage

def loadImage(self,image_file):
            image_path = getImage(image_file)

            self.bg = PhotoImage(file=image_path)

            background_label = Label(self, image=self.bg)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)