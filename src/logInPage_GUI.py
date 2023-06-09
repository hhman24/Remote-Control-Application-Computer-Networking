from tkinter import*
import tkinter.font as font
from PIL import ImageTk, Image

import os
import sys

def path(file_name):
    file_name = 'pic\\' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, file_name)

class LogIn_Page_UI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.configure(
            bg = "#ff0000",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        parent.geometry("800x500+200+200")
        self.grid(row=0, column=0, sticky="nsew")

        #frames
        self.left = Frame(self,height= 500,width=400, bg = 'black')
        self.left.place(x=0,y=0)
        self.right = Frame(self,height= 500,width=400, bg='black')
        self.right.place(x=400,y=0)

        #left frame design
        self.left_image = ImageTk.PhotoImage(Image.open(path("bg2.jpg")))
        
        # goi label de pritn cai icon nay len do
        self.left_image_label = Label(self.left, image=self.left_image, bg='black')
        self.left_image_label.place(x=0, y=0)

        # Label - Your IP Addresss
        self.heading = Label(
            self.right,
            text='Your IP Addresss', 
            font='arial 15 bold', 
            bg='black',
            fg='#cc2121'
        )
        self.heading.place(x=80,y=150)
        #Entry - Input IP

        self.input = StringVar()

        self.entry_1 = Entry(
            self.right,
            textvariable = self.input,
            bg="black",
            highlightthickness=1,
            fg='white',
            relief="flat",
        )

        self.myFont = font.Font(family='Helvetica', size=20)

        self.entry_1['font'] = self.myFont

        self.entry_1.place(
            x=60,
            y=200,
            width=300.0,
            height=58.0,
        )
        # BUtton
        self.right_image = ImageTk.PhotoImage(Image.open(path("pbtt.png")))

        self.button_1 = Button(
            self.right,
            image=self.right_image,
            bg='black',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )

        self.button_1.place(
            x=180,
            y=300,
            height= 50,
            width=50,
        )






    


