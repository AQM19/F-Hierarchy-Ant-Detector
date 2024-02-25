#region Imports
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import customtkinter

from utils.YoloUtils import YoloUtils
#endregion

class Utils():  
    @staticmethod
    def select_file():
        file_path = filedialog.askopenfilename()
        return file_path
    
    @staticmethod
    def open_select_window(source):
        root = customtkinter.CTk()
        root.resizable(False, False)
        root.title("Tr.ANT.cker")
        root.geometry("300x400")

        button = customtkinter.CTkButton(
            master=root,
            text="Detect",
            command=lambda: YoloUtils.predict(source),
            width=120,
            height=32,
            border_width=0,
            corner_radius=8
        )
        button.place(relx=0.5, rely=0.5, anchor=CENTER)

        root.mainloop()