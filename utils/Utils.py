#region Imports
import os
import tkinter as tk
from tkinter import filedialog
#endregion

class Utils():  
    @staticmethod
    def select_file():
        file_path = filedialog.askopenfilename()
        return file_path