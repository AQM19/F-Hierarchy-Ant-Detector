from utils.Utils import Utils
from utils.YoloUtils import YoloUtils
from tkinter import Tk, Button, Label, Frame
from tkinter import ttk

# pip install requirements.txt
def main():
    print("Seleccionando archivo...")
    video_source = Utils.select_file()

    if not video_source:
        print("No se seleccionó ningún archivo.")
        return

    Utils.open_select_window(source=video_source)
    
if __name__ == '__main__':
    main()